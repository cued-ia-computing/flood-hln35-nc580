from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    list_10_highest_rel_water_level = stations_highest_rel_level(stations, N)
    for station in list_10_highest_rel_water_level:
        print(station.name + ' ' + str(station.relative_water_level()))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
