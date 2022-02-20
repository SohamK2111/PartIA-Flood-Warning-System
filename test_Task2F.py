import numpy
import floodsystem.analysis
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def test_polyfit():
    stations = build_station_list()
    dt = 2
    for station in stations[:30]:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        p = floodsystem.analysis.polyfit(dates, levels, 2)
        assert type(p[1]) == numpy.float64

test_polyfit()


def test_plot_water_level_with_fit():
    stations = build_station_list()
    dt = 2
    for station in stations[:30]:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, 4)
        assert len(dates) == len(levels)

test_plot_water_level_with_fit()


    