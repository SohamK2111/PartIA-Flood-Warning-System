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

def stations_by_distance(stations, p):

   """This function, given a list of staiton objects and a coordinate p, returns a list of (station, distance) tuples, 
   where "distance" is the distance of the station from the coordinate p. This list is also sorted in order of distance."""
   stations_and_distance = []
   for station in stations:
      stations_and_distance.append((station.name, haversine(p, station.coord)))
   return sorted_by_key(stations_and_distance, 1)

def rivers_with_station(stations):
   """This function, given a list of station objects, returns a container with the names of the rivers with a monitoring station. 
      It has one argument, which is a list of stations."""
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

def stations_by_river(stations):

   """This function passes a list of stations, and returns a dictionary whose values 
   are the stations that correspond to a particular river"""
   
   riverdict ={}
   for station in stations:
      if station.river in riverdict:
         riverdict[station.river].append(station.name)
      else:
         riverdict[station.river] = [station.name]
   riverdict = {k:sorted(v) for k,v in riverdict.items()}
   return riverdict 