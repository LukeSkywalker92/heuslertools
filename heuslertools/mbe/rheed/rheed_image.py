from PIL import Image
import PIL.ImageOps
from skimage.measure import profile_line
import numpy as np

class RHEEDimage(object):
    """
    Object representing a RHEED image.
    You can import it with `from heuslertools.mbe.rheed import RHEEDimage`

    Parameters
    ----------
    path : str
        Path of the RHEED image
    """
    def __init__(self, path):
        self.raw_image = Image.open(path)
        """RAW image. This won't be affected by any operations."""
        self.image = None
        """Intensity data of the RHEED image. This is affected by operations."""
        if self.raw_image.mode == 'RGB':
            self.image = self.raw_image.convert('L')
        else:
            self.image = self.raw_image

    def crop(self, roi):
        """
        Crop the image to a region of interest.

        Parameters
        ----------
        roi : tuple
            Region of interest to crop the image to `(x0, y0, x1, y1)`
        """
        self.image = self.image.crop(roi)

    def invert(self):
        """
        Invert the image intensities.
        """
        self.image = PIL.ImageOps.invert(self.image)

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
            intensities along profile
        """
        profile = profile_line(np.transpose(np.array(self.image)), src, dst, linewidth=linewidth, order=order)
        len(profile)
        return profile
