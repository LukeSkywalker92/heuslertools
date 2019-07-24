"""
Functions to load transport data from measurement files
"""
import numpy as np
from tabulate import tabulate
from heuslertools.tools.data_handling import search_data_start

def load_transport_data(file, identifier):
    """
    Loads a transport measurement and returns the data
    moment data.
    """
    data = {}

    data = np.genfromtxt(fname=file, delimiter='\t', skip_header=search_data_start(file, identifier)-1, names=True)
    return data


class TransportMeasurement(object):
    """
    Object representing a transport measurement
    """

    def __init__(self, file, identifier):
        self.file = file
        """Path of the data file"""
        self.identifier = identifier
        """identifier for data start"""
        self.data = load_transport_data(self.file, self.identifier)
        self.names = {}
        for name in self.data.dtype.names:
            self.names[name]={"short_name": name.split("_")[0], "unit":name.split("_")[-1]}

    def append_measurement(self, file, identifier):
        """
        Append data from another file.
        """
        self.data = np.append(self.data, load_transport_data(file, identifier))

    def print_names(self):
        """
        Show availiable names of the data file that can be used to access the data.
        """
        headers = ["name", "short_name", "unit"]
        table = [[name, self.names[name]["short_name"], self.names[name]["unit"]] for name in self.data.dtype.names]
        print("Availiable names:")
        print(tabulate(table, headers))
