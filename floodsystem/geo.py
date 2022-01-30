# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from utils import sorted_by_key  # noqa
from stationdata import build_station_list
from haversine import haversine, Unit

stations = build_station_list()

stations_and_distance = []

def stations_by_distance(stations, p):
    for station in stations:
        stations_and_distance.append((station, haversine(p, station.coord)))
    return sorted_by_key(stations_and_distance, 1)