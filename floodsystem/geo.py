# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
#return a dictionary that map river names to lists of stations 
def stations_by_river(stations):
    river_dict={}
    for station in stations:
        
        river=station.river
        name=station.name
        if river not in river_dict:
          
            river_dict[river]=[name]
        else:
            river_dict[river].append(name)
    

    return river_dict
#return river names from a list of Monitoring station objects
def rivers_with_station(stations):
    rivers=set()
    for station in stations:
        rivers.add(station.river)
    return rivers
#Return N rivers with the greatest number of stations
def rivers_by_station_numbers(stations,N):
    river_dict=stations_by_river(stations)
    river_number_stations=[]
    for river in river_dict:
        i=0
        for station in river_dict[river]:
            i+=1
        river_number_stations.append((river,i))
    def myFunc(e):
        return e[1]
   
    river_number_stations.sort(key=myFunc,reverse=True)
    #check river with the same number of stations
    
    n=N
    
    for i in range(len(river_number_stations)-N):

      if river_number_stations[N-1][1]==river_number_stations[N+i][1]:
         n+=1
    #return list of rivers and their numbers of stations  
    N_river=river_number_stations[:n]
    return N_river
    

from haversine import haversine, Unit
from .station import MonitoringStation
from .stationdata import build_station_list

# 1B return a list of stations and their distances
def stations_by_distance(stations,p):
    #build an station list
    stations_list = []
    stations=build_station_list()
    for station in stations:
        #calculate distance using haversine formula
        distance=haversine(station.coord,p)
        #make into a list of tuples
        stations_list.append((station.name,station.town,distance))
    #sort by distance
    return sorted_by_key(stations_list,2)

#1C stations within a radius from a coordinate
def stations_within_radius(stations,centre,r):
    #build list of stations
    stations_in_radius=[]
    stations=build_station_list()
    for station in stations:
        #calculate distance
        distance=haversine(station.coord,centre)
        # make sure the stations in list are within radius
        if r>=distance:
            stations_in_radius.append(station.name)
    return sorted(stations_in_radius)
