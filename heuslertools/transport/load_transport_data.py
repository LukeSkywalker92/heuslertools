"""
Functions to load transport data from measurement files
"""
import numpy as np
from heuslertools.tools.data_handling import search_data_start
import warnings

def load_transport_data(file, identifier):
    """
    Loads a transport measurement and returns the data
    moment data.
    """
    warnings.warn("load_transport_data is deprecated. Use TransportMeasurement object instead.", DeprecationWarning, stacklevel=2)
    data = {}
    data = np.genfromtxt(fname=file, delimiter='\t', skip_header=search_data_start(file, identifier)-1, names=True)
    first_line = [str(i) for i in data[0]]
    if 'nan' in first_line:
        data = data[1:]
    return data
