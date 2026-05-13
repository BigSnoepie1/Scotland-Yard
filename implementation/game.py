import random
from dataclasses import dataclass

from implementation.board import Board
from implementation.node import Node


@dataclass
class Player:
    location: int
    taxi_tickets: int
    bus_tickets: int
    metro_tickets: int
    black_tickets: int


class Game:
    def __init__(
        self,
        number_of_detectives: int,
        game_info_path: str = "game_info/game_info.txt",
    ) -> None:
        self._board = Board(game_info_path)
        self._mister_x_history = []
        self._detectives_history = []
        self._generate_players(number_of_detectives)
        self._test_board()

    def _generate_players(self, number_of_detectives: int):
        possible_starting_places = self._board._starting_positions.copy()
        mister_X_start = possible_starting_places.pop(
            random.randrange(len(possible_starting_places))
        )
        self._detectives = []
        self._mister_X = Player(
            mister_X_start, 1000, 1000, 1000, number_of_detectives
        )
        self._mister_x_history.append(mister_X_start)
        starting_tickets = self._board._starting_tickets
        for i in range(number_of_detectives):
            starting_position = possible_starting_places.pop(
                random.randrange(len(possible_starting_places))
            )
            self._detectives_history.append([starting_position])
            self._detectives.append(
                Player(
                    starting_position,
                    starting_tickets["Taxi"],
                    starting_tickets["Bus"],
                    starting_tickets["Metro"],
                    starting_tickets["Black"],
                )
            )

    def check_space_occupation(self, space: int) -> bool:
        if self._mister_x_history[-1] == space:
            return True
        for detective in self._detectives_history:
            if detective[-1] == space:
                return True
        return False

    def move(
        self, destination: int, transport_type: str, detective_number=None
    ):
        if detective_number:
            player = self._detectives[detective_number]
        else:
            player = self._mister_X

        if self.check_space_occupation(destination):
            return False

        match transport_type:
            case "taxi":
                if player.taxi_tickets <= 0:
                    return False
                player.taxi_tickets -= 1
            case "bus":
                if player.bus_tickets <= 0:
                    return False
                player.bus_tickets -= 1
            case "metro":
                if player.metro_tickets <= 0:
                    return False
                player.metro_tickets -= 1
            case "boat":
                if player.black_tickets <= 0:
                    return False
                player.black_tickets -= 1

    def _test_board(self) -> None:
        if self._board.test_data():
            print("Board succesfully initialized!")
