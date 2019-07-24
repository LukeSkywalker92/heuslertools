"""
Functions to load SQUID data from measurement files
"""
import numpy as np
from heuslertools.tools.data_handling import search_data_start

def load_squid_data(file):
    """
    Loads a SQUID measurement and returns the field, temperature and long
    moment data.
    """
    data = {}
    data["field"], data["temperature"], data["long_moment"] = np.loadtxt(fname=file, skiprows=search_data_start(file, "[Data]"), delimiter=",", usecols = (2,3,4), unpack=True)
    return data
