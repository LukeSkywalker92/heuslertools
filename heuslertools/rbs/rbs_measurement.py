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

    def __init__(self, file, **kwargs):
        names = ["D1_Channel_Channel", "D1_Intensity_Counts",
                 "D2_Channel_Channel", "D2_Intensity_Counts",
                 "D3_Channel_Channel", "D3_Intensity_Counts",
                 "D4_Channel_Channel", "D4_Intensity_Counts"]
        super().__init__(file, "Data:", names=names, encoding='latin_1', **kwargs)
