
from pip import main
from floodsystem.geo import *

def run():

    print(f"Stations within the radius chosen are:")
    stations_within_radius(stations, (52.2053, 0.1218), 10)


if __name__ == "__main__":
        run()  

