from heuslertools.xrd import XRDMeasurement
import xrayutilities as xu
import numpy as np

class XRRMeasurement(XRDMeasurement):
    """Object representing omega two theta measurement.

    Parameters
    ----------
    file : str
        path of xrdml file containing o2t data.
    layerstack : xrayutilities layerstack
        layerstack to use for simulation.
    """

    def __init__(self, file, layerstack=None):
        super().__init__(file)
        if layerstack is not None:
            self.set_layerstack(layerstack)

    def set_layerstack(self, layerstack):
        """Set layerstack.

        Parameters
        ----------
        layerstack : xrayutilities layerstack
            layerstack to use for simulation.
        """
        self.layerstack = layerstack

    def simulate_xrr(self, bounds=[], monochromator=xu.materials.Ge.planeDistance(2, 2, 0), I0=1000000000, offset=0.0, xmin=-np.inf, xmax=np.inf, plot=False, verbose=False):
        """Short summary.

        Parameters
        ----------
        H : int
            `H`.
        K : int
            `K`.
        L : int
            `L`.
        bounds : dict
            Bounds for simulation `bounds`.
        monochromator : xu.materials.Ge.planeDistance(2, 2, 0)
            xu.materials.Ge.planeDistance(2, 2, 0).
        polarization : str
            'both'.
        I0 : type
            Intensity of x rays.

        Returns
        -------
        array:
            Simulated data.
        fitreport:
            report containing all simulation parameters

        """
        tt = self.data['2Theta'] - offset
        ai = tt/2
        md = xu.simpack.SpecularReflectivityModel(self.layerstack, energy=self.en, resolution_width=self.resol,background=1, I0=I0)

        fitm = xu.simpack.FitModel(md, plot=plot, verbose=verbose)
        for bound in bounds:
            fitm.set_param_hint(**bound)
        fitm.set_fit_limits(xmin=xmin, xmax=xmax)
        params = fitm.make_params()
        fitr = fitm.fit(self.data['detector'], params, ai)
        simdyn = fitm.eval(fitr.params, x=tt/2)
        return simdyn, fitr
