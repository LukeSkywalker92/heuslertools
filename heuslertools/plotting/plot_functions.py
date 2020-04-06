import numpy as np
from operator import sub

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
