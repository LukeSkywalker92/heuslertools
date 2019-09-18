"""
Functions to load xps data from measurement files
"""
import numpy as np
import matplotlib.pyplot as plt

def load_xps_data(file):
    data = np.loadtxt(fname=file, unpack=True)
    return data

class XPSMeasurement(object):

    def __init__(self, file, integration_time=None):
        self.file = file
        self.data = {}
        self.data["E_b"], self.data["CH1"], self.data["CH2"], self.data["CH3"] = load_xps_data(self.file)
        if integration_time is not None:
            self.data["CH1"] = self.data["CH1"]/integration_time
            self.data["CH2"] = self.data["CH2"]/integration_time
            self.data["CH3"] = self.data["CH3"]/integration_time


    def append_measurement(self, file):
        new_data = load_xps_data(file)
        np.append(self.data["E_b"], new_data[0])
        np.append(self.data["CH1"], new_data[1])
        np.append(self.data["CH2"], new_data[2])
        np.append(self.data["CH3"], new_data[3])

    def plot(self, x, y, show=True):
        """
        Plot measurement with matplotlib
        """
        plt.figure()
        plt.plot(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        if show:
            plt.show()
