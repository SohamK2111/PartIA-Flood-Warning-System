from logging import raiseExceptions
from floodsystem.geo import *
from floodsystem.geo import rivers_with_station

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
    
    





    #assert that each river in the ordered set list has a monitoring station