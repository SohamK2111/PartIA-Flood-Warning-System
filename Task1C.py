
from pip import main
from floodsystem.geo import *

def run():

    print("\n")
    print(f"Stations within this radius are:")
    stations_within_radius(stations, (52.2053, 0.1218), 10)
    print("\n")


if __name__ == "__main__":
        run()  

