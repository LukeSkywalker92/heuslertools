from heuslertools.tools.measurement import Measurement
import datetime
from numpy.lib.recfunctions import append_fields
import numpy as np

class MBEMeasurement(Measurement):
    """
    Object representing a MBE measurement

    You can import it with

    ```from heuslertools.mbe import MBEMeasurement```
    """

    def __init__(self, file, **kwargs):
        super().__init__(file, None, delimiter='\t', **kwargs)
        date_time = np.array([np.datetime64(datetime.datetime.strptime(str(int(time)),"%Y%m%d%H%M%S")) for time in self.data['Time']])
        self.data = append_fields(self.data, 'Datetime_Datetime', date_time)
        self._generate_names()