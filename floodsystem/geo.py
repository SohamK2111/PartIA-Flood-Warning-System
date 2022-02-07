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

   """This function, given a list of staiton objects and a coordinate p, returns a list of (station, distance) tuples, 
   where "distance" is the distance of the station from the coordinate p. This list is also sorted in order of distance."""


def stations_within_radius(stations, centre, r):

   """This function, given a list of staiton objects and a coordinate centre, returns a list of station names that are within 
   the radius r"""

   stations_in_radius = []

   for station in stations:
        d = haversine(centre, station.coord)
        if d < r or d == r:
            stations_in_radius.append(station)

   list_of_names = []
   for station in stations_in_radius:
        list_of_names.append(station.name)
    
   print(sorted(list_of_names))
   sorted_list_of_names = sorted(list_of_names)
   return sorted_list_of_names


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

   