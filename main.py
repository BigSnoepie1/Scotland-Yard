from implementation import board, game, node


def get_setup_input():
    print("Initializing Game")
    number_of_detectives = input("How many detectives are there this game? ")
    while not (
        number_of_detectives.isdigit() and int(number_of_detectives) > 0
    ):
        number_of_detectives = input("Please put in a whole number ")
    return int(number_of_detectives)


def main():
    number_of_detectives = get_setup_input()
    test_game = game.Game(number_of_detectives, "game_info/game_info.txt")
    

    test_game._board.test_data()



if __name__ == "__main__":
    main()
