import matplotlib.pyplot as plt
import numpy as np
from heuslertools.magnetism import Layer, Crystal
from heuslertools.squid import load_squid_data, gamma, fit_cw
from heuslertools.squid.csh import calculate_beta, interpolate_measurement, calculate_compensated_moment

FILEPATH_SAMPLE = 'data/H1258_CSH_HipII110_[L]_45,7mg_+b13,7mg_m(T,5kOe,FC)_300K_to_4K_12062019.rso.dat'
FILEPATH_GAP = 'data/Gap_CSH_-61.6mg_m(T,5kOe,FC)_300K_to_4K_07062019.rso.dat'
FILEPATH_REFERENCE = 'data/Reference_C21_1_1906_HipII110_[L]_CSH_50,0mg_+b13,7mg_m(T,5kOe,FC)_300K_to_4K_14062019.rso.dat'
SAVE_PATH = ''
X = "temperature"
Y = "long_moment"

WEIGHT_SAMPLE = 45.7 + 13.7
WEIGHT_GAP = -61.6
WEIGHT_REFERENCE = 50.0 + 13.7

LENGTH_SAMPLE = 4.481e-3
WIDTH_SAMPLE = 4.259e-3
HEIGHT_SAMPLE = 40e-9

LENGTH_GAP = 5.5e-3
WIDTH_GAP = 4.5e-3

LENGTH_REFERENCE = 5.017e-3
WIDTH_REFERENCE = 3.8e-3

FIELD = 5000
fit_range = [250, 300]

cumnsb = Crystal(a=6.09, n=4, mu_eff=5.4, t_cw=-160)
sample = Layer(l=LENGTH_SAMPLE, w=WIDTH_SAMPLE, h=HEIGHT_SAMPLE, crystal=cumnsb)

# load data
data_sample = load_squid_data(FILEPATH_SAMPLE)
data_gap = load_squid_data(FILEPATH_GAP)
data_reference = load_squid_data(FILEPATH_REFERENCE)

# interpolate gap and reference signal
interpolation_gap = interpolate_measurement(data_gap[X], data_gap[Y])
interpolation_reference = interpolate_measurement(data_reference[X], data_reference[Y])

# calculate compensated signal
gamma_sample = gamma(LENGTH_SAMPLE, WIDTH_SAMPLE)
gamma_gap = gamma(LENGTH_GAP, WIDTH_GAP)
gamma_reference = gamma(LENGTH_REFERENCE, WIDTH_REFERENCE)
beta = calculate_beta(WEIGHT_GAP, WEIGHT_REFERENCE, WEIGHT_SAMPLE, gamma_gap, gamma_reference, gamma_sample)
data_sample["compensated_moment"] = calculate_compensated_moment(data_sample[Y], data_sample[X], interpolation_gap, interpolation_reference, beta)
data_sample["suszeptibility"] = sample.emu_to_sus(data_sample["compensated_moment"], FIELD)

# fit cw

fit = fit_cw(data_sample["temperature"], data_sample["suszeptibility"], fit_range[0], fit_range[1])


mu_eff = sample.crystal.get_exp_eff_moment_from_sus(fit[0])
m_sat = sample.crystal.mu_eff_to_m_sat(mu_eff)
t_cw = -fit[1]/fit[0]
print("Tcw:", round(t_cw, 2), "K")
print("µ_eff: ", round(mu_eff, 2), "µ_b")
print("m_eff: ", round(m_sat, 2), "µ_b")

# plot compensated_moment
plt.figure()
plt.subplot(2,1,1)
plt.title("$T_{CW}=" + str(round(t_cw, 1)) + "K$" + "   $µ_{eff}=" + str(round(mu_eff, 1)) + "µ_{b}$" + "   $m_{sat}=" + str(round(m_sat, 1)) + "µ_{b}$")
plt.plot(data_sample[X], data_sample["suszeptibility"])
plt.ylabel("$\chi$")
plt.subplot(2,1,2)
plt.plot(data_sample[X], 1/data_sample["suszeptibility"])
x = np.linspace(t_cw, 300, 10)
plt.plot(x, fit[1] + x*fit[0])
plt.ylabel("$1/\chi$")
plt.xlabel("Temperature [K]")

plt.tight_layout()
plt.savefig(FILEPATH_SAMPLE + '.png')
plt.show()
