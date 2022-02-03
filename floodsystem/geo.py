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
        stations_and_distance.append((station.name, haversine(p, station.coord)))
    return sorted_by_key(stations_and_distance, 1)

def rivers_with_station(stations):
   a = []
   rivers = []
   for station in stations:
      rivers.append(station.river)
   for river in rivers:
      if river in stations:
         a.append(river)

   b = set(rivers)
   c = list(b)
   d = sorted(c)

   print(str(len(d)) + " stations. First 10 - " + str(d[:10]))

#rivers_with_station(stations)

def stations_by_river(a = "River Aire", b = "River Cam", c = "River Thames"):
   list_a = []
   list_b = []
   list_c = []
   for station in stations:
      if a == station.river:
         list_a.append(station.name)
      elif b == station.river:
         list_b.append(station.name)
      elif c ==station.river:
         list_c.append(station.name)
   print("\n \'River Aire\'")
   print(str(sorted(list_a)))
   print("\'River Cam\'")
   print(str(sorted(list_b)))
   print("\'River Thames\'")
   print(str(sorted(list_c)))

#stations_by_river(a = "River Aire", b = "River Cam", c = "River Thames")