from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_numbers


def run():
    stations = build_station_list()
    # Print river with N highest number of stations
    N = 10
    river_station_numbers = rivers_by_station_numbers(stations, N)
    for i in range(len(river_station_numbers)):
        print(river_station_numbers[i])


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
