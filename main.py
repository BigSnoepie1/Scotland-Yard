from implementation import node,board




def main():
    game = board.board("game_info/game_info.txt")
    game.generate_game()
    print(game._starting_positions)
    print(game._starting_tickets)
    game.print_board()


if __name__ == "__main__":
    main()
