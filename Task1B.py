from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key
from haversine import haversine

#10 closest and 10 furthest stations to p
def run():
    #build station list
    stations=build_station_list()
    p=(52.2053,0.1218)

    #10 closest stations
    closest=stations_by_distance(stations,p)[:10]
    #print 10 furthest stations
    furthest=stations_by_distance(stations,p)[-10:]
    print("The 10 closest are:", closest)
    print("The 10 furthest are:", furthest)
    

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()