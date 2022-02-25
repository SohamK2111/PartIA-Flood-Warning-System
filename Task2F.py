from floodsystem.datafetcher import *
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
import datetime
import matplotlib.pyplot as plt

def run():
    
    stations = build_station_list()
    list_of_levels = []
    update_water_levels(stations)
    for station in stations:
        if station.latest_level is None:
            pass
        elif station.typical_range is None:
            pass
        else:
            list_of_levels.append((station, station.relative_water_level()))
            #print(station.latest_level, station.relative_water_level())
    #print(list_of_levels)

    sorted_levels = sorted_by_key(list_of_levels, 1)
    five_greatest_levels = sorted_levels[-5:]
    #print(five_greatest_levels)

    for i in five_greatest_levels:
        dt = 2
        dates, levels = fetch_measure_levels(i[0].measure_id, dt=datetime.timedelta(days=dt))
        #print(i[0].typical_range)
        plot_water_level_with_fit(i[0], dates, levels, 4)
        #print(levels)

if __name__ == "__main__":
    run()



