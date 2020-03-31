from heuslertools.tools.measurement import Measurement

class SQUIDMeasurement(Measurement):
    """
    Object representing a SQUID measurement

    You can import it with

    ```from heuslertools.squid import SQUIDMeasurement```
    """

    def __init__(self, file):
        super().__init__(file, "[Data]", delimiter=',')
