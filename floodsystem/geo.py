# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list


stations = build_station_list()

stations_and_distance = []

def stations_by_distance(stations, p):
    for station in stations:
        stations_and_distance.append((station, haversine(p, station.coord)))
    return sorted_by_key(stations_and_distance, 1)


def task_1B():
   a = stations_by_distance(stations, (52.2053, 0.1218))
   print("The 10 CLOSEST stations are: ")
   for i in range(10):
      print(str(a[i][0].name) + ", " + str(a[i][0].town) + ", " + str(a[i][1]))

   print("\n The 10 FURTHEST stations are: ")
   for i in range(10):
      print(str(a[-i][0].name) + ", " + str(a[-i][0].town) + ", " + str(a[-i][1]))


task_1B()
