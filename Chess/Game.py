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

                move_choice = move_choice.split(' ')
                origin: str = move_choice[0]
                destination: str = move_choice[1]

                try:
                    valid_move = self.board.move_piece(
                        self.turn_of_color, origin, destination)

                except Exception as _:
                    valid_move = False

            self.next_turn()


new_game = Game()
new_game.run_game_loop()
