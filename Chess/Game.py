from Board import Board
from Piece import get_file_index


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.check_mate = False
        self.turn_of_color = 'White'
        self.next_turn_of_color = 'Black'
        self.current_move = 1

    def next_turn(self) -> None:
        self.turn_of_color, self.next_turn_of_color = self.next_turn_of_color, self.turn_of_color
        self.current_move = self.current_move + 1

    def run_game_loop(self) -> None:

        while not self.board.is_check_mate():

            self.board.show_board()
            valid_move: bool = False

            while not valid_move:

                move_choice = input(
                    f'{self.turn_of_color}\'s move: ').strip()

                if len(move_choice) == 2:
                    move_choice = f'p{get_file_index(move_choice[0]) + 1} {move_choice}'

                move_choice = move_choice.split(' ')

                try:
                    valid_move = self.board.move_piece(
                        self.turn_of_color, move_choice[0], move_choice[1])

                except Exception as _:
                    valid_move = False

                self.next_turn()


# my_board = Board()
# # my_board.show_board()
# my_board.move_piece('white', 'p5', 'e4')
# my_board.move_piece('black', 'p5', 'e5')
# my_board.move_piece('white', 'N1', 'c3')
# my_board.move_piece('white', 'p2', 'b4')
# my_board.move_piece('black', 'B2', 'd6')
# # my_board.move_piece('white', 'R1', 'b1')
# my_board.move_piece('black', 'Q', 'f6')
# my_board.move_piece('black', 'Q', 'f4')
# my_board.move_piece('black', 'Q', 'e3')
# my_board.move_piece('white', 'B1', 'a3')
# my_board.move_piece('white', 'Q', 'e2')
# my_board.move_piece('white', 'N2', 'f3')
# my_board.move_piece('white', 'p7', 'g3')
# my_board.move_piece('white', 'B2', 'g2')
# my_board.move_piece('white', 'K', 'h1')
#
# my_board.show_board()
new_game = Game()
new_game.run_game_loop()
