import matplotlib
from shutil import copyfile
import os
import subprocess

HEUSLER_MPL_STYLE = '../../heuslertools/plotting/heusler.mplstyle'

copyfile(HEUSLER_MPL_STYLE, os.path.join(matplotlib.get_configdir(),'stylelib', 'heusler.mplstyle'))
process = subprocess.Popen(['pip', 'install', 'pyqtchart'],
         stdout=subprocess.PIPE,
         stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
