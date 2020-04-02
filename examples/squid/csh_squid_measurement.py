from heuslertools.squid import SQUIDMeasurement, SQUIDSample, fit_cw
from heuslertools.magnetism import Layer, Crystal
import matplotlib.pyplot as plt
import numpy as np


sample = SQUIDSample(length=4.481e-3, width=4.259e-3, weight=45.7 + 13.7)
gap = SQUIDSample(length=5.5e-3, width=4.5e-3, weight=-61.6)
reference = SQUIDSample(length=5.017e-3, width=3.8e-3, weight=50.0 + 13.7)
cumnsb = Crystal(a=6.09, n=4, mu_eff=5.4, t_cw=-160)
layer = Layer(l=sample.length, w=sample.width, h=40e-9, crystal=cumnsb)

sample_measurement = SQUIDMeasurement(
    'data/H1258_CSH_HipII110_[L]_45,7mg_+b13,7mg_m(T,5kOe,FC)_300K_to_4K_12062019.rso.dat')
gap_measurement = SQUIDMeasurement(
    'data/Gap_CSH_-61.6mg_m(T,5kOe,FC)_300K_to_4K_07062019.rso.dat')
reference_measurement = SQUIDMeasurement(
    'data/Reference_C21_1_1906_HipII110_[L]_CSH_50,0mg_+b13,7mg_m(T,5kOe,FC)_300K_to_4K_14062019.rso.dat')

sample_measurement.add_compensated_moment(
    'Temperature_K', 'Long_Moment_emu', gap_measurement, reference_measurement, sample, gap, reference)
sample_measurement.add_data_column('Suszeptibility_unitless', layer.emu_to_sus(
    sample_measurement.data['Compensated_Moment_emu'], sample_measurement.data['Field_Oe'][0]))

curie_weiss_fit = fit_cw(
    sample_measurement.data['Temperature_K'], sample_measurement.data['Suszeptibility_unitless'], 250, 300)


mu_eff = layer.crystal.get_exp_eff_moment_from_sus(curie_weiss_fit[0])
m_sat = layer.crystal.mu_eff_to_m_sat(mu_eff)
t_cw = -curie_weiss_fit[1] / curie_weiss_fit[0]
print("Tcw:", round(t_cw, 2), "K")
print("µ_eff: ", round(mu_eff, 2), "µ_b")
print("m_eff: ", round(m_sat, 2), "µ_b")

# plot compensated_moment
plt.figure()
plt.subplot(2, 1, 1)
plt.title("$T_{CW}=" + str(round(t_cw, 1)) + "K$" + "   $µ_{eff}=" +
          str(round(mu_eff, 1)) + "µ_{b}$" + "   $m_{sat}=" + str(round(m_sat, 1)) + "µ_{b}$")
plt.plot(sample_measurement.data['Temperature_K'],
         sample_measurement.data['Suszeptibility_unitless'])
plt.ylabel("$\chi$")
plt.subplot(2, 1, 2)
plt.plot(sample_measurement.data['Temperature_K'], 1 /
         sample_measurement.data['Suszeptibility_unitless'])
x = np.linspace(t_cw, 300, 10)
plt.plot(x, curie_weiss_fit[1] + x * curie_weiss_fit[0])
plt.ylabel("$1/\chi$")
plt.xlabel("Temperature [K]")

plt.tight_layout()
plt.show()
