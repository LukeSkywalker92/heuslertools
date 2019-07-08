"""
Module for calculation of the \(\\gamma\)-factor
"""
import numpy as np
from scipy.interpolate import interp2d

LENGTH_ARRAY = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
WIDTH_ARRAY = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
FACTOR_ARRAY = [[0.9995, 0.9953, 0.9887, 0.979561, 0.968, 0.9541],
                [1.0015, 0.9974, 0.9907, 0.98035, 0.97, 0.956],
                [1.0049, 1.0007, 0.9939, 0.9816, 0.973, 0.959],
                [1.0096, 1.0054, 0.9986, 0.9847, 0.9775, 0.9634],
                [1.0156, 1.0114, 1.0045, 0.9892, 0.9832, 0.969],
                [1.023, 1.0187, 1.0117, 0.9951, 0.9902, 0.9759]]

f = interp2d(LENGTH_ARRAY, WIDTH_ARRAY, FACTOR_ARRAY, kind='cubic', bounds_error=True)

def gamma(length, width):
    """
    Calculates the \(\\gamma\)-factor for a given length and width of a sample.
    The length is always the dimension of the sample along the field direction.
    """
    return(f(length*1e3, width*1e3)[0])
