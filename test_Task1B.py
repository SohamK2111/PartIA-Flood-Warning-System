from floodsystem.geo import *

def test_stations_by_distance():
    for i in stations_by_distance(stations, (52.2053, 0.1218)):
        assert i[1] <= i[1]
