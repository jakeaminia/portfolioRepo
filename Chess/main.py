# import tkinter as tk


class Piece:
    def __init__(self, val, position, color, board):
        self.value = val
        self.start_position = position
        self.position = self.start_position
        self.board = board
        self.color = color

    def move(self, destination):
        if self.is_valid_move(destination):
            self.position = destination
            return True

    def is_valid_move(self, destination):
        if int(destination[1]) + 1 not in range(8) or destination[0] not in self.board.files:
            return False
        if self.board.get_piece(destination) is not None and self.board.get_piece(
                destination).get_color() == self.get_color():
            return False
        return True

    def get_value(self):
        return self.value

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color


class Pawn(Piece):
    def __init__(self, val, position, color, board):
        super().__init__(val, position, color, board)
        self.has_moved = False

    def __str__(self):
        if self.get_color() == 'black':
            return 'p'
        else:
            return 'P'

    def move(self, destination):
        if self.is_valid_move(destination):
            if not self.has_moved:
                self.has_moved = True
            self.position = destination
            return True

    def is_valid_move(self, destination):
        if not super(Pawn, self).is_valid_move(destination):
            return False
        elif int(destination[1]) == int(self.get_position()[1]) or abs(int(destination[1]) - int(self.position[1])) > 2:
            return False
        elif (int(destination[1]) > int(self.get_position()[1]) and self.get_color() == 'black') or (
                int(destination[1]) < int(self.get_position()[1]) and self.get_color() == 'white'):
            return False
        elif int(destination[1]) - int(self.position[1]) > 1 and self.has_moved:
            return False
        elif abs(self.board.get_files().index(destination[0]) - self.board.get_files().index(self.position[0])) > 1:
            return False
        elif abs(self.board.get_files().index(destination[0]) - self.board.get_files().index(
                self.position[0])) == 1 and (self.board.get_piece(destination) is None or self.board.get_piece(
            destination).get_color() == self.get_color()):
            return False
        else:
            return True


class Knight(Piece):
    def __init__(self, val, position, color, board):
        super().__init__(val, position, color, board)

    def __str__(self):
        if self.get_color() == 'black':
            return 'n'
        else:
            return 'N'

    def move(self, destination):
        if self.is_valid_move(destination):
            self.position = destination
            return True

    def is_valid_move(self, destination):
        if not super(Knight, self).is_valid_move(destination):
            return False
        return (abs(int(destination[1]) - int(self.position[1])) == 2 and abs(
            self.board.get_files().index(destination[0]) - self.board.get_files().index(
                self.position[0])) == 1) or (abs(int(destination[1]) - int(self.position[1])) == 1 and abs(
            self.board.get_files().index(destination[0]) - self.board.get_files().index(
                self.position[0])) == 2)


class Bishop(Piece):
    def __init__(self, val, position, color, board):
        super().__init__(val, position, color, board)

    def __str__(self):
        if self.get_color() == 'black':
            return 'b'
        else:
            return 'B'

    def move(self, destination):
        if self.is_valid_move(destination):
            self.position = destination
            return True

    def is_valid_move(self, destination):
        if not super(Bishop, self).is_valid_move(destination):
            return False
        if abs(int(destination[1]) - int(self.position[1])) != abs(
                self.board.get_files().index(destination[0]) - self.board.get_files().index(self.position[0])):
            return False
        else:
            current_position = [self.position[0], int(self.position[1])]
            while current_position != [destination[0], int(destination[1])]:
                if self.board.get_files().index(self.position[0]) < self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) + 1]
                else:
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) - 1]
                if self.position[1] < destination[1]:
                    current_position[1] += 1
                else:
                    current_position[1] -= 1
                # print(current_position)
                # print(self.board.get_piece(f'{current_position[0]}{current_position[1]}'))
                # print(f'{current_position[0]}{current_position[1]}', destination)
                if (self.board.get_piece(
                        f'{current_position[0]}{current_position[1]}') is not None) and current_position != [
                    destination[0], int(destination[1])]:
                    return False
            else:
                return True


class Rook(Piece):
    def __init__(self, val, position, color, board):
        super().__init__(val, position, color, board)
        self.has_moved = False

    def __str__(self):
        if self.get_color() == 'black':
            return 'r'
        else:
            return 'R'

    def move(self, destination):
        if self.is_valid_move(destination):
            if not self.has_moved:
                self.has_moved = True
            self.position = destination
            return True

    def is_valid_move(self, destination):
        if not super(Rook, self).is_valid_move(destination):
            return False
        if self.position[0] != destination[0] and self.position[1] != destination[1]:
            return False
        else:
            current_position = [self.position[0], int(self.position[1])]
            while current_position != [destination[0], int(destination[1])]:
                if self.board.get_files().index(self.position[0]) < self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) + 1]
                elif self.board.get_files().index(self.position[0]) > self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) - 1]
                if self.position[1] < destination[1]:
                    current_position[1] += 1
                elif self.position[1] > destination[1]:
                    current_position[1] -= 1
                # print(f'{current_position[0]}{current_position[1]}', destination)
                if (self.board.get_piece(
                        f'{current_position[0]}{current_position[1]}') is not None) and current_position != [
                    destination[0], int(destination[1])]:
                    return False
            else:
                return True


class Queen(Piece):
    def __init__(self, val, position, color, board):
        super().__init__(val, position, color, board)

    def __str__(self):
        if self.get_color() == 'black':
            return 'q'
        else:
            return 'Q'

    def move(self, destination):
        if self.is_valid_move(destination):
            self.position = destination
            return True

    def is_valid_bishop_move(self, destination):
        if abs(int(destination[1]) - int(self.position[1])) != abs(
                self.board.get_files().index(destination[0]) - self.board.get_files().index(self.position[0])):
            return False
        else:
            current_position = [self.position[0], int(self.position[1])]
            while current_position != [destination[0], int(destination[1])]:
                if self.board.get_files().index(self.position[0]) < self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) + 1]
                else:
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) - 1]
                if self.position[1] < destination[1]:
                    current_position[1] += 1
                else:
                    current_position[1] -= 1
                # print(current_position)
                # print(self.board.get_piece(f'{current_position[0]}{current_position[1]}'))
                # print(f'{current_position[0]}{current_position[1]}', destination)
                if (self.board.get_piece(
                        f'{current_position[0]}{current_position[1]}') is not None) and current_position != [
                    destination[0], int(destination[1])]:
                    return False
        return True

    def is_valid_rook_move(self, destination):
        if self.position[0] != destination[0] and self.position[1] != destination[1]:
            return False
        else:
            current_position = [self.position[0], int(self.position[1])]
            while current_position != [destination[0], int(destination[1])]:
                if self.board.get_files().index(self.position[0]) < self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) + 1]
                elif self.board.get_files().index(self.position[0]) > self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) - 1]
                if self.position[1] < destination[1]:
                    current_position[1] += 1
                elif self.position[1] > destination[1]:
                    current_position[1] -= 1
                # print(f'{current_position[0]}{current_position[1]}', destination)
                if (self.board.get_piece(
                        f'{current_position[0]}{current_position[1]}') is not None) and current_position != [
                    destination[0], int(destination[1])]:
                    return False
        return True

    def is_valid_move(self, destination):
        if not super(Queen, self).is_valid_move(destination):
            return False
        return self.is_valid_rook_move(destination) or self.is_valid_bishop_move(destination)


class King(Piece):
    def __init__(self, val, position, color, board):
        super().__init__(val, position, color, board)
        self.has_moved = False

    def __str__(self):
        if self.get_color() == 'black':
            return 'k'
        else:
            return 'K'

    def move(self, destination):
        valid_move = self.is_valid_move(destination)
        if valid_move and valid_move != 2:
            if not self.has_moved:
                self.has_moved = True
            self.position = destination
            return True
        elif self.is_valid_move(destination) == 2:
            self.has_moved = True
            target_piece = self.board.get_piece(destination)
            if self.board.white_pieces['R2'] == target_piece or self.board.black_pieces['R2'] == target_piece:
                self.position = f'g{self.position[1]}'
                target_piece.position = f'f{target_piece.position[1]}'
                return 2
            else:
                self.position = f'c{self.position[1]}'
                target_piece.position = f'd{target_piece.position[1]}'
                return 2

    def is_valid_move(self, destination):
        target_piece = self.board.get_piece(destination)
        if int(destination[1]) + 1 not in range(8) or destination[0] not in self.board.files:
            return False
        elif not self.has_moved and target_piece.get_color() == self.get_color() and target_piece.__str__() == 'R' \
                and not target_piece.has_moved:
            current_position = [self.position[0], int(self.position[1])]
            while current_position != [destination[0], int(destination[1])]:
                if self.board.get_files().index(self.position[0]) < self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) + 1]
                elif self.board.get_files().index(self.position[0]) > self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files()[self.board.get_files().index(current_position[0]) - 1]
                if self.position[1] < destination[1]:
                    current_position[1] += 1
                elif self.position[1] > destination[1]:
                    current_position[1] -= 1
                # print(f'{current_position[0]}{current_position[1]}', destination)
                if (self.board.get_piece(
                        f'{current_position[0]}{current_position[1]}') is not None) and current_position != [
                    destination[0], int(destination[1])]:
                    return False
            return 2
        elif abs(int(destination[1]) - int(self.position[1])) > 1 or abs(
                self.board.get_files().index(destination[0]) - self.board.get_files().index(self.position[0])) > 1:
            return False
        else:
            return True


class Board:
    def __init__(self):
        # self.root = tk.Tk()
        # self.root.geometry('600x600')
        # self.label = tk.Label(self.root, text='Chess Board')
        # self.label.pack(padx=10, pady=10)
        # self.frame = tk.Frame(self.root, width=100, height=100)
        # for i in range(8):
        #     self.frame.columnconfigure(i, weight=1)
        #     for j in range(8):
        #         this_button = tk.Button(self.frame, text=f"{j},{i}")
        #         this_button.grid(row=j, column=i, sticky='nesw')
        # self.frame.pack(pady=10, padx=20, fill='both')
        # self.frame.grid_propagate(0)
        self.white_captures = {}
        self.black_captures = {}
        self.white_pieces = {'R1': Rook(5, 'a1', 'white', self), 'N1': Knight(3, 'b1', 'white', self),
                             'B1': Bishop(3, 'c1', 'white', self),
                             'Q': Queen(9, 'd1', 'white', self),
                             'K': King(0, 'e1', 'white', self), 'B2': Bishop(3, 'f1', 'white', self),
                             'N2': Knight(3, 'g1', 'white', self),
                             'R2': Rook(5, 'h1', 'white', self), 'p1': Pawn(1, 'a2', 'white', self),
                             'p2': Pawn(1, 'b2', 'white', self), 'p3': Pawn(1, 'c2', 'white', self),
                             'p4': Pawn(1, 'd2', 'white', self), 'p5': Pawn(1, 'e2', 'white', self),
                             'p6': Pawn(1, 'f2', 'white', self), 'p7': Pawn(1, 'g2', 'white', self),
                             'p8': Pawn(1, 'h2', 'white', self)}
        self.black_pieces = {'R1': Rook(5, 'a8', 'black', self), 'N1': Knight(3, 'b8', 'black', self),
                             'B1': Bishop(3, 'c8', 'black', self),
                             'Q': Queen(9, 'd8', 'black', self),
                             'K': King(0, 'e8', 'black', self), 'B2': Bishop(3, 'f8', 'black', self),
                             'N2': Knight(3, 'g8', 'black', self),
                             'R2': Rook(5, 'h8', 'black', self), 'p1': Pawn(1, 'a7', 'black', self),
                             'p2': Pawn(1, 'b7', 'black', self), 'p3': Pawn(1, 'c7', 'black', self),
                             'p4': Pawn(1, 'd7', 'black', self), 'p5': Pawn(1, 'e7', 'black', self),
                             'p6': Pawn(1, 'f7', 'black', self), 'p7': Pawn(1, 'g7', 'black', self),
                             'p8': Pawn(1, 'h7', 'black', self)}
        self.squares = {'-': None}
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.is_check_mate = False
        for ch in self.files:
            for i in range(8):
                self.squares[f'{ch}{i + 1}'] = None

        self.update()
        # self.root.mainloop()

    def move_piece(self, color, piece, destination):
        piece_moved_successfully = False
        piece_position = None
        piece_at_destination = self.get_piece(destination)
        if color == 'white':
            piece_position = self.white_pieces.get(piece).get_position()
            piece_moved_successfully = self.white_pieces.get(piece).move(destination)
        elif color == 'black':
            piece_position = self.black_pieces.get(piece).get_position()
            piece_moved_successfully = self.black_pieces.get(piece).move(destination)
        if piece_moved_successfully == 2:
            self.update([piece_position, destination])
            return True
        elif piece_moved_successfully:
            if piece_at_destination is not None:
                piece_at_destination.position = None
                if color == 'white':
                    self.black_captures[piece_at_destination.__str__()] = piece_at_destination.get_value()
                else:
                    self.white_captures[piece_at_destination.__str__()] = piece_at_destination.get_value()
            self.update([piece_position])
            return True
        else:
            print(f'\ninvalid move: {color, piece, destination}\n')

    def show_board(self):
        print('\n= = = = = = = = = = = = = = = = = = = = = =', list(self.white_captures.keys()),
              sum(self.white_captures.values()), '\n')
        for i in range(8):
            for ch in self.files:
                if self.squares[f'{ch}{8 - i}'] is None:
                    print('-     ', end='')
                else:
                    print(self.squares[f'{ch}{8 - i}'], '    ', end='')
            print('\n')
        print('= = = = = = = = = = = = = = = = = = = = = =', list(self.black_captures.keys()),
              sum(self.black_captures.values()), '\n')

    def update(self, clear_squares=None):
        if clear_squares is None:
            clear_squares = []
        for piece in self.white_pieces.values():
            self.squares[piece.get_position()] = piece
        for piece in self.black_pieces.values():
            self.squares[piece.get_position()] = piece
        for square in clear_squares:
            self.squares[square] = None

    def get_piece(self, position):
        return self.squares[position]

    def get_files(self):
        return self.files

    def check_mate(self):
        return self.is_check_mate


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
                        valid_move = self.board.move_piece('white', white_move[0], white_move[1])
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
                        valid_move = self.board.move_piece('black', black_move[0], black_move[1])
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
