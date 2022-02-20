from sympy import N
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key


stations = build_station_list()

def stations_level_over_threshold(stations, tol):
    stationsovertol_relativelevel = []
    update_water_levels(stations)
    for station in stations:
        if station in inconsistent_typical_range_stations(stations):
            if station.latest_level == None:
                pass
            elif station.latest_level > tol:
                stationsovertol_relativelevel.append((station.name, station.latest_level))
    ordered_list = sorted_by_key(stationsovertol_relativelevel, 1, reverse = True)
    return ordered_list
#print(stations_level_over_threshold(stations, 0.8))


def stations_highest_rel_level(stations, N):
    stations_highest_rellev = []
    update_water_levels(stations)
    for station in stations:
        if MonitoringStation.relative_water_level(station) == None:
            pass
        else:
            stations_highest_rellev.append((station.name, MonitoringStation.relative_water_level(station)))
    
    sortedlist = sorted_by_key(stations_highest_rellev, 1, reverse = True)
    
    #x is a list of the top N stations with highest relative water level
    x = sortedlist[:N]
    y = []
    # this loop creates a list of the names of the stations with highest water level
    for i in x:
        y.append(i[0])
        
    return y


