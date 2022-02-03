from logging import raiseExceptions
from floodsystem.geo import *
from floodsystem.station import MonitoringStation
from Task1D import *

def test_rivers_with_station():
    
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

    for station in stations:
        assert station.river in d
    
        if station.river not in d:
            raise Exception("Error: List of unique rivers not complete")

def test_stations_by_river():
    assert type(r_dict) == dict