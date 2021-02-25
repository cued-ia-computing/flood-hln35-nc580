from .station import MonitoringStation, inconsistent_typical_range_stations
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    list_stations_over_threshold = []
    inconsistent_list = inconsistent_typical_range_stations(stations)
    for station in stations:
        if station in inconsistent_list:
            pass
        else:
            if station.relative_water_level():     
                if station.relative_water_level() > tol:
                    list_stations_over_threshold.append((station, station.relative_water_level()))
    
    return sorted_by_key(list_stations_over_threshold, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    tol = 0
    list_stations_with_relative_water_level = stations_level_over_threshold(stations, tol)
    top_N_stations = []
    for station, relative_level in list_stations_with_relative_water_level[0:N]:
        top_N_stations.append(station)
    return top_N_stations
