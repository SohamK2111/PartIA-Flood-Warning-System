import matplotlib
from matplotlib import pyplot 
import numpy as np
import matplotlib.pyplot as plt
#from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_measure_levels
from datetime import datetime, timedelta



def plot_water_level_with_fit(station, dates, levels, p):

    #This function, given the station, the list of dates, the list of water levels, and the polynomial degree, 
    #returns plots of the typical range, the water level over the past 2 days, and the least-squares fit all on the same graph.

    fetch_latest_water_level_data(station)    
    float_dates = matplotlib.dates.date2num(dates)
    p_coeff= np.polyfit(float_dates - float_dates[0], levels, p)
    poly1 = np.poly1d(p_coeff)
    plt.plot(float_dates, levels, '.', label = "Measured Data")
    plt.legend()
    x1 = np.linspace(float_dates[0], float_dates[-1], 60)
    plt.plot(x1, poly1(x1 - float_dates[0]), label = "Least Squares Regression")
    plt.legend()
    b = []
    for k in x1:
        b.append(station.typical_range[0])
    plt.plot(x1, b, label = "Typical Range Minimum")
    plt.legend()
    d = []
    for j in x1:
        d.append(station.typical_range[1])
    plt.plot(x1, d, label = "Typical Range Maximum")
    plt.legend()
    plt.title(station.name)
    plt.show()



def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()  
    plt.show()

