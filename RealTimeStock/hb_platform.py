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

# Make nice plot
def figure_design(ax):
    ax.set_facecolor('#091217')
    ax.tick_params(axis='both', labelsize=14, colors='white')
    ax.ticklabel_format(useOffset=False)
    ax.spines['bootom'].set_color('#808080')
    ax.spines['top'].set_color('#808080')
    ax.spines['left'].set_color('#808080')
    ax.spines['right'].set_color('#808080')
    

# Convert strings to numbers
def string_to_number(df, column):
    if isinstance(df.iloc[0, df.columns.get_loc(column)], str):
        df[column] = df[column].str.replace(',', ' ')
        df[column] = df[column].astype(float)
    return df

# Read data (Open, High, Low, Cost) function
def read_data_ohlc(filename, stock_code, usecols):
    df = pd.read_csv(filename, header=None, usecols=usecols,
                    names=['time', stock_code, 'change', 'volume', 'pattern','target'],
                    index_col = 'time', parse_dates['time'])

    index_with_nan = df.index[df.isnull().any(axis=1)]
    df.drop(index_with_nan, 0, inplace=True) # The 'zero' here means the rows that is going to drop

    df.index = pd.DatetimeIndex(df.index)

    # Convert these three columns into a floating number type
    df = string_to_number(df, stock_code)
    df = string_to_number(df, 'volume')
    df = string_to_number(df, 'target')

    latest_info   = df.iloc[-1, :] # last line, all columns
    latest_price  = str(latest_info.iloc[0])
    latest_change = str(latest_info.iloc[1])

    df_vol = df['volume'].resample('1Min').mean() # resampling the data

    # Move from generic df to Open, High, Low, Cost df
    data = df[stock_code].resample('1Min').ohlc() #
    data['time'] = data.index

    data['time'] = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S')

    data['MA5']  = data['close'].rolling(5).mean()
    data['MA10'] = data['close'].rolling(10).mean()
    data['MA20'] = data['close'].rolling(20).mean()

    data['volume_diff'] = df_vol.diff()
    data[data['volume_diff']<0]=None

    index_with_nan = data.index[data.isnull().any(axis=1)]
    data.drop(index_with_nan, 0, inplace=True)
    data.reset_index(drop=True, inplace=True)

    reteurn data, latest_price, latest_change, df['pattern'][-1], df['target'][-1], df['volume'][-1]

