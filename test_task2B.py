from floodsystem.stationdata import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list

stations = build_station_list()
def latest_water_level_fraction_test(stations):
    a = stations_level_over_threshold(stations, 0.8)
    for i in range(len(a)-1):
        assert a[i][1] > a[i+1][1]

latest_water_level_fraction_test(stations)