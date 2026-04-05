from collections import defaultdict

from implementation.node import Node


class Board:
    def __init__(self, game_info: str) -> None:
        self._game_info = game_info
        self._stations = []
        self._generate_game()

    class _LinesIterator:
        def __init__(self, file_path: str):
            self._current_index = 0
            self._separated_lines = []
            with open(file_path) as file:
                for line in file:
                    line_segments = line.split(";")
                    self._separated_lines.append(line_segments)

        def __iter__(self):
            return self

        def __next__(self):
            i = self._current_index
            if i >= len(self._separated_lines):
                raise StopIteration
            else:
                self._current_index += 1
                return self._separated_lines[i]

    def _generate_game(self):
        self._extract_common_info()
        self._add_stations()
        self._add_connections()

    def _extract_common_info(self) -> None:
        for line_segments in self._LinesIterator(self._game_info):
            if line_segments[0] == "Starting positions:":
                self._starting_positions = self._convert_game_string(
                    line_segments[1:]
                )
            elif line_segments[0] == "Starting tickets:":
                self._starting_tickets = defaultdict(int)
                self._starting_tickets["Taxi"] = int(line_segments[1])
                self._starting_tickets["Bus"] = int(line_segments[2])
                self._starting_tickets["Metro"] = int(line_segments[3])
            else:
                break

    def _add_stations(self) -> None:
        for line_segments in self._LinesIterator(self._game_info):
            if line_segments[0] in {
                "Starting positions:",
                "Starting tickets:",
            }:
                continue
            else:
                self._stations.append(Node(int(line_segments[0])))

    def _add_connections(self) -> None:
        for line_segments in self._LinesIterator(self._game_info):
            if line_segments[0] in {
                "Starting positions:",
                "Starting tickets:",
            }:
                continue
            else:
                id, taxi, bus, metro, boat = line_segments
                station = self._smart_station_finder(int(id))
                taxi = self._convert_game_string(taxi)
                bus = self._convert_game_string(bus)
                metro = self._convert_game_string(metro)
                boat = self._convert_game_string(boat)
                if len(taxi) > 0:
                    station.add_connections(
                        self._indices_to_nodes(taxi), "taxi"
                    )
                if len(bus) > 0:
                    station.add_connections(self._indices_to_nodes(bus), "bus")
                if len(metro) > 0:
                    station.add_connections(
                        self._indices_to_nodes(metro), "metro"
                    )
                if len(boat) > 0:
                    station.add_connections(
                        self._indices_to_nodes(boat), "boat"
                    )

    def _convert_game_string(self, numbers: str | list[str]) -> list[int]:
        return_list = []
        if isinstance(numbers, str):
            numbers = numbers.split(",")
        for item in numbers:
            new_item = item.replace("\n", "")
            if len(new_item) > 0:
                return_list.append(int(new_item))
        return return_list

    def _smart_station_finder(self, id: int) -> Node:
        if id < len(self._stations):
            current_candidate = self._stations[id]
        else:
            current_candidate = self._stations[id - 1]
        if current_candidate.station_id == id:
            return current_candidate
        offset = 1
        while True:
            error_count = 0
            lower_id = id - offset
            if lower_id >= 0:
                current_candidate = self._stations[lower_id]
                if current_candidate.station_id == id:
                    return current_candidate
            else:
                error_count += 1

            upper_id = id + offset
            if upper_id <= len(self._stations) - 1:
                current_candidate = self._stations[upper_id]
                if current_candidate.station_id == id:
                    return current_candidate
            else:
                error_count += 1

            if error_count >= 2:
                raise ValueError(f"Station {id} does not exist")

            offset += 1

    def _indices_to_nodes(self, indices: list[int]) -> list[Node]:
        nodes = []
        for i in indices:
            nodes.append(self._smart_station_finder(i))
        return nodes

    def _test_data(self) -> bool:
        for station in self._stations:
            id = station.station_id
            if len(station._taxi_connections) > 0:
                for taxi in station._taxi_connections:
                    if station not in taxi._taxi_connections:
                        raise LookupError(
                            f"{id} points to {station.station_id}, but not the other way around"
                        )
            if len(station._bus_connections) > 0:
                for bus in station._bus_connections:
                    if station not in bus._bus_connections:
                        raise LookupError(
                            f"{id} points to {station.station_id}, but not the other way around"
                        )
            if len(station._metro_connections) > 0:
                for metro in station._metro_connections:
                    if station not in metro._metro_connections:
                        raise LookupError(
                            f"{id} points to {station.station_id}, but not the other way around"
                        )
            if len(station._boat_connections) > 0:
                for boat in station._boat_connections:
                    if station not in boat._boati_connections:
                        raise LookupError(
                            f"{id} points to {station.station_id}, but not the other way around"
                        )

    def print_board(self) -> None:
        for location in self._stations:
            print(location)
