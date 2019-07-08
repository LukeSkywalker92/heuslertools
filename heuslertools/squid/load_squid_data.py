"""
Functions to load SQUID data from measurement files
"""
import numpy as np

def search_data_start(file, identifier):
    """
    Returns the line of an identifier for the start of the data in a file.
    """
    search = open(file)
    i = 1
    for line in search:
        if identifier in line:
            search.close()
            return i + 1
        i += 1

def load_squid_data(file):
    """
    Loads a SQUID measurement and returns the field, temperature and long
    moment data.
    """
    data = {}
    data["field"], data["temperature"], data["long_moment"] = np.loadtxt(fname=file, skiprows=search_data_start(file, "[Data]"), delimiter=",", usecols = (2,3,4), unpack=True)
    return data
