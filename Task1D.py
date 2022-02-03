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

    a = "River Aire"
    b = "River Cam"
    c = "River Thames"

    list_a = []
    list_b = []
    list_c = []

    for station in stations:
        if a == station.river:
            list_a.append(station.name)
        elif b == station.river:
            list_b.append(station.name)
        elif c ==station.river:
            list_c.append(station.name)
    print("\n \'River Aire\'")
    print(str(sorted(list_a)))
    print("\n \'River Cam\'")
    print(str(sorted(list_b)))
    print("\n \'River Thames\'")
    print(str(sorted(list_c)))

if __name__ == "__main__":
    run()