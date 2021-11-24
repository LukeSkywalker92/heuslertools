from heuslertools.tools.measurement import Measurement
import numpy as np


class RBSMeasurement(Measurement):
    """
    Object representing a RBS measurement

    D1: RBS
    D2: PIXE

    You can import it with

    ```from heuslertools.rbs import RBSMeasurement```
    """

    def __init__(self, file,
                 d1_calib_factor=1.773, d1_offset=13.0,
                 d2_calib_factor=0.019898, d2_offset=0.695,
                 d3_calib_factor=1.5896, d3_offset=13.000000,
                 d4_calib_factor=0.0166, d4_offset=0.0,
                 **kwargs):
        names = ["D1_Channel_Channel", "D1_Intensity_Counts",
                 "D2_Channel_Channel", "D2_Intensity_Counts",
                 "D3_Channel_Channel", "D3_Intensity_Counts",
                 "D4_Channel_Channel", "D4_Intensity_Counts"]
        super().__init__(file, "Data:", names=names, encoding='latin_1', **kwargs)
        self.add_data_column('D1_Energy_keV', d1_calib_factor*self.data['D1_Channel_Channel']-d1_offset)
        self.add_data_column('D2_Energy_keV', d2_calib_factor*self.data['D2_Channel_Channel']-d2_offset)
        self.add_data_column('D3_Energy_keV', d3_calib_factor*self.data['D3_Channel_Channel']-d3_offset)
        self.add_data_column('D4_Energy_keV', d4_calib_factor*self.data['D4_Channel_Channel']-d4_offset)
