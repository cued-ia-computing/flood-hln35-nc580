import datetime
import matplotlib.dates
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Finding the 5 stations for which the water levels are greatest 
    dt = 2
    N = 5
    top_5_stations_highest = stations_highest_rel_level(stations, N)

    # Fetch measurement data for the 5 stations 
    for station in top_5_stations_highest:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    # Plot values for stations apart from the blacklisted one
    for station in top_5_stations_highest:
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()