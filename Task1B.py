from unicodedata import name
from pip import main
from floodsystem.geo import *

def run():

   a = stations_by_distance(stations, (52.2053, 0.1218))

   name_town_distance = []
   list_of_towns = []
   for i in range(10):
      for station in stations:
         if a[i][0] == station.name:
            list_of_towns.append(station.town)
   
   for j in range(10):
      name_town_distance.append(a[j][0])
      name_town_distance.append(list_of_towns[j])
      name_town_distance.append(a[j][1])
   
   name_town_distance2 = []
   list_of_towns2 = []
   for i in range(1,11):
      for station in stations:
         if a[-i][0] == station.name:
            list_of_towns2.append(station.town)
   
   for j in range(1, 11):
      name_town_distance2.append(a[-j][0])
      name_town_distance2.append(list_of_towns2[j-1])
      name_town_distance2.append(a[-j][1])


   print("\n")
   print("The 10 CLOSEST stations are: ")
   print(name_town_distance)
   print("\n")
   print("The 10 FURTHEST stations are: ")
   print(name_town_distance2)
   
if __name__ == "__main__":
        run()      




