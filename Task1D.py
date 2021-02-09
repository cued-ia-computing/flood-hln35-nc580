from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    # Build list of stations
    stations = build_station_list()
    #list of rivers
    river_list=rivers_with_station(stations)
    dict_river_and_station=stations_by_river(stations)
    # Print number of rivers with at least 1 station 
    print("Number of rivers: {}".format(len(river_list)))
    list_rivers=list(river_list)
    list_rivers.sort()
    first_10_rivers=[]
    for i in range(10):
      first_10_rivers.append(list_rivers[i])
    print('First 10 -{}'.format(str(first_10_rivers)))
    #Print stations on 3 rivers
    for river in dict_river_and_station.keys():
        if river in ['River Aire', 'River Cam', 'River Thames']:
           stations_on_river=dict_river_and_station[river]
           stations_on_river.sort()
           print('{}'.format(stations_on_river)) 
   
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
