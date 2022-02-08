from pip import main
from floodsystem.geo import *
from floodsystem.station import *


def run():

    print("\n")
    print(f"Stations with inconsistent data:")
    inconsistent_typical_range_stations(stations)
    print("\n")


if __name__ == "__main__":
        run()  

