import matplotlib.pyplot as plt
import numpy as np
from heuslertools.magnetism import Layer, Crystal
from heuslertools.squid import load_squid_data, gamma, fit_cw
from heuslertools.squid.csh import calculate_beta, interpolate_measurement, calculate_compensated_moment

FILEPATH_SAMPLE = '/home/luke/system01/heusler/Samples/H1256/SQUID/H1256_CSH_HipII110_[s]_47,9mg_+b13,7mg_m(T,5kOe,FC)_300K_to_4K_11062019.rso.dat'
FILEPATH_GAP = '/home/luke/system01/heusler/Lab/SQUID/CSH_InAs_1/Gap/Gap_CSH_-61.6mg_m(T,5kOe,FC)_300K_to_4K_07062019.rso.dat'
FILEPATH_REFERENCE = '/home/luke/system01/heusler/Lab/SQUID/CSH_InAs_1/Reference/Reference_C21_1_1906_HipII110_[L]_CSH_50.0mg_+b13,7mg_m(T,5kOe,FC)_300K_to_4K_14062019.rso.dat'
SAVE_PATH = ''
X = "temperature"
Y = "long_moment"

WEIGHT_SAMPLE = 47.9 + 13.7
WEIGHT_GAP = -61.6
WEIGHT_REFERENCE = 50.0 + 13.7

LENGTH_SAMPLE = 3.539e-3
WIDTH_SAMPLE = 4.556e-3
HEIGHT_SAMPLE = 36e-9

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
print(gamma_gap, gamma_sample, gamma_reference)
beta = calculate_beta(WEIGHT_GAP, WEIGHT_REFERENCE, WEIGHT_SAMPLE, gamma_gap, gamma_reference, gamma_sample)
print(beta)
data_sample["compensated_moment"] = calculate_compensated_moment(data_sample[Y], data_sample[X], interpolation_gap, interpolation_reference, beta)
data_sample["suszeptibility"] = sample.emu_to_sus(data_sample["compensated_moment"], FIELD)

# fit cw

fit = fit_cw(data_sample["temperature"], data_sample["suszeptibility"], 200, 300)
mu_eff = sample.crystal.get_exp_eff_moment_from_sus(fit[0])
m_sat = sample.crystal.mu_eff_to_m_sat(mu_eff)
print("Tcw:", round(-fit[1]/fit[0], 2), "K")
print("µ_eff: ", mu_eff)
print("m_eff: ", m_sat)

# plot compensated_moment
plt.figure()
plt.subplot(2,1,1)
plt.plot(data_sample[X], data_sample["suszeptibility"])
plt.subplot(2,1,2)
plt.plot(data_sample[X], 1/data_sample["suszeptibility"])
x = np.linspace(-200, 300, 400)
plt.plot(x, fit[1] + x*fit[0])
plt.show()
