import numpy as np
from operator import sub
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter

LABEL_POSITIONS = {
    'top': -1,
    'bottom': 0,
    'left': 0,
    'right': -1
}

def get_aspect(ax):
    fig = ax.figure
    ll, ur = ax.get_position() * fig.get_size_inches()
    width, height = ur - ll
    axes_ratio = height / width
    return axes_ratio

def sub_label(ax, label, position, style=None, color='k', x_factor=1, y_factor=1):
    vertical, horizontal = position.split('_')
    aspect = get_aspect(ax)
    label_string = r''
    if 'sf' in style:
        label_string += r'\sffamily'
    if 'b' in style:
        label_string += r'\textbf'
    label_string += '{' + label + '}'
    ax.text(abs(LABEL_POSITIONS[horizontal]+(0.03*aspect*x_factor)),
            abs(LABEL_POSITIONS[vertical]+(0.03*(1/aspect)*y_factor)),
            label_string,
            horizontalalignment=horizontal, verticalalignment=vertical,
            transform=ax.transAxes, color=color)

def arrows(ax, x, y, n_arrows, offset=0, color='black', size=20, window_length=211, polyorder=3, plot_interpolation=False):
    x0 = min(x)
    x1 = max(x)
    if x[0]>x[-1]:
        x0 = max(x)
        x1 = min(x)
    xx = np.linspace(x0, x1, 10*len(x))
    interpolation = interp1d(x, y)
    yhat = savgol_filter(interpolation(xx), window_length, polyorder)
    interpolation = interp1d(xx, yhat)
    u = interp1d(xx[1:], np.diff(xx))
    v = interp1d(xx[1:], np.diff(interpolation(xx)))
    x_arr = np.linspace(x0, x1, n_arrows+2)
    x_arr = x_arr[1:-1]
    y_arr = interpolation(x_arr)
    u_arr = u(x_arr)
    v_arr = v(x_arr)
    if plot_interpolation:
        ax.plot(xx, interpolation(xx), 'k-')
    for X,Y,dX,dY in zip(x_arr, y_arr, u_arr, v_arr):
        ratio = ax.get_data_ratio()
        dY_bar = dY/ratio
        norm = np.sqrt(dX**2+dY_bar**2)
        y_offset = (dX/norm)*ratio
        x_offset = dY_bar/norm
        norm = np.sqrt(x_offset**2+y_offset**2)
        X = X+((offset*x_offset))
        Y = Y-((offset*y_offset))
        ax.annotate("", xytext=(X,Y),xy=(X+0.001*dX,Y+0.001*dY), 
                    arrowprops=dict(arrowstyle="->", color=color), size = size)

def label_lines(ax)