import numpy as np

def fit_cw(temperatures, suszeptibilities, min, max):
    fit_temp_array = np.array([])
    fit_moment_array = np.array([])
    for i in range(0, suszeptibilities.size):
        if temperatures[i] > min and temperatures[i] < max:
            fit_temp_array = np.append(fit_temp_array, temperatures[i])
            fit_moment_array = np.append(fit_moment_array, suszeptibilities[i])
    return np.polyfit(fit_temp_array, 1/fit_moment_array, 1)
