from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

# stations within 10 km of city centre
def run():


    # build station list
    stations = build_station_list()
    # assign centre and radius
    centre = (52.2053, 0.1218)
    r = 10
    print(stations_within_radius(stations, centre, r))

if __name__ == "__main__":
    
    
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
