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


stations = build_station_list()

stations_and_distance = []

def stations_by_distance(stations, p):
    for station in stations:
        stations_and_distance.append((station, haversine(p, station.coord)))
    return sorted_by_key(stations_and_distance, 1)

print(stations[0])
print("Hi Ella")
print("Hi Soham")


def stations_within_radius(stations, centre, r):
    stations_in_radius = []

    for station in stations:
        d = haversine(centre, station.coord)
        if d < r or d == r:
            stations_in_radius.append(station)

    return stations_in_radius


list_of_names = []
for station in stations_within_radius(stations, (52.2053, 0.1218), 10):
    list_of_names.append(station.name)

print(sorted(list_of_names))