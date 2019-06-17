import numpy as np
from scipy.interpolate import interp1d

def calculate_beta(weight_gap, weight_reference, weight_sample, gamma_gap, gamma_reference, gamma_sample):
    return ((weight_reference*gamma_reference)-(weight_sample*gamma_sample))/(weight_gap*gamma_gap)

def interpolate_measurement(x, y):
    return interp1d(x, y, bounds_error=False)

def calculate_compensated_moment(moment_sample, x_sample, interp_gap, interp_reference, beta):
    return moment_sample - interp_reference(x_sample) + (beta * interp_gap(x_sample))
