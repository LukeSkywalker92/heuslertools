from heuslertools.tools.measurement import Measurement
import xrayutilities as xu
import warnings

class XRDMeasurement(Measurement):
    """Object representing xrd measurement.

    Parameters
    ----------
    file : str
        path of xrdml file.

    Attributes
    ----------
    en : str
        Energy of xrays.
    wavelength : type
        wavelength of xrays.
    resol : float
        resolution in qz.

    """

    def __init__(self, file):
        super().__init__(file, "")
        self.en = 'CuKa1'
        self.wavelength = xu.wavelength('CuKa1')
        self.resol = 2e-10  # resolution in qz

    def _load_data(self):
        self.xrdml = xu.io.XRDMLFile(self.file)
        return self.xrdml.scans[0].ddict

    def _generate_names(self):
        for name in self.data:
            self.names[name] = {"short_name": name, "unit": "a.u."}

    def add_data_column(self, name, data):
        warnings.warn('add_data_column not availiable for XRDMeasurement', stacklevel=2)
        warnings.warn
