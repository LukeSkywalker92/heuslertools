from heuslertools.tools.measurement import Measurement
import xrayutilities as xu
import warnings
import numpy as np

class RSMMeasurement(Measurement):
    """Object representing rsm measurement.

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

    def __init__(self, file, material=None, geometry='hi_lo', beam_direction=None, surface_normale=None, reflex=None):
        self.material = material
        self.geometry = geometry
        self.beam_direction = beam_direction
        self.surface_normale = surface_normale
        self.reflex = reflex
        if any(elem is not None for elem in [material, geometry, beam_direction, surface_normale, reflex]):
            self._create_experiment()
        super().__init__(file, "")

    def _load_data(self):
        data = {}
        data['scanmot'], data['Omega'], data['2Theta'], data['Chi'], data['Phi'], data['psd'] = xu.io.getxrdml_scan(self.file, 'om', 'tt', 'c', 'p')
        return data

    def _generate_names(self):
        for name in self.data:
            self.names[name] = {"short_name": name, "unit": "a.u."}

    def _create_experiment(self):
        self.hxrd = xu.HXRD(self.material.Q(self.beam_direction),
                            self.material.Q(self.surface_normale),
                            geometry=self.geometry)
        
        
    def _get_nominal_angle(self, axis):
        angles = {}
        [angles['Omega'],
         angles['Chi'],
         angles['Phi'],
         angles['2Theta']] = self.hxrd.Q2Ang(self.material.Q(self.reflex))
        return angles[axis]

    def _get_substrate_peak(self):
        # anggridder = xu.FuzzyGridder2D(500, 500)
        # anggridder(self.data['Omega'], self.data['2Theta'], self.data['psd'])
        # angINT = xu.maplog(anggridder.data.transpose(), 10, 0)
        # return anggridder.xaxis[np.unravel_index(angINT.argmax(), angINT.shape)[0]], anggridder.yaxis[np.unravel_index(angINT.argmax(), angINT.shape)[1]]
        threshold = 10**int(np.log10(self.data['psd'].max()))
        max_values = np.where(self.data['psd'] > threshold)
        return np.mean(self.data['Omega'][max_values]), np.mean(self.data['2Theta'][max_values])


    def get_angle_data(self, size=300, dynamic_range=10):
        anggridder = xu.FuzzyGridder2D(300, 300)
        anggridder(self.data['Omega'], self.data['2Theta'], self.data['psd'])
        angINT = xu.maplog(anggridder.data.transpose(), 3.3, 0)
        return anggridder, angINT

    def get_q_data(self, size=300, dynamic_range=10, om_sub=None, tt_sub=None):
        sub_peak = self._get_substrate_peak()
        if om_sub == None:
            om_sub = sub_peak[0]
        if tt_sub == None:
            tt_sub = sub_peak[1]
        #om_sub, tt_sub = self._get_substrate_peak()
        qx, qy, qz = self.hxrd.Ang2Q(self.data['Omega'],
                                     self.data['2Theta'],
                                     delta=[om_sub - self._get_nominal_angle('Omega'),
                                            tt_sub - self._get_nominal_angle('2Theta')])
        qgridder = xu.FuzzyGridder2D(size, size)
        qgridder(qy, qz, self.data['psd'])
        qINT = xu.maplog(qgridder.data.transpose(), dynamic_range, 0)
        return qgridder, qINT

    def get_hkl_data(self, size=300, dynamic_range=10, om_sub=None, tt_sub=None):
        sub_peak = self._get_substrate_peak()
        if om_sub == None:
            om_sub = sub_peak[0]
        if tt_sub == None:
            tt_sub = sub_peak[1]
        #om_sub, tt_sub = self._get_substrate_peak()
        h, k, l = self.hxrd.Ang2HKL(self.data['Omega'],
                               self.data['2Theta'],
                               delta=[om_sub - self._get_nominal_angle('Omega'),
                                      tt_sub - self._get_nominal_angle('2Theta')],
                               mat=self.material)
        hklgridder = xu.FuzzyGridder2D(size, size)
        hklgridder(h, l, self.data['psd'])
        hklINT = xu.maplog(hklgridder.data.transpose(), dynamic_range, 0)
        return hklgridder, hklINT