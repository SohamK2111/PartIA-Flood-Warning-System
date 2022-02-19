import matplotlib
from matplotlib import pyplot 
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_measure_levels


def plot_water_level_with_fit(station, dates, levels, p):
    fetch_latest_water_level_data(station)    
    float_dates = matplotlib.dates.date2num(dates)
    p_coeff= np.polyfit(float_dates - float_dates[0], levels, p)
    poly1 = np.poly1d(p_coeff)
    plt.plot(float_dates, levels, '.')
    x1 = np.linspace(float_dates[0], float_dates[-1], 60)
    plt.plot(x1, poly1(x1 - float_dates[0]))
    plt.show()
