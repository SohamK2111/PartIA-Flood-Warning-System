# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
#from utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
import math

from floodsystem.utils import sorted_by_key


stations = build_station_list()

stations_and_distance = []

def stations_by_distance(stations, p):
    for station in stations:
        stations_and_distance.append((station, haversine(p, station.coord)))
    return sorted_by_key(stations_and_distance, 1)



def stations_within_radius(stations, centre, r):
    stations_in_radius = []

    for station in stations:
        d = haversine(centre, station.coord)
        if d < r or d == r:
            stations_in_radius.append(station)

    list_of_names = []
    for station in stations_in_radius:
        list_of_names.append(station.name)
    
    print(sorted(list_of_names))


def rivers_by_station_number(stations, N):
    #create list of all river names
    rivers = []
    
    for station in stations:
        if station.river not in rivers:
            rivers.append(station.river)
    
    list_of_tuples = []

    for river in rivers:
        counter = 0
        for station in stations:
            if station.river == river:
                counter += 1 
        list_of_tuples.append((river, counter))
    
    sorted_list = sorted_by_key(list_of_tuples, 1, True)

    #TODO - in the case that there are more rivers with same number of stations, print them too.
    #number of items in list excluding first N
    x = len(sorted_list) - N
    counter2 = 0

    for item in sorted_list[-x:]:
        if item[1] == sorted_list[N][1]:
            counter2 += 1
        else:
            break
    
    print(sorted_list[:N+counter2])


