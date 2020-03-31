from heuslertools.tools.measurement import Measurement

class TransportMeasurement(Measurement):
    """
    Object representing a transport measurement

    You can import it with

    ```from heuslertools.transport import TransportMeasurement```
    """

    def __init__(self, file, identifier):
        super().__init__(file, identifier, delimiter='\t')
