
from pip import main
from floodsystem.geo import *


def run():

    print("\n")
    print("Rivers with the greatest number of stations:")
    print(rivers_by_station_number(stations, 9))
    print("\n")


if __name__ == "__main__":
        run()  

