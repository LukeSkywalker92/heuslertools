from heuslertools.tools.measurement import Measurement
from heuslertools.squid.csh import calculate_compensated_moment
import numpy as np


class SQUIDMeasurement(Measurement):
    """
    Object representing a SQUID measurement

    You can import it with

    ```from heuslertools.squid import SQUIDMeasurement```
    """

    def __init__(self, file):
        super().__init__(file, "[Data]", delimiter=',')

    def add_compensated_moment(self, x, y, gap_measurement, reference_measurement, sample, gap_sample, reference_sample):
        interp_gap = gap_measurement.interpolation(x, y)
        interp_reference = reference_measurement.interpolation(x, y)
        compensated_moment = calculate_compensated_moment(self.data[y], self.data[x],
                                                          interp_gap, interp_reference,
                                                          sample.beta(gap_sample, reference_sample))
        self.add_data_column("Compensated_Moment_emu", compensated_moment)
