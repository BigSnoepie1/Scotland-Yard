from abc import ABC, abstractmethod

from implementation import board, game, node


class Strategy(ABC):
    @abstractmethod
    def get_next_move(self) -> int | list[int]:
        pass


class Minimax(Strategy):
    def get_next_move(self) -> int | list[int]:
        pass
