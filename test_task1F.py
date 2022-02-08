from unittest.mock import Mock
from floodsystem.geo import *
from floodsystem.station import *
from logging import raiseExceptions


def test_inconsistent_typical_range_systems():
    stations = build_station_list()

    incon_stations = inconsistent_typical_range_stations(stations)

    """Check that the types are correct"""
    assert type(incon_stations) == list
    assert type(incon_stations[0]) == MonitoringStation

    """Make a list of stations where 2 are inconsistent"""
    test_list_of_stations = [MonitoringStation(None, None, None, None, (1,4), None, None),
    MonitoringStation(None, None, None, None, (1,4), None, None),
    MonitoringStation(None, None, None, None, (1,4), None, None),
    MonitoringStation(None, None, None, None, (10,2), None, None),
    MonitoringStation(None, None, None, None, (10,2), None, None)]
    assert len(inconsistent_typical_range_stations(test_list_of_stations)) == 2

test_inconsistent_typical_range_systems()



