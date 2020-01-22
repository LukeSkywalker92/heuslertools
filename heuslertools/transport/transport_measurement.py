import numpy as np
from numpy.lib.recfunctions import append_fields
import matplotlib.pyplot as plt
from tabulate import tabulate
from heuslertools.transport.load_transport_data import load_transport_data

class TransportMeasurement(object):
    """
    Object representing a transport measurement

    You can import it with

    ```from heuslertools.transport import TransportMeasurement```
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

    def add_data_column(self, name, data):
        self.data = append_fields(self.data, name, data, np.float)
        for name in self.data.dtype.names:
            self.names[name]={"short_name": name.split("_")[0], "unit":name.split("_")[-1]}


    def append_measurement(self, file, identifier):
        """
        Append data from another file.
        """
        self.data = np.append(self.data, load_transport_data(file, identifier))

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


    def print_names(self):
        """
        Show availiable names of the data file that can be used to access the data.
        """
        headers = ["name", "short_name", "unit"]
        table = [[name, self.names[name]["short_name"], self.names[name]["unit"]] for name in self.data.dtype.names]
        print("Availiable names:")
        print(tabulate(table, headers))
