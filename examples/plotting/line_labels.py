import matplotlib.pyplot as plt
import numpy as np
from heuslertools.plotting.plot_functions import label_lines

def get_label_for_line(line):
    leg = line.axes.get_legend()
    ind = line.axes.get_lines().index(line)
    return leg.texts[ind].get_text()

x = np.linspace(0,10,10)
y = x**2

fig, ax = plt.subplots()
for i in range(5):
    line = plt.plot(x, y+(i*10), label=f'Curve {str(i+1)}')
#plt.legend()
ax.set_xlim(0, 14)
label_lines(x_margin=0.5)
plt.show()