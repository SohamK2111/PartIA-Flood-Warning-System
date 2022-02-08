
from pip import main
from floodsystem.geo import *

def run():

    a = stations_within_radius(stations, (52.2053, 0.1218), 10)
    list_of_names = []
    for station in a:
      list_of_names.append(station.name)

    print("\n")
    print("Stations within this radius are:")
    print(sorted(list_of_names))
    print("\n")


if __name__ == "__main__":
        run()  

