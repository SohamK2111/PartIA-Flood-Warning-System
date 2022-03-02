
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_latest_water_level_data
import matplotlib
import numpy as np

stations = build_station_list()

def stations_level_over_threshold(stations, tol):
    stationsovertol_relativelevel = []
    update_water_levels(stations)
    for station in stations:
        if MonitoringStation.relative_water_level(station) == None:
            pass
        elif MonitoringStation.relative_water_level(station) > tol:
            stationsovertol_relativelevel.append((station.name, MonitoringStation.relative_water_level(station)))
    ordered_list = sorted_by_key(stationsovertol_relativelevel, 1, reverse = True)
    return ordered_list



def stations_highest_rel_level(stations, N):
    stations_highest_rellev = []
    for station in stations:
        if MonitoringStation.relative_water_level(station) == None:
            pass
        else:
            stations_highest_rellev.append((station, MonitoringStation.relative_water_level(station)))
    
    sortedlist = sorted_by_key(stations_highest_rellev, 1, reverse = True)
    #x is a list of the top N stations with highest relative water level
    x = sortedlist[:N]
    y = []
    # this loop creates a list of the stations with highest water level
    for i in x:
        y.append(i[0])
    
    return y

def warning_system(station, dates, levels, p):
    #find out if water level is rising or falling (derivative of relative water level)
    #if derivative is positive then water level is rising - send a warning (severity depends on how large derivative is)

    fetch_latest_water_level_data(station)    
    float_dates = matplotlib.dates.date2num(dates)
    p_coeff= np.polyfit(float_dates - float_dates[0], levels, p)
    poly1 = np.poly1d(p_coeff)

    x1 = np.linspace(float_dates[0], float_dates[-1], 60)

    deriv_of_poly = np.polyder(poly1)
    #print('derivative of polyfit')
    #print(deriv_of_poly(x1[0]- float_dates[0]))
    derivative = deriv_of_poly(x1[0]- float_dates[0])

    return derivative
  








    

