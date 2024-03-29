from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    dt = 10
    top_5_highest_rel_level = stations_highest_rel_level(stations, N)
    for station in top_5_highest_rel_level:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    for station in top_5_highest_rel_level:
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
