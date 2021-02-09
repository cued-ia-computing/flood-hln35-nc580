from floodsystem.geo import stations_by_river
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_numbers
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
station1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s_id1 = "test-s-id"
m_id1 = "test-m-id"
label1 = "another station"
coord1 = (-2.0, 4.0)
trange1 = (-2.3, 3.4445)
river1 = "River Y"
town1 = "My Town"
station2 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
s = []
s.append(station1)
s.append(station2)


def test_stations_by_river():
    a = stations_by_river(s)
    assert a == {river: [label], river1: [label1]}


def test_rivers_with_station():
    list_river = rivers_with_station(s)
    assert len(list_river) == 2


def test_rivers_by_station_numbers():
    river_list2 = rivers_by_station_numbers(s, 2)
    river_list1 = rivers_by_station_numbers(s, 1)
    assert len(river_list2) == 2
    assert len(river_list1) == 2
    assert river_list2 == [(river, 1), (river1, 1)]
