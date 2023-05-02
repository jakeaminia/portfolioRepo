from Board import Board
# import tkinter as tk


class Game:
    def __init__(self):
        self.board = Board()
        self.check_mate = False
        self.turn_of_color = 'w'
        self.current_move = 1

    def run_game_loop(self):
        while not self.board.check_mate():
            self.board.show_board()
            if self.turn_of_color == 'w':
                valid_move = False
                while not valid_move:
                    white_move = input('White\'s move: ')
                    if len(white_move) == 2:
                        white_move = f'p{self.board.get_files().index(white_move[0]) + 1} {white_move}'
                    white_move = white_move.split(' ')
                    try:
                        valid_move = self.board.move_piece(
                            'white', white_move[0], white_move[1])
                    except Exception as e:
                        valid_move = False
                self.turn_of_color = 'b'
            elif self.turn_of_color == 'b':
                valid_move = False
                while not valid_move:
                    black_move = input('Black\'s move: ')
                    if len(black_move) == 2:
                        black_move = f'p{self.board.get_files().index(black_move[0]) + 1} {black_move}'
                    black_move = black_move.split(' ')
                    try:
                        valid_move = self.board.move_piece(
                            'black', black_move[0], black_move[1])
                    except Exception as e:
                        valid_move = False
                self.turn_of_color = 'w'
                self.current_move += 1


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
