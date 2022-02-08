from floodsystem.geo import *
from logging import raiseExceptions

def test_stations_within_radius():
    stations = build_station_list()
    
    #assert and raise exceptions
    test_set = stations_within_radius(stations, (51.509865,-0.118092), 0)
    assert len(test_set) == 0

    #assert that total number of stations is equal to stations in a v large radius
    total_number_of_stations = len(stations)
    test_set2 = stations_within_radius(stations, (51.509865,-0.118092), 15000)
    assert total_number_of_stations == len(test_set2)

test_stations_within_radius()


