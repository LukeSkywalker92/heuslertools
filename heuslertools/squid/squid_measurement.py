from heuslertools.tools.measurement import Measurement
from heuslertools.squid.csh import calculate_compensated_moment, calculate_compensated_moment_ref_only
import numpy as np


class SQUIDMeasurement(Measurement):
    """
    Object representing a SQUID measurement

    You can import it with

    ```from heuslertools.squid import SQUIDMeasurement```
    """

    def __init__(self, file, **kwargs):
        super().__init__(file, "[Data]", delimiter=',', **kwargs)

    def add_compensated_moment(self, x, y, gap_measurement, reference_measurement, sample, gap_sample, reference_sample):
        interp_gap = gap_measurement.interpolation(x, y)
        interp_reference = reference_measurement.interpolation(x, y)
        compensated_moment = calculate_compensated_moment(np.array(self.data[y]), np.array(self.data[x]),
                                                          interp_gap, interp_reference,
                                                          sample.beta(gap_sample, reference_sample))
        self.add_data_column("Compensated_Moment_emu", compensated_moment)

    def add_compensated_moment_ref_only(self, x, y, reference_measurement, sample, reference_sample):
        interp_reference = reference_measurement.interpolation(x, y)
        compensated_moment = calculate_compensated_moment_ref_only(np.array(self.data[y]), np.array(self.data[x]),
                                                                   interp_reference,
                                                                   sample, reference_sample)
        self.add_data_column("Compensated_Moment_emu", compensated_moment)

    def mean_field(self):
        return round(np.mean(self.data['Field_Oe']),1)

    def mean_temperature(self):
        return round(np.mean(self.data['Temperature_K']),1)
