from floodsystem.geo import *

def test_stations_by_distance():
    for i in range(len(stations_by_distance) - 1):
        assert stations_by_distance[i][1] < stations_by_distance[i+1][1]


