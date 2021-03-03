# Import modules
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Highest risk of flooding when water is above high typical range
    stations_tol = stations_level_over_threshold(stations, 1)
    stations_tol.sort(key=lambda x: x[1])

    # Consider risk based on data for past 5 days
    dt = 5
    dic_risk = {}

    for station in stations_tol:
        # Risk is 0 for low, 1 for moderate, 2 for high, 3 for sevre
        risk = 0
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt))
        # We count how many times the level increases compared to the previous level
        n = 0
        for i in range(len(levels) - 1):
            if type(levels[i + 1]) == float and type(levels[i]) == float:
                if levels[i] < levels[i + 1]:
                    n += 1
                # Severe risk more than 60% increase, high more than 45% and moderate more than 30%
            if n > 0.6 * len(levels):
                risk = 3
            elif n > 0.45 * len(levels):
                risk = 2
            elif n > 0.3 * len(levels):
                risk = 1
            dic_risk[station] = risk

    # Severe risk stations
    print('Severe:')
    for station in stations_tol:
        if dic_risk[station] == 3:
            print(station[0].town)

    print('\n' * 1)

    # Print high stations
    print('High:')
    for station in stations_tol:
        if dic_risk[station] == 2:
            print(station[0].town)

    print('\n' * 1)

    # Print moderate stations
    print('Moderate:')
    for station in stations_tol:
        if dic_risk[station] == 1:
            print(station[0].town)

    print('\n' * 1)

    # Print low stations
    print('Low:')
    for station in stations_tol:
        if dic_risk[station] == 0:
            print(station[0].town)

    print('\n' * 1)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
