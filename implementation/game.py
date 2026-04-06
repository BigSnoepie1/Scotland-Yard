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
        self._generate_players(number_of_detectives)

    def _generate_players(self, number_of_detectives: int):
        possible_starting_places = self._board._starting_positions.copy()
        mister_X_start = possible_starting_places.pop(
            random.randrange(len(possible_starting_places))
        )
        self._detectives = []
        self._mister_X = Player(
            mister_X_start, 1000, 1000, 1000, number_of_detectives
        )

        starting_tickets = self._board._starting_tickets
        for i in range(number_of_detectives):
            starting_position = possible_starting_places.pop(
                random.randrange(len(possible_starting_places))
            )
            self._detectives.append(
                Player(
                    starting_position,
                    starting_tickets["Taxi"],
                    starting_tickets["Bus"],
                    starting_tickets["Metro"],
                    starting_tickets["Black"],
                )
            )
