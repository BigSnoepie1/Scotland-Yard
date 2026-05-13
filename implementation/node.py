from __future__ import annotations


class Node:
    def __init__(
        self,
        station_id: int,
        taxi_connections: list[Node] = [],
        bus_connections: list[Node] = [],
        metro_connections: list[Node] = [],
        boat_connections: list[Node] = [],
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
        return f"id: {self._station_id}, taxi: {len(self._taxi_connections)}, bus: {len(self._bus_connections)}, metro: {len(self._metro_connections)} boat: {len(self._boat_connections)}"

    @property
    def station_id(self) -> int:
        return self._station_id

    def add_connections(
        self, connecting_nodes: list[Node], connection_type: str
    ) -> None:
        match connection_type.lower():
            case "taxi":
                self._taxi_connections = connecting_nodes
            case "bus":
                self._bus_connections = connecting_nodes
            case "metro":
                self._metro_connections = connecting_nodes
            case "boat":
                self._boat_connections = connecting_nodes

    def get_connecting_stations(self, transport_type: str) -> list[Node]:
        match transport_type:
            case "taxi":
                connections = self._taxi_connections
            case "bus":
                connections = self._bus_connections
            case "metro":
                connections = self._metro_connections
            case "boat":
                connections = self._boat_connections
            case _:
                raise ValueError("Connection type does not exist")
        return connections
