from floodsystem.geo import *

def test_stations_by_distance():
    for i in range(len(stations_and_distance) - 1):
        assert stations_and_distance[i][1] < stations_and_distance[i+1][1]