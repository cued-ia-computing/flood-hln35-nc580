from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    # build station list
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    for station, relative_level in stations_level_over_threshold(stations, tol):
        print(station.name + ' ' + str(station.relative_water_level()))
    

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()