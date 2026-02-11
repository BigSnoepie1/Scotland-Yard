from implementation.node import node


class board:
    def __init__(self, game_info: str) -> None:
        self._game_info = game_info
        self._game_data = []

    def _generate_dict(self, data: list[str]) -> dict[str, str]:
        if len(data) != 4:
            raise ValueError("Needs exactly 4 elements")
        return {
            "Taxi": data[0],
            "Bus": data[1],
            "Metro": data[2],
            "Boat": data[3],
        }

    def _convert_game_string(self, numbers: list[str]) -> list[int]:
        newlist = []
        for item in numbers:
            new_item = item.replace("\n", "")
            if len(new_item) > 0:
                newlist.append(int(new_item))
            else:
                newlist.append(None)
        return newlist

    def _open_game(self) -> list[tuple[str, dict[str, str]]]:
        game_data = []
        with open(self._game_info) as file:
            for line in file:
                line_segments = line.split(";")
                if line_segments[0] == "Starting positions:":
                    self._starting_positions = self._convert_game_string(
                        line_segments[1:]
                    )
                elif line_segments[0] == "Starting tickets:":
                    data = line_segments[1:]
                    data.append("")
                    self._starting_tickets = self._generate_dict(data)

                else:
                    game_data.append(
                        (
                            line_segments[0],
                            self._generate_dict(line_segments[1:]),
                        )
                    )
        return game_data

    def _get_location(self, node_id: int) -> node:
        for location in self._locations:
            if location.station_id == node_id:
                break
        else:
            raise ValueError(f"Location {node_id} does not exist")
        return location

    def _generate_connections(
        self, connection_data: tuple[str, dict[str, str]]
    ) -> None:
        current_station_id, connections = connection_data
        current_station_id = int(current_station_id)
        current_station = self._get_location(current_station_id)
        for type, connections in connections.items():
            connection_list = connections.split(",")
            connection_list = self._convert_game_string(connection_list)
            other_stations = []
            for other_station_id in connection_list:
                if other_station_id is not None:
                    other_stations.append(self._get_location(other_station_id))
                else:
                    break
            current_station.add_connections(other_stations, type)

    def _generate_nodes(
        self, game_data: list[tuple[str, dict[str, str]]]
    ) -> None:
        self._locations = set()
        for datapoint in game_data:
            self._locations.add(node(int(datapoint[0])))
        for datapoint in game_data:
            self._generate_connections(datapoint)

    def generate_game(self) -> None:
        game_data = self._open_game()
        self._generate_nodes(game_data)

    def _test_data(self) -> bool:
        pass

    def print_board(self) -> None:
        for location in self._locations:
            print(location)
