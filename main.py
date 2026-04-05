from implementation import board, node



def main():
    

    game = board.Board("game_info/game_info.txt")
    print(game._starting_positions)
    print(game._starting_tickets)
    game.print_board()
    game._test_data()


if __name__ == "__main__":
    main()
