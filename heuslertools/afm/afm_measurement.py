import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from skimage.measure import profile_line

class AFMMeasurement(object):
    """
    Object representing a afm measurement

    You can import it with

    ```from heuslertools.afm import AFMMeasurement```
    """

    def __init__(self, file, size):
        self.file = file
        """Path of the data file"""
        self.x_size, self.y_size = size
        self.load_data()

    def load_data(self):
        data = np.loadtxt(self.file)
        self.x = []
        self.y = []
        for i in range(1, len(data[0])+1):
            self.x.append(i)
        for i in range(1, len(data)+1):
            self.y.append(i)
        self.z=(data-np.min(data))*1e10

    def rms_roughness(self):
        z = []
        for i in self.z:
            for j in i:
                z.append(j)
        return(np.std(z))

    def profile(self, src, dst, linewidth=1, order=3):
        x_size_facor = self.x_size/max(self.x)
        y_size_facor = self.y_size/max(self.y)
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
