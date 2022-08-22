from heuslertools.tools.measurement import Measurement
import numpy as np


# def conv(file):
#     i=0
#     for x in open(file):
#         if i == 2:
#             yield x.replace('#', 'Number').encode()
#         else:
#             yield x.replace(',', '.').encode()
#         i+=1

def load_musr_data(file):
    data = np.genfromtxt(file, comments='#', skip_header=0, names=True)
    return data

class MUSRMeasurement(Measurement):
    """
    Object representing a SIMS measurement

    You can import it with

    ```from heuslertools.sims import SIMSMeasurement```
    """

    def __init__(self, file, **kwargs):
        super().__init__(file, "", **kwargs)

    def _load_data(self):
        return load_musr_data(self.file)

    def append_measurement(self, file):
        """Append data from another file.

        Parameters
        ----------
        file : str
            path of file to append
        """
        self.data = np.append(self.data, load_musr_data(file))