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

    def __str__(self) -> str:
        taxi_connections = []
        for taxi in self._taxi_connections:
            taxi_connections.append(taxi.station_id)
        print(sorted(taxi_connections))
        return f"id: {self._station_id}, taxi: {len(self._taxi_connections)}, bus: {len(self._bus_connections)}, metro: {len(self._metro_connections)} boat: {len(self._boat_connections)}"

    @property
    def station_id(self) -> int:
        return self._station_id

    def add_connections(
        self, connecting_nodes: list[node], connection_type: str
    ) -> None:
        print(self.station_id)
        match connection_type.lower():
            case "taxi":
                self._taxi_connections.extend(connecting_nodes)
            case "bus":
                self._bus_connections.extend(connecting_nodes)
            case "metro":
                self._metro_connections.extend(connecting_nodes)
            case "boat":
                self._boat_connections.extend(connecting_nodes)
