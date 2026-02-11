from __future__ import annotations


class node:
    def __init__(
        self,
        station_id: int,
        taxi_connections: list[node] = [],
        bus_connections: list[node] = [],
        metro_connections: list[node] = [],
        boat_connections: list[node] = [],
    ) -> None:
        self._station_id = station_id
        self._taxi_connections = taxi_connections
        self._bus_connections = bus_connections
        self._metro_connections = metro_connections
        self._boat_connections = boat_connections

    def add_connections(
        self, connecting_nodes: list[node], connection_type: str
    ) -> None:
        match connection_type:
            case "taxi":
                self._taxi_connections.extend(connecting_nodes)
            case "bus":
                self._bus_connections.extend(connecting_nodes)
            case "metro":
                self._metro_connections.extend(connecting_nodes)
            case "boat":
                self._boat_connections.extend(connecting_nodes)
