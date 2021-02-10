from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list


def run():

    # build station list
    stations = build_station_list()
    print(sorted(inconsistent_typical_range_stations(stations)))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
