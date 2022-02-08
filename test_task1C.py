from floodsystem.geo import *
from logging import raiseExceptions

def test_stations_within_radius():
    stations = build_station_list()
    
    """Test that there are no stations returned when radius is 0"""
    test_set = stations_within_radius(stations, (51.509865,-0.118092), 0)
    assert len(test_set) == 0

    """Test that all stations are included in list when radius is very large"""
    total_number_of_stations = len(stations)
    test_set2 = stations_within_radius(stations, (51.509865,-0.118092), 15000)
    assert total_number_of_stations == len(test_set2)

    """Test that haversine is corrrectly calculating distance between coordinate and stations using specific examples"""
    #distance between two arbitrary coordinates (stated below) is 185km (externally caculated and rounded)
    test_distance = round(haversine((50.8225, 0.1372),(52.39572, 0.98942)))
    if test_distance != 185:
        raise Exception("Haversine function is not working correctly")

test_stations_within_radius()

