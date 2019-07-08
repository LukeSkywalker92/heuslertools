"""
CSH related tools
"""
import numpy as np
from scipy.interpolate import interp1d

def calculate_beta(weight_gap, weight_reference, weight_sample, gamma_gap, gamma_reference, gamma_sample):
    """
    Calculates the factor \(\\beta\) that is needed to calculate the compensated moment of a sample.
    """
    return ((weight_reference*gamma_reference)-(weight_sample*gamma_sample))/(weight_gap*gamma_gap)

def interpolate_measurement(x, y):
    """
    Interpolates a measurement and returnes the interpolation as a function.
    To access a y value of the interpolation, just call the returned function
    with the x value.
    """
    return interp1d(x, y, bounds_error=False)

def calculate_compensated_moment(moment_sample, x_sample, interp_gap, interp_reference, beta):
    """
    Calculates the compensated moment for a measurement of a sample.
    """
    return moment_sample - interp_reference(x_sample) + (beta * interp_gap(x_sample))
