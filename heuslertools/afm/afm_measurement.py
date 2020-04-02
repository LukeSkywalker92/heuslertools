import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from skimage.measure import profile_line
import os

class AFMMeasurement(object):
    """
    Object representing a afm measurement.
    You can import it with `from heuslertools.afm import AFMMeasurement`

    Parameters
    ----------
    file : str
        Path of the data file. Can be `.txt` (DME) or `.asc` (gwyddion) file. If file extension is `.txt` (DME) z data is
        multiplied by a factor of `1e10`.
    size : tuple
        Size of the measurement in `(meter, meter)`, e.g. `(1e-6, 1e-6)`
    """

    def __init__(self, file, size):
        self._file = file
        """Path of the data file"""
        self.x = []
        """Data positions in x"""
        self.y = []
        """Data positions in y"""
        self.z = []
        """Height data"""
        self._x_size, self._y_size = self._size
        self._factor = 1e10
        if os.path.splitext(self._file)[1] == '.asc':
            self._factor = 1
        self._load_data()

    def _load_data(self):
        data = np.loadtxt(self._file)
        self.x = []
        self.y = []
        for i in range(1, len(data[0])+1):
            self.x.append(i)
        for i in range(1, len(data)+1):
            self.y.append(i)
        self.z=(data-np.min(data))*self._factor

    def rms_roughness(self):
        """
        Returns the RMS roughness of the AFM measurement in nm.

        Returns
        -------
        float
            RMS roughness in nm
        """
        z = []
        for i in self.z:
            for j in i:
                z.append(j)
        return(np.std(z))

    def profile(self, src, dst, linewidth=1, order=3):
        """
        Calculates profile for given start and endpoints.

        Parameters
        ----------
        src : tuple
            start points of profile `(x0, y0)`
        dst : tuple
            end points of profile `(x1, y1)`
        linewidth : int
            linewidth of profile in pixels
        order : int
            order of interpolation between data points
        Returns
        -------
        array:
            length and height data of profile
        array:
            positions of profile to show the profile position in the afm image
        """
        x_size_facor = self._x_size/max(self.x)
        y_size_facor = self._y_size/max(self.y)
        x0, y0 = src
        x1, y1 = dst
        vec = np.subtract(dst,src)
        neg = (np.array([-1*vec[1], vec[0]])/np.linalg.norm(np.array([-1*vec[1],vec[0]])))*linewidth*0.5
        pos = -neg
        line = [np.add(src, neg), np.add(src, pos), np.add(dst, pos), np.add(dst, neg), np.add(src, neg)]
        length = np.linalg.norm(np.array([vec[0]*x_size_facor, vec[1]*y_size_facor]))
        profile = profile_line(np.transpose(self.z), (x0, y0), (x1,y1), linewidth=linewidth, order=order)
        profile_length = np.linspace(0, length, num=len(profile))
        return [profile_length, profile], np.transpose(line)
