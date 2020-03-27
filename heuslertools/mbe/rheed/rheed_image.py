from PIL import Image
import PIL.ImageOps
from skimage.measure import profile_line
import numpy as np

class RHEEDimage(object):

    def __init__(self, path):
        self.raw_image = Image.open(path)
        if self.raw_image.mode == 'RGB':
            self.image = self.raw_image.convert('L')
        else:
            self.image = self.raw_image

    def crop(self, roi):
        self.image = self.image.crop(roi)

    def invert(self):
        self.image = PIL.ImageOps.invert(self.image)

    def profile(self, src, dst, linewidth=1, order=3):
        profile = profile_line(np.transpose(np.array(self.image)), src, dst, linewidth=linewidth, order=order)
        len(profile)
        return profile
