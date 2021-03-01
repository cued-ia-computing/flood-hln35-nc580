from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run(): 
    
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Severe risk stations
    tol = 1
    for station, relative_level in stations_level_over_threshold(stations, tol):
        print(station.name + ' ' + str(station.relative_water_level()) + ':' + 'Severe Risk')
    
    tol = 0.75 and tol < 1
    for station, relative_level in stations_level_over_threshold(stations, tol):
        print(station.name + ' ' + str(station.relative_water_level()) + ':' + 'High Risk')

    tol = 0.5 and tol < 0.75
    for station, relative_level in stations_level_over_threshold(stations, tol):
        print(station.name + ' ' + str(station.relative_water_level()) + ':' + 'Moderate Risk')

    tol = 0.25 and tol < 0.5
    for station, relative_level in stations_level_over_threshold(stations, tol):
        print(station.name + ' ' + str(station.relative_water_level()) + ':' + 'Low Risk')
    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()