
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.utils import sorted_by_key  # noqa

stations = build_station_list()
stations_within_radius(stations, (52.2053, 0.1218), 10)



