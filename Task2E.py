from pip import main
from floodsystem.datafetcher import *
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
import datetime
import matplotlib.pyplot as plt
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    dt = 10
    for i in stations_highest_rel_level(stations, 5):
        dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(i, dates, levels)


if __name__ == "__main__":
    run()

