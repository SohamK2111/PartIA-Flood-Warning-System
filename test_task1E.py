from floodsystem.geo import *
from logging import raiseExceptions

def test_rivers_by_station_number():

    stations = build_station_list()

    rivers = []
    for station in stations:
        if station.river not in rivers:
            rivers.append(station.river)


    if len(rivers) != len(set(rivers)):
        raise Exception("ERROR - List of rivers is not unique")


test_rivers_by_station_number()

