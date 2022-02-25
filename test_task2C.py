from floodsystem.stationdata import MonitoringStation
from floodsystem.flood import *

def test_stations_highest_rel_level():
    #create a dummy set
    test_stations = [MonitoringStation(None, None, 'NoneType Test', None, None, None, None),
    MonitoringStation(None, None, 'Filler1', None, (1.1,1.2), None, None),
    MonitoringStation(None, None, 'Lowest', None, (0.025, 1.5), None, None),
    MonitoringStation(None, None, 'Filler2', None, (0.467, 2.38), None, None),
    MonitoringStation(None, None, 'Highest', None, (0.4, 1.68), None, None),
    MonitoringStation(None, None, 'Inconsistent Range Test', None, (3.5, 0.5), None, None)]

    #none, 1, 0.424, 1.847, 2.3, none 
    latest_levels = [3.7, 1.2, 0.65, 4, 3.33, 0.9]

    #assign a latest level to all dummy stations
    for station in test_stations:
        ind = test_stations.index(station)
        station.latest_level = latest_levels[ind]

    
    x = stations_highest_rel_level(test_stations, 6)
    assert len(x) == 4
    assert x[0].name == 'Highest'
    assert x[3].name == 'Lowest'
    for i in x:
        if i.name == 'NoneType Test' or i.name == 'Inconsistent Range Test':
            assert MonitoringStation.relative_water_level(i) == None


test_stations_highest_rel_level()
