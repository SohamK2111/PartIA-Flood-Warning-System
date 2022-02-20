
from pip import main
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level



def run():

    stations = build_station_list()
    print("\n")
    print("Rivers with the highest relative water levels:")
    print(stations_highest_rel_level(stations, 9))
    print("\n")


if __name__ == "__main__":
        run()  