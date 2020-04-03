from heuslertools.xrd import XRDMeasurement
import xrayutilities as xu
import numpy as np

class OmegaMeasurement(XRDMeasurement):
    """Object representing omega measurement.

    Parameters
    ----------
    file : str
        path of xrdml file with omega data.

    """

    def __init__(self, file):
        super().__init__(file)

    def voigt_fit(self):
        """Performs voigt fit.

        Returns
        -------
        array
            Fit parameters.
        callable
            callable fit function
        """
        fit_params, sd_params, itlim, fitfunc = xu.math.fit.peak_fit(self.data['Omega'], self.data['detector'], peaktype='PseudoVoigt', plot=False, func_out=True)
        return fit_params, fitfunc
