# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
s_id0 = "test-s-id0"
m_id0 = "test-m-id0"
label0 = "some station"
coord0 = (-2.0, 4.0)
trange0 = (-2.3, -3.4445)
river0 = "River 0"
town0 = "My Town"
s0 = MonitoringStation(s_id0, m_id0, label0, coord0, trange0, river0, town0)
# Create a station
s_id1 = "test-s-id"
m_id1 = "test-m-id"
label1 = "some station"
coord1 = (-2.0, 4.0)
trange1 = (-2.3, 3.4445)
river1 = "River 1"
town1 = "My Town"
s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
list_river = [s0, s1]


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def tesst_typical_range_consistent():
    assert s0.typical_range_consistent() is False
    assert s1.typical_range_consistent() is True


def test_inconsistent_typical_range_stations():
    inconsistent_station = inconsistent_typical_range_stations(list_river)
    assert inconsistent_station == [s0.name]
