import numpy as np
from numpy.lib.recfunctions import append_fields
import matplotlib.pyplot as plt
from tabulate import tabulate
from heuslertools.tools.data_handling import load_data
from scipy.interpolate import interp1d

class Measurement(object):
    """
    Object representing a measurement
    """

    def __init__(self, file, identifier, delimiter=None):
        self.file = file
        """Path of the data file"""
        self.identifier = identifier
        """identifier for data start"""
        self.delimiter = delimiter
        self.data = load_data(self.file, self.identifier, self.delimiter)
        self.names = {}
        for name in self.data.dtype.names:
            self.names[name]={"short_name": ' '.join(name.split("_")[0:-1]), "unit":name.split("_")[-1]}

    def add_data_column(self, name, data):
        """
        Append column to data.
        """
        self.data = append_fields(self.data, name, data, np.float)
        for name in self.data.dtype.names:
            self.names[name]={"short_name": name.split("_")[0], "unit":name.split("_")[-1]}

    def append_measurement(self, file, identifier):
        """
        Append data from another file.
        """
        self.data = np.append(self.data, load_data(self.file, self.identifier, self.delimiter))

    def plot(self, x, y, show=True):
        """
        Plot measurement with matplotlib
        """
        plt.figure()
        plt.plot(self.data[x], self.data[y])
        plt.xlabel(self.names[x]["short_name"] + ' (' + self.names[x]["unit"] + ')')
        plt.ylabel(self.names[y]["short_name"] + ' (' + self.names[y]["unit"] + ')')
        if show:
            plt.show()

    def get_unit(self, name):
        return self.names[name]["unit"]

    def get_short_name(self, name):
        return self.names[name]["short_name"]

    def get_axis_label(self, name):
        return self.get_short_name(name) + ' (' + self.get_unit(name) + ')'

    def interpolation(self, x, y, kind='linear'):
        return interp1d(self.data[x], self.data[y], bounds_error=False, kind=kind)

    def print_names(self):
        """
        Show availiable names of the data file that can be used to access the data.
        """
        headers = ["name", "short_name", "unit"]
        table = [[name, self.names[name]["short_name"], self.names[name]["unit"]] for name in self.data.dtype.names]
        print("Availiable names:")
        print(tabulate(table, headers))
