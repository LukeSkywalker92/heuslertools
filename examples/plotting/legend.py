import matplotlib.pyplot as plt
import numpy as np

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
for line in ax.lines:
    print(line._label)
    print(line.get_xdata()[-1], line.get_ydata()[-1])
    ax.text(line.get_xdata()[-1]+0.5, line.get_ydata()[-1], line._label, horizontalalignment='left', verticalalignment='center')
plt.show()