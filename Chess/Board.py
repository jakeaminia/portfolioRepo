from Piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King


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
            piece_moved_successfully = self.white_pieces.get(
                piece).move(destination)
        elif color == 'black':
            piece_position = self.black_pieces.get(piece).get_position()
            piece_moved_successfully = self.black_pieces.get(
                piece).move(destination)
        if piece_moved_successfully == 2:
            self.update([piece_position, destination])
            return True
        elif piece_moved_successfully:
            if piece_at_destination is not None:
                piece_at_destination.position = None
                if color == 'white':
                    self.black_captures[piece_at_destination.__str__(
                    )] = piece_at_destination.get_value()
                else:
                    self.white_captures[piece_at_destination.__str__(
                    )] = piece_at_destination.get_value()
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
