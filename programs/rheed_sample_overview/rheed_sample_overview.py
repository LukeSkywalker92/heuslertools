import os
import configparser
from datetime import datetime
import numpy as np
import csv
import matplotlib as mpl
import matplotlib.pylab as plt
from heuslertools.mbe.rheed import RHEEDimage
from heuslertools.plotting.mpl_helpers import set_size
from matplotlib.backends.backend_pdf import PdfPages

SAMPLE_FOLDER = '/home/luke/system02/heusler/Samples'
SAMPLE_FROM = 'H1301'
SAMPLE_TO = 'H1305'
DIRECTIONS = ['110', '1-10', '100', '010']
ROI = (200, 500, 1000, 900)
aspect = ((ROI[3]-ROI[1])/(ROI[2]-ROI[0]))

pp = PdfPages('RHEED_'+ SAMPLE_FROM + '-' + SAMPLE_TO +'.pdf')

folders = os.listdir(SAMPLE_FOLDER)
sample_folders = []
for folder in folders:
    if folder.startswith('H'):
        if int(SAMPLE_FROM[1:]) <= int(folder[1:]) <= int(SAMPLE_TO[1:]):
            sample_folders.append(folder)

sample_folders.sort()
rheed_folders = [os.path.join(SAMPLE_FOLDER, sample_folder, 'RHEED') for sample_folder in sample_folders]


for sample in sample_folders:
    growth = configparser.ConfigParser()
    growth.read(os.path.join(SAMPLE_FOLDER, sample, 'Growth', 'growth.ini'))
    rheed_folder = os.path.join(SAMPLE_FOLDER, sample, 'RHEED')
    rheed_images = {dir:os.path.join(rheed_folder, dir, 'hdr', os.listdir(os.path.join(rheed_folder, dir, 'hdr'))[-1]) for dir in DIRECTIONS}

    fig = plt.figure(figsize=set_size(30, cm=True, ratio=aspect/len(DIRECTIONS)+0.1), constrained_layout=True)
    axes = fig.subplots(1, len(DIRECTIONS))
    fig.suptitle(sample + '\n'
                 'Cu Tip: ' + str(int(round(float(growth['Temperatures']['CuTip']), 0))) +
                 '  Cu Base: ' + str(int(round(float(growth['Temperatures']['CuBase']), 0))) +
                 '  Mn: ' + str(int(round(float(growth['Temperatures']['Mn']), 0))) +
                 '  Sb: ' + growth['Temperatures']['Sb'])
    i = 0
    for dir in rheed_images:
        print(rheed_images[dir])
        image = RHEEDimage(rheed_images[dir])
        image.crop(ROI)
        ax = axes[i]
        ax.imshow(image.image, cmap='viridis')
        ax.set_title(dir)
        ax.set_xticks([])
        ax.set_yticks([])

        i += 1
    plt.savefig(pp, format='pdf')

pp.close()
