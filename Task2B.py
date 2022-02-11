from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list

def run():

    stations = build_station_list()
    a = stations_level_over_threshold(stations, 0.8)
    for i in a:
        print(i[0], i[1])

if __name__ == "__main__":
    run()

