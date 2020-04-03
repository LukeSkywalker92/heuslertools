from heuslertools.xrd import XRDMeasurement
import xrayutilities as xu
import numpy as np

class O2TMeasurement(XRDMeasurement):
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

    def simulate_o2t(self, H, K, L, bounds, monochromator=xu.materials.Ge.planeDistance(2, 2, 0), polarization='both', I0=1000000000):
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
        sub = self.layerstack[0]
        qx = np.sqrt(sub.material.Q(H, K, L)[0]**2 + sub.material.Q(H, K, L)[1]**2)
        tt = self.data['2Theta']
        ai = tt/2
        qz = xu.simpack.get_qz(qx, ai, self.en)
        thetaMono = np.arcsin(self.wavelength/(2 * monochromator))
        Cmono = np.cos(2 * thetaMono)
        md = xu.simpack.DynamicalModel(self.layerstack, resolution_width=self.resol,background=1, polarization=polarization, Cmono=Cmono, I0=I0)

        fitmdyn = xu.simpack.FitModel(md)
        fitmdyn.set_param_hint(sub.material.name+'_a', vary=True)
        fitmdyn.set_param_hint('resolution_width', vary=True)
        for l in self.layerstack[1:]:
            name = l.material.name.replace('(', '_').replace(')', '_').replace('.', '_')
            fitmdyn.set_param_hint(name+'_c', vary=True)
            fitmdyn.set_param_hint(name+'_a', expr=sub.material.name+'_a')
            fitmdyn.set_param_hint(name+'_thickness', vary=True)
        for bound in bounds:
            fitmdyn.set_param_hint(bound['name'], min=bound['min'], max=bound['max'])
        paramsdyn = fitmdyn.make_params()
        fitmdyn.lmodel.set_hkl((H, K, L))
        fitr = fitmdyn.fit(self.data['detector'], paramsdyn, ai)
        simdyn = fitmdyn.eval(fitr.params, x=tt/2)
        return simdyn, fitr
