from pip import main
from floodsystem.geo import *
from floodsystem.station import *


def run():

    b = []
    incon_stations = inconsistent_typical_range_stations(stations)
    for station in incon_stations:
        b.append(station.name)
    
    print("\n")
    print("Stations with inconsistent data:")
    print(sorted(b))
    print("\n")


if __name__ == "__main__":
        run()  

