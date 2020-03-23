#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import argparse

def search_data_start(file, identifier):
    search = open(file)
    i = 1
    for line in search:
        if identifier in line:
            search.close()
            return i + 1
        i += 1

def load_squid_data(file):
    return np.loadtxt(fname=file, skiprows=search_data_start(file, "[Data]"), delimiter=",", usecols = (2,3,4), unpack=True)



def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Plot SQUID measurements.')
    parser.add_argument('-f', '--files', type=str, nargs='+', help='Folder')
    parser.add_argument('-t', '--temperature', action='store_true', help='Temperature curves.')
    parser.add_argument('-it', '--inverse-temperature', action='store_true', help='Inverse temperature curves.')
    parser.add_argument('-m', '--magnet', action='store_true', help='m(H) curves.')
    parser.add_argument('-s', '--suszeptibility', action='store_true', help='Plot suszeptibility.')
    parser.add_argument('-sb', '--substract-background', action='store_true', help='Substract background.')
    parser.add_argument('-g', '--gradient', action='store_true', help='Plot gradient.')
    parser.add_argument('-lt', '--legend-top', action='store_true', help='Legend above plot.')
    args = parser.parse_args()

    plt.style.use('heusler_plotting')
    fig = plt.figure()

    measurements = []
    for file in args.files:
        loaded_data = load_squid_data(file)
        label = file.split('/')[-1].split('.')[0]
        if args.suszeptibility:
            loaded_data[2] = loaded_data[2]/loaded_data[0]
        if args.substract_background:
            if args.temperature or args.inverse_temperature:
                loaded_data[2] = loaded_data[2]-min(loaded_data[2])
            elif args.magnet:
                fit = np.poly1d(np.polyfit(loaded_data[0][5:], loaded_data[2][5:], 1))
                loaded_data[2] = loaded_data[2] - fit(loaded_data[0])
                loaded_data[2] = loaded_data[2] + np.max(loaded_data[2]/2)
        if args.gradient:
            loaded_data[2] = np.gradient(loaded_data[2])
        measurements.append({"label": label,"data": loaded_data})
        print('Loaded', label)

    for data in measurements:
        if args.temperature:
            plt.plot(data["data"][1], data["data"][2], marker='o', linestyle='-', label=data["label"])
        if args.inverse_temperature:
            plt.plot(data["data"][1], 1/data["data"][2], marker='o', linestyle='-', label=data["label"])
        if args.magnet:
            plt.plot(data["data"][0], data["data"][2], marker='o', linestyle='-', label=data["label"])

    if args.temperature or args.inverse_temperature:
        plt.xlabel('Temperature (K)')
    elif args.magnet:
        plt.xlabel('Field (Oe)')

    ylabel = ''
    if args.inverse_temperature:
        ylabel += 'Inverse '

    if args.suszeptibility:
        ylabel += 'Suszeptibility (emu/Oe)'
    else:
        ylabel += 'Long moment (emu)'

    if args.substract_background:
        ylabel += ' (SB)'

    plt.ylabel(ylabel)

    if args.legend_top:
        plt.legend(bbox_to_anchor=(0,1.08,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=1)
    else:
        plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
