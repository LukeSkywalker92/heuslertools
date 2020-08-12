from heuslertools.xrd import XRDMeasurement
import xrayutilities as xu
import numpy as np

class O2TSimulation(object):
    """Object representing omega two theta measurement.

    Parameters
    ----------
    file : str
        path of xrdml file containing o2t data.
    layerstack : xrayutilities layerstack
        layerstack to use for simulation.
    """

    def __init__(self, layerstack):
        self.set_layerstack(layerstack)
        self.en = 'CuKa1'
        self.wavelength = xu.wavelength('CuKa1')
        self.resol = 2e-11  # resolution in qz

    def set_layerstack(self, layerstack):
        """Set layerstack.

        Parameters
        ----------
        layerstack : xrayutilities layerstack
            layerstack to use for simulation.
        """
        self.layerstack = layerstack

    def simulate_o2t(self, H, K, L, qz_range, monochromator=xu.materials.Ge.planeDistance(2, 2, 0), polarization='both', I0=1000000000):
        sub = self.layerstack[0]
        qx = np.sqrt(sub.material.Q(H, K, L)[0]**2 + sub.material.Q(H, K, L)[1]**2)
        qz_center = (H+K+L)*2*np.pi/sub.material.a3[-1]
        qz = np.linspace(qz_center-(qz_range/2), qz_center+(qz_range/2), 2000)
        ai = xu.simpack.coplanar_alphai(qx, qz, self.en)
        thetaMono = np.arcsin(self.wavelength/(2 * monochromator))
        Cmono = np.cos(2 * thetaMono)
        md = xu.simpack.DynamicalModel(self.layerstack, resolution_width=self.resol,background=1, polarization=polarization, Cmono=Cmono, I0=I0)

        Idyn = md.simulate(ai, hkl=(H, K, L))
        return ai, Idyn
