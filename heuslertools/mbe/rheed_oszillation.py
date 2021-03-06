import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as patches
import os
import warnings
from scipy.interpolate import interp1d
import time
warnings.filterwarnings("ignore", category=FutureWarning)

def get_image_intensity(image):
    intensity = 0
    for row in image:
        for pixel in row:
            intensity += pixel
    return intensity

def get_roi_image(filepath, roi):
    image = plt.imread(filepath)
    return image[roi[1][0]:roi[1][1], roi[0][0]:roi[0][1]]

def get_folder_intensities(folder, roi, extension=".tif", show_images=False, bg_roi=None):
    files = os.listdir(folder)
    values = []
    bg_pixels = 0
    bg_int = 1
    sps_pixels = (roi[0][1]-roi[0][0])*(roi[1][1]-roi[1][0])
    if bg_roi is not None:
        bg_pixels = (bg_roi[0][1]-bg_roi[0][0])*(bg_roi[1][1]-bg_roi[1][0])
    i=0
    length = len(files)
    for file in files:
        if file.endswith(extension):
            if show_images:
                show_image_with_roi(os.path.join(folder,file), roi, pause=True)
            sps_int = get_image_intensity(get_roi_image(os.path.join(folder,file), roi))
            if bg_roi is not None:
                sps_int = sps_int/sps_pixels
                bg_int = get_image_intensity(get_roi_image(os.path.join(folder,file), bg_roi))/bg_pixels
            values.append([int(os.path.splitext(file)[0].split('_')[-1])/1000, sps_int, bg_int])
        i += 1
        print("Processed File " + str(i) + "/" + str(length))
    values.sort()
    bg_int_start = values[0][2]
    return [val[0] for val in values], [val[1]*(bg_int_start/val[2]) for val in values]

def show_image_with_roi(filepath, roi, pause=False):
    im = plt.imread(filepath)
    im_roi = get_roi_image(filepath, roi)
    ax = plt.subplot(121)
    plt.imshow(im, interpolation="none", cmap='gray')
    rect = patches.Rectangle((roi_x[0],roi_y[0]),roi_x[1]-roi_x[0],roi_y[1]-roi_y[0],linewidth=1,edgecolor='r',facecolor='none')
    ax.add_patch(rect)
    ax = plt.subplot(122)
    plt.imshow(im_roi, interpolation="none", cmap='gray')
    if pause:
        plt.pause(0.01)
    else:
        plt.show()

if __name__ == "__main__":
    FOLDER = "/home/luke/Documents/RecordTest9/RHEED/record/"

    roi_x = [610, 650]
    roi_y = [315, 355]

    X, Y = get_folder_intensities(FOLDER, [roi_x, roi_y], show_images=False)
    interp = interp1d(X,Y)
    plt.subplot(211)
    plt.plot(X, Y, 'o')
    x = np.linspace(0.1, 19.0, 10000)
    plt.plot(x, interp(x))

    plt.subplot(212)

    sp = np.fft.rfft(interp(x))
    freq = np.fft.rfftfreq(x.shape[-1])
    plt.plot(freq, sp.real, freq, sp.imag)
    plt.tight_layout()



    plt.show()
