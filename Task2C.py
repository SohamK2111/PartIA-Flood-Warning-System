from pip import main
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():

    stations = build_station_list()
    update_water_levels(stations)
    print("\n")
    print("Rivers with the highest relative water levels:")
    for i in stations_highest_rel_level(stations, 9):
        print("{}, {}".format(i.name, MonitoringStation.relative_water_level(i)))
    print("\n")
    


if __name__ == "__main__":
        run()  

