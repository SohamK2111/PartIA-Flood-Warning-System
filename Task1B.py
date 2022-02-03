from pip import main
from floodsystem.geo import *

def run():

   a = stations_by_distance(stations, (52.2053, 0.1218))
   print("The 10 CLOSEST stations are: ")
   for i in range(10):
      print(str(a[i][0].name) + ", " + str(a[i][0].town) + ", " + str(a[i][1]))

   print("\n The 10 FURTHEST stations are: ")
   for i in range(10):
      print(str(a[-i][0].name) + ", " + str(a[-i][0].town) + ", " + str(a[-i][1]))

if __name__ == "__main__":
        run()      




