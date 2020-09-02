"""
Functions to load xps data from measurement files
"""
import numpy as np
import matplotlib.pyplot as plt
from heuslertools.tools.measurement import Measurement
from heuslertools.tem.ser_reader import serReader

class TEMMeasurement(Measurement):
    """Object representing a Measurement

    Parameters
    ----------
    file : str
        path of file
    integration_time : float, optional
        integration time of measurement, if given cps are calculated, by default `None`
    """

    def __init__(self, file, **kwargs):
        super().__init__(file, "", **kwargs)

    def _load_data(self):
        return serReader(self.file)

    def _generate_names(self):
        for name in self.data:
            self.names[name] = {"short_name": name, "unit": "a.u."}

    def append_measurement(self, file):
        """Append data from another file.

        Parameters
        ----------
        file : str
            path of file to append
        """
        self.data = np.append(self.data, serReader(file))

    def tem_xy_ticks(self, ax):
        ax.tick_params(
            axis='both',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            left=False,
            right=False,
            labelbottom=False,
            labelleft=False)
