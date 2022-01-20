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
        super().__init__(file, None, delimiter='\t', dtype=None, **kwargs)
        date_time = np.array([np.datetime64(datetime.datetime.strptime(time,"%Y-%m-%d-%H-%M-%S")) for time in self.data['Time']])
        self.data = append_fields(self.data, 'Datetime_Datetime', date_time)
        self._generate_names()
        self.add_data_column('Time_Seconds', [(date-self.data['Datetime_Datetime'][0]).item().total_seconds() for date in self.data['Datetime_Datetime']])