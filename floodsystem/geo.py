# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
import math
from floodsystem.utils import sorted_by_key


stations = build_station_list()

def stations_by_distance(stations, p):

   """This function, given a list of staiton objects and a coordinate p, returns a list of (station, distance) tuples, 
   where "distance" is the distance of the station from the coordinate p. This list is also sorted in order of distance."""
   
   stations_and_distance = []
   for station in stations:
      stations_and_distance.append((station.name, haversine(p, station.coord)))
   return sorted_by_key(stations_and_distance, 1)

def stations_within_radius(stations, centre, r):

   """This function given a list of station objects and a coordinate centre, returns a list of station names that are 
   within radius r"""

   stations_in_radius = []

   for station in stations:
      d = haversine(centre, station.coord)
      if d < r or d == r:
         stations_in_radius.append(station)
   
   return(stations_in_radius)


def rivers_by_station_number(stations, N):
   """This function creates a list of rivers with the most stations. This list is ordered. It returns the fors N number 
   of stations. It takes in arguments: stations, a list of all the stations in the database, and N, the number of stations 
   to be printed. It returns a list of tuples with the river name and the number of stations."""

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

   x = len(sorted_list) - N
   counter2 = 0

   for item in sorted_list[-x:]:
      if item[1] == sorted_list[N][1]:
         counter2 += 1
      else:
         break
    
   return(sorted_list[:N+counter2])


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

   