from nav import Database
from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

# Opening time of the slope
OPENING_TIME = 8
# window size of moving average
win_size_short = 4
win_size_long = 10


def get_current_time(opening_time=OPENING_TIME) -> int:
    """Gets the current time; converts and sums hours to minutes
    
    :param opening_time: opening time of the slope
    
    :return: Current time in minutes
    """ 
    t = time.localtime()
    current_time = time.strftime("%H%M", t)
    hours = int(current_time[:2])
    minutes = int(current_time[2:4])
    
    ctime = (hours*60*60 + minutes*60 - opening_time*60*60)
    return ctime


def line(ctime):
    """
    Generates sample line for drehzeuge
    """
    T = int(ctime/0.02)
    global x_axis
    x_axis = np.linspace(0, T)
    # generating actually possible number
    random_bias = random.randint(0, 6)
     
    y = (
        np.abs((
            np.sin(4*x_axis)
            ) - ((7/4)*random_bias)*np.sin(x_axis))
        )
        
    return np.array(y)
    

def moving_average(series: np.array, window_size: int) -> List:
    """
    Calculates the moving average based on the window_size
    
    :param series: (np.array) Series of numbers
    :param window_size: (int) Size of window
    
    :return: List of average numbers
    """
    
    # Initialization
    series = pd.Series(series)
    windows = series.rolling(window_size)
    
    # Averaging
    average_that_moves = windows.mean()
    moving_average_list = average_that_moves.tolist()
    
    # Removing invalids
    final = moving_average_list[window_size - 1:]
    
    return final


## Creating database
#db = Database('database.db')
#db.create_table("drehzeug_data", "SUNLINER")
debug = 0

ctime = get_current_time()
print(ctime)
trend = line(ctime= ctime)
ma_short = moving_average(trend, window_size= win_size_short)
ma_long = moving_average(trend, window_size=win_size_long)

#while debug < 20:
#    time.sleep(0)
#    ctime = get_current_time()
#    
#    debug += 1
#    time.sleep(1)
#

# FIXME: Nothing :)
# TODO: plotting through eachother
# TODO: Code merging

plt.figure()
ax = plt.gca()
ax.set_xscale(OPENING_TIME, ctime)
plt.plot(x_axis[:-win_size_short+1], ma_short, c='tab:red')
plt.plot(x_axis[:-win_size_long+1], ma_long, c= 'tab:blue')
plt.show()

#db.close_connection()
exit()

