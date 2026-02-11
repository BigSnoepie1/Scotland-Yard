from node import node


class board:
    def __init__(self, nodes: list[node] = []) -> None:
        self._nodes = nodes

    def add_nodes(self, nodes: list[node]) -> None:
        self._nodes.extend(nodes)
