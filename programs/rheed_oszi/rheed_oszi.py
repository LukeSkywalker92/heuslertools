import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import RectangleSelector, Button
from matplotlib.backend_tools import ToolBase, ToolToggleBase
from heuslertools.mbe.rheed_oszillation import get_folder_intensities
import os
import argparse


class ROISelect(object):

    def __init__(self, folder, extension=".tif"):
        self.folder = folder
        self.extension = extension

        self.index = 0
        self.images = self.get_images_of_folder()
        self.image = plt.imread(os.path.join(self.folder, self.images[self.index][1]))
        self.figure = plt.figure(figsize=(10, 10), tight_layout=True)

        self.gs = gridspec.GridSpec(2, 2)

        self.main_plot = self.figure.add_subplot(self.gs[0, 0])
        self.roi_plot = self.figure.add_subplot(self.gs[0, 1])
        self.intensity_plot = self.figure.add_subplot(self.gs[1, :])
        self.main_plot.imshow(self.image, interpolation="none", cmap='gray')
        self.roi_plot.imshow(self.image, interpolation="none", cmap='gray')


        self.RS = RectangleSelector(self.main_plot, self.onselect, drawtype='box')
        self.figure.canvas.mpl_connect('key_press_event', self.toggle_selector)

        self.axstart = plt.axes([0.18, 0.55, 0.05, 0.04])
        self.start_button = Button(self.axstart, 'Start')
        self.start_button.on_clicked(self.button_callback)

        self.axnext = plt.axes([0.26, 0.55, 0.05, 0.04])
        self.next_button = Button(self.axnext, '>')
        self.next_button.on_clicked(self.next)

        self.axprev = plt.axes([0.1, 0.55, 0.05, 0.04])
        self.prev_button = Button(self.axprev, '<')
        self.prev_button.on_clicked(self.prev)

        plt.show()

    def toggle_selector(self, event):
        print('Key pressed.')
        if event.key in ['Q', 'q'] and self.RS.active:
            self.toggle_selector.RS.set_active(False)
        if event.key in ['A', 'a'] and not self.RS.active:
            self.RS.set_active(True)

    def onselect(self, eclick, erelease):
        self.roi_plot.set_xlim(eclick.xdata, erelease.xdata)
        self.roi_plot.set_ylim(eclick.ydata, erelease.ydata)
        self.roi = [[int(eclick.xdata), int(erelease.xdata)], [int(eclick.ydata), int(erelease.ydata)]]
        plt.tight_layout()

    def get_images_of_folder(self):
        files = os.listdir(self.folder)
        file_list = []
        for file in files:
            if file.endswith(self.extension):
                file_list.append([int(os.path.splitext(file)[0].split('_')[-1])/1000, file])
        file_list.sort()
        return file_list

    def button_callback(self, event):
        X, Y = get_folder_intensities(self.folder, self.roi)
        self.intensity_plot.plot(X, Y, 'o')
        plt.tight_layout()

    def next(self, event):
        if self.index < (len(self.images) - 1):
            self.index += 1
            self.image = plt.imread(os.path.join(self.folder, self.images[self.index][1]))
            self.main_plot.clear()
            self.roi_plot.clear()
            self.main_plot.imshow(self.image, interpolation="none", cmap='gray')
            self.roi_plot.imshow(self.image, interpolation="none", cmap='gray')
            self.RS = RectangleSelector(self.main_plot, self.onselect, drawtype='box')
            plt.draw()
            plt.tight_layout()

    def prev(self, event):
        if self.index > 0:
            self.index -= 1
            self.image = plt.imread(os.path.join(self.folder, self.images[self.index][1]))
            self.main_plot.clear()
            self.roi_plot.clear()
            self.main_plot.imshow(self.image, interpolation="none", cmap='gray')
            self.roi_plot.imshow(self.image, interpolation="none", cmap='gray')
            self.RS = RectangleSelector(self.main_plot, self.onselect, drawtype='box')
            plt.draw()
            plt.tight_layout()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get RHEED intensities.')
    parser.add_argument('folder', type=str, help='Folder')
    args = parser.parse_args()
    rs = ROISelect(args.folder)
