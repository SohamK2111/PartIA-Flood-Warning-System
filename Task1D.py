from floodsystem.geo import *

def run():

# Part 1: Rivers with Stations
    a = []
    rivers = []
    for station in stations:
       rivers.append(station.river)
    for river in rivers:
       if river in stations:
           a.append(river)
    
    b = set(rivers)
    c = list(b)
    d = sorted(c)

    print("\n" + str(len(d)) + " stations. First 10 - " + str(d[:10]))
    
#Part 2: Rivers by Station

r_dict = stations_by_river(stations)
print("\n")
print(r_dict["River Aire"])
print("\n")
print(r_dict["River Cam"])
print("\n")
print(r_dict["River Thames"])

if __name__ == "__main__":
    run()