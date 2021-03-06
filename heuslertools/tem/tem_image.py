import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from skimage.measure import profile_line
import os
from matplotlib import ticker
from .ser_reader import serReader
from PIL import Image

class TEMImage(object):
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

    def __init__(self, file):
        self._file = file
        """Path of the data file"""
        self.x = []
        """Data positions in x"""
        self.y = []
        """Data positions in y"""
        self.z = []
        """Height data"""
        self._load_data()

    def _load_data(self):
        data = serReader(self._file)
        self.x = []
        self.y = []
        for i in range(1, len(data['data'][0])+1):
            self.x.append(i)
        for i in range(1, len(data['data'])+1):
            self.y.append(i)
        self.pixel_size_x = data['pixelSizeX']
        self.pixel_size_y = data['pixelSizeY']
        self._x_size = data['pixelSizeX']*len(self.x)
        self._y_size = data['pixelSizeY']*len(self.y)
        self.z = data['data']
        self.image = Image.fromarray(self.z)

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

    def set_xy_ticks(self, ax):
        ax.tick_params(
            axis='both',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            left=False,
            right=False,
            labelbottom=False,
            labelleft=False)
        ax.ticklabel_format(style='plain')

    def set_aspect_ratio(self, ax):
        xleft, xright = ax.get_xlim()
        ybottom, ytop = ax.get_ylim()
        ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*1)

    def show_scale_bar(self, ax, length, label, position, lw=1, color='k', fontsize=8, text_y_offset=0.05):
        left, right = self.x[0], self.x[-1]
        bottom, top = self.y[0], self.y[-1]
        width = right - left
        height = top - bottom
        bar_length = length/(self._x_size/len(self.x))
        x = [position[0]*width+left, position[0]*width+left+bar_length]
        y = [bottom+position[1]*height, bottom+position[1]*height]
        line = ax.plot(x, y, '-', lw=lw, color=color)
        ax.text((x[1]+x[0])/2, y[0]-text_y_offset*len(self.y), label, verticalalignment='top', horizontalalignment='center', color=color, fontsize=fontsize)

    def show_auto_scale_bar(self, ax, position, **kwargs):
        length = float(format(self._x_size/10, '.1g'))
        label = format(self._x_size/10, '.1g') + ' m'
        self.show_scale_bar(ax, length, label, position, **kwargs)

    def show_profile(self, ax, line, box=True, arrow=True, color='k'):
        src = (np.mean(line[0][0:2]), np.mean(line[1][0:2]))
        dst = (np.mean(line[0][2:4]), np.mean(line[1][2:4]))
        if box:
            ax.plot(line[0], line[1], '-', c=color)
        if arrow:
            ax.annotate("",
            xy=src,    # start point
            xycoords='data',
            xytext=dst,    # end point
            textcoords='data',
            arrowprops=dict(
                arrowstyle="<-",
                connectionstyle="arc3",
                color=color,
                ),
            )
