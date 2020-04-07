"""
Functions to load xps data from measurement files
"""
import numpy as np
import matplotlib.pyplot as plt
from heuslertools.tools.measurement import Measurement

def load_xps_data(file):
    preload = np.genfromtxt(fname=file)
    if len(preload[0]) == 6:
        data = np.genfromtxt(fname=file, unpack=True, dtype=[("E_b", 'f8'), ("CH1", 'f8'), ("CH2", 'f8'), ("CH3", 'f8'), ("Date", 'U10'), ("Time", 'U8')])
    else:
        data = np.genfromtxt(fname=file, unpack=True, names=["E_b", "CH1", "CH2", "CH3"])
    return data

class XPSMeasurement(Measurement):
    """Object representing a Measurement

    Parameters
    ----------
    file : str
        path of file
    integration_time : float, optional
        integration time of measurement, if given cps are calculated, by default `None`
    """

    def __init__(self, file, integration_time=None, **kwargs):
        super().__init__(file, "", **kwargs)
        self.file = file
        if integration_time is not None:
            self.add_data_column("CH1_cps", self.data["CH1"]/integration_time)
            self.add_data_column("CH2_cps", self.data["CH2"]/integration_time)
            self.add_data_column("CH3_cps", self.data["CH3"]/integration_time)

    def _load_data(self):
        return load_xps_data(self.file)

    def append_measurement(self, file):
        """Append data from another file.

        Parameters
        ----------
        file : str
            path of file to append
        """
        self.data = np.append(self.data, load_xps_data(self.file))
