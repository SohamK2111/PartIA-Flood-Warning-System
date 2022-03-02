from floodsystem.flood import stations_level_over_threshold, warning_system, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    listz = []

    for i in stations_level_over_threshold(stations, 1):
        for j in stations:
            if j.name == i[0]:
                if j.name == 'Letcombe Bassett':
                    pass
                elif j.name == 'Cam':
                    pass
                else:
                    listz.append(j)

    #iterating through all stations where relative water level is above 1
    low = []
    moderate = []
    high = []
    severe = []
    
    for i in listz:
        dt = 2
        dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
        
        #x is the derivative of the water levels and tells us how high the risk is
        x = warning_system(i, dates, levels, 3)

        if x < 0:
            low.append(i)
        elif x > 0 and x <= 1:
            moderate.append(i)
        elif x > 1 and x < 1.5:
            high.append(i)
        else:
            severe.append(i)
    
    for y in severe:
        print('WARNING - {} has severe risk of flooding'.format(y.name))
        
    for z in high:
        print('{} has high risk of flooding'.format(z.name))
    
    for f in moderate:
        print('{} has moderate risk of flooding'.format(f.name))
    
    for g in low:
        print('{} has low risk of flooding'.format(g.name))    

    
if __name__ == "__main__":
    run()
    
    

