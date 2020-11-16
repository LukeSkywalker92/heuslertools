from heuslertools.tools.measurement import Measurement
import numpy as np


def conv(file):
    i=0
    for x in open(file):
        if i == 2:
            print('yay')
            yield x.replace('#', 'Number').encode()
        else:
            yield x.replace(',', '.').encode()
        i+=1

def load_sims_data(file):
    data = np.genfromtxt((conv(file)), delimiter='\t', comments='#', skip_header=2, names=True)
    print(data.dtype.names)
    return data

class SIMSMeasurement(Measurement):
    """
    Object representing a SIMS measurement

    You can import it with

    ```from heuslertools.sims import SIMSMeasurement```
    """

    def __init__(self, file, **kwargs):
        super().__init__(file, "", **kwargs)

    def _load_data(self):
        return load_sims_data(self.file)

    def append_measurement(self, file):
        """Append data from another file.

        Parameters
        ----------
        file : str
            path of file to append
        """
        self.data = np.append(self.data, load_sims_data(file))