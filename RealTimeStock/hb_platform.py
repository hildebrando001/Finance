import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import GridSpec # split screen into grids
import matplotlib.ticker as mticker
import datetime
import math


fig = plt.figure()
fig.patch.set_facecolor('#121416')
gs  = fig.add_gridspec(6,6) # Screen divided into 6x6 frames
ax1 = fig.add_subplot(gs[0:4, 0:4])
ax2 = fig.add_subplot(gs[0, 4:6])
ax3 = fig.add_subplot(gs[1, 4:6])
ax4 = fig.add_subplot(gs[2, 4:6])
ax5 = fig.add_subplot(gs[3, 4:6])
ax6 = fig.add_subplot(gs[4, 4:6])
ax7 = fig.add_subplot(gs[5, 4:6])
ax8 = fig.add_subplot(gs[4, 0:4])
ax9 = fig.add_subplot(gs[5, 0:4])

Stock = ['BRK-B', 'PYPL', 'TWTR', 'AAPL', 'AMZN', 'MSFT', 'FB']


plt.show()