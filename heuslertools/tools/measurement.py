import numpy as np
from numpy.lib.recfunctions import append_fields
import matplotlib.pyplot as plt
from tabulate import tabulate
from heuslertools.tools.data_handling import load_data
from scipy.interpolate import interp1d


class Measurement(object):
    """Object representing a Measurement

    Parameters
    ----------
    file : str
        path of file
    identifier : str
        identifier for data start
    delimiter : str, optional
        delimiter of data, by default `None`
    """


    def __init__(self, file, identifier, delimiter=None, start_row=0, end_row=None, names=True, encoding=None):
        self.file = file
        """Path of the data file"""
        self._identifier = identifier
        self._delimiter = delimiter
        self._start_row = start_row
        self._end_row = end_row
        self._names = names
        self._encoding = encoding
        self.data = self._load_data()
        """Numpy ndarray containing the data."""
        self.names = {}
        """Dict containing the names, short names and units of the data columns"""
        self._generate_names()

    def _load_data(self):
        return load_data(self.file, self._identifier, delimiter=self._delimiter,
                         start_row=self._start_row, end_row=self._end_row,
                         names=self._names, encoding=self._encoding)

    def _generate_names(self):
        for name in self.data.dtype.names:
            self.names[name] = {"short_name": ' '.join(
                name.split("_")[0:-1]), "unit": name.split("_")[-1]}

    def add_data_column(self, name, data):
        """Add column to data.

        Parameters
        ----------
        name : str
            name of data column, format: `name_name_unit`
        data : array
            data
        """
        self.data = append_fields(self.data, name, data, np.float)
        self._generate_names()

    def append_measurement(self, file, identifier, start_row=0, end_row=None):
        """Append data from another file.

        Parameters
        ----------
        file : str
            path of file to append
        identifier : str
            identifier for data start
        """
        self.data = np.append(self.data, load_data(self.file, self._identifier, delimiter=self._delimiter, start_row=start_row, end_row=end_row, names=self._names, encoding=self._encoding))

    def plot(self, x, y, *args, show=True, label=True, **kwargs):
        """Plot data

        Parameters
        ----------
        x : str
            name of x data column
        y : str
            name of y data column
        show : bool, optional
            if `true` the plot will be shown immediately, by default `true`
        """
        if show:
            plt.figure()
        plt.plot(self.data[x], self.data[y], *args, **kwargs)
        if label:
            plt.xlabel(self.get_axis_label(x))
            plt.ylabel(self.get_axis_label(y))
        if show:
            plt.show()

    def get_unit(self, name):
        """
        Get unit of data column by column name.

        Arguments:
            name (str): Column name

        Returns:
            str: unit of data column
        """
        return self.names[name]["unit"]

    def get_short_name(self, name):
        """Get short name of data column by column name.

        Parameters
        ----------
        name : str
            Column name

        Returns
        -------
        str
            short name of data cloumn
        """

        return self.names[name]["short_name"]

    def get_axis_label(self, name):
        """Get axis label of data column by column name.

        Parameters
        ----------
        name : str
            Column name

        Returns
        -------
        str
            axis label of data cloumn
        """
        return self.get_short_name(name) + ' (' + self.get_unit(name) + ')'

    def interpolation(self, x, y, kind='linear'):
        """Interpolate data

        Parameters
        ----------
        x : str
            name of x data column
        y : str
            name of y data column
        kind : str, optional
            kind of interpolation (see scipy.interpolate.interp1d), by default
            'linear'

        Returns
        -------
        callable
            call the returned callable with an x value to evaluate the
            interpolation at this position
        """
        return interp1d(self.data[x], self.data[y], bounds_error=False, kind=kind)

    def print_names(self):
        """
        Print table of availiable data columns that can be used to access the data.
        """
        headers = ["name", "short_name", "unit"]
        table = [[name, self.names[name]["short_name"], self.names[name]["unit"]]
                 for name in self.names]
        print("Availiable names:")
        print(tabulate(table, headers))

    def substract_linear_baseline(self, x, y, x_min, x_max, mean=False):
        """Substract linear baseline from x-y-data and add substracted data
        column to data.

        Parameters
        ----------
        x : str
            name of x data column
        y : str
            name of y data column
        x_min : float
            lower bound of x range, where lienar baseline should be extracted from
        x_min : float
            upper bound of x range, where lienar baseline should be extracted from
        mean: bool, optional
            if `true` the substracted data will be symmetrised to x-axis
        """
        data_name = y.split('_')
        data_name.insert(-1, 'LinearBaselineSubstracted')
        data_name = "_".join(data_name)
        indices = np.where(np.logical_and(self.data[x] >= x_min, self.data[x] <= x_max))
        fit = np.poly1d(np.polyfit(self.data[x][indices], self.data[y][indices], 1))
        data = self.data[y]-fit(self.data[x])
        if mean:
            data = data - np.mean(data)
        self.add_data_column(data_name, data)
