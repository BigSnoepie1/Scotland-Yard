class AsymmetricNodeError(Exception):
    def __init__(self, root, other, transporttype) -> None:
        self.message = f"{root} points to {other} using {transporttype}, but not the other way around"
        super().__init__(self.message)


class SelfReferencingError(Exception):
    def __init__(self, root, transporttype) -> None:
        self.message = f"{root} points to itself using{transporttype}"
        super().__init__(self.message)


starting_positions = [
    138,
    26,
    34,
    171,
    53,
    50,
    132,
    94,
    198,
    103,
    155,
    197,
    29,
    112,
    117,
    174,
    13,
    91,
]
starting_positions = [str(x) for x in starting_positions]
starting_tickets = [10, 8, 4]
starting_tickets = [str(x) for x in starting_tickets]


def transform_line(line: list[str], is_location=True) -> str:
    new_line = line.pop(0)
    for element in line:
        new_line += ";" + element

    return new_line


def generate_proper_gameinfo(
    destination_file: str,
    connections: str,
    starting_tickets: list[str],
    starting_positions: list[str],
) -> None:
    with open(destination_file, "w") as empty:
        empty.write("")
    with open(connections) as file:
        for line in file:
            new_line = line.split("\t")
            if new_line[0] == "Nummer":
                transformed_line = (
                    "Starting positions:"
                    + ";"
                    + transform_line(starting_positions, False)
                    + "\n"
                    + "Starting tickets:"
                    + ";"
                    + transform_line(starting_tickets, False)
                    + "\n"
                )
            else:
                transformed_line = transform_line(new_line)
            with open(destination_file, "a") as new_file:
                new_file.write(transformed_line)


generate_proper_gameinfo(
    "game_info/game_info.txt",
    "game_info/Board_info.txt",
    starting_tickets,
    starting_positions,
)


transform_line(starting_positions)
