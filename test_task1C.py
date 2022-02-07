from floodsystem.geo import *
from logging import raiseExceptions

def test_stations_within_radius():
    #assert and raise exceptions
    test_set = stations_within_radius(stations, (51.509865,-0.118092), 0)
    assert len(test_set) == 0

test_stations_within_radius()


