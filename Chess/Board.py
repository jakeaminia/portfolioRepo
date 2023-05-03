from Piece import Piece, King, Queen, Rook, Bishop, Knight, Pawn


class Board:

    def __init__(self) -> None:
        self.white_captures = dict()
        self.black_captures = dict()
        self._captures: dict[str, Piece] = dict()
        self._pieces: dict[str, Piece] = {
            'wK': King(0, 'e1', 'white', self),
            'wQ': Queen(9, 'd1', 'white', self),
            'wR1': Rook(5, 'a1', 'white', self),
            'wR2': Rook(5, 'h1', 'white', self),
            'wB1': Bishop(3, 'c1', 'white', self),
            'wB2': Bishop(3, 'f1', 'white', self),
            'wN1': Knight(3, 'b1', 'white', self),
            'wN2': Knight(3, 'g1', 'white', self),
            'wp1': Pawn(1, 'a2', 'white', self),
            'wp2': Pawn(1, 'b2', 'white', self),
            'wp3': Pawn(1, 'c2', 'white', self),
            'wp4': Pawn(1, 'd2', 'white', self),
            'wp5': Pawn(1, 'e2', 'white', self),
            'wp6': Pawn(1, 'f2', 'white', self),
            'wp7': Pawn(1, 'g2', 'white', self),
            'wp8': Pawn(1, 'h2', 'white', self),
            'bK': King(0, 'e8', 'black', self),
            'bQ': Queen(9, 'd8', 'black', self),
            'bR1': Rook(5, 'a8', 'black', self),
            'bR2': Rook(5, 'h8', 'black', self),
            'bB1': Bishop(3, 'c8', 'black', self),
            'bB2': Bishop(3, 'f8', 'black', self),
            'bN1': Knight(3, 'b8', 'black', self),
            'bN2': Knight(3, 'g8', 'black', self),
            'bp1': Pawn(1, 'a7', 'black', self),
            'bp2': Pawn(1, 'b7', 'black', self),
            'bp3': Pawn(1, 'c7', 'black', self),
            'bp4': Pawn(1, 'd7', 'black', self),
            'bp5': Pawn(1, 'e7', 'black', self),
            'bp6': Pawn(1, 'f7', 'black', self),
            'bp7': Pawn(1, 'g7', 'black', self),
            'bp8': Pawn(1, 'h7', 'black', self)}
        self._squares: dict[str, Piece | None] = {'-': None}
        self._is_check_mate: bool = False

        for ch in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            for i in range(8):
                self._squares[f'{ch}{i + 1}'] = None

        self.update()

    def move_piece(self, color: str, origin: str, destination: str):
        piece_moved_successfully: bool | str = False
        piece_position: str = ''
        piece_at_destination: Piece | None = self.get_piece_at(destination)
        piece_at_origin: Piece | None = self.get_piece_at(origin)

        if isinstance(piece_at_origin, Piece):
            if piece_at_origin.get_color() != color:
                return False
            piece_position = piece_at_origin.get_position()
            piece_moved_successfully = piece_at_origin.move(destination)

        if piece_moved_successfully == 'castle':
            self.update(piece_position, destination)
            return True

        if piece_moved_successfully == True:
            if piece_at_destination:
                self.add_piece_to_captures(piece_at_destination)

            self.update(piece_position)
            return True

        else:
            print(f'\ninvalid move: {origin, destination}\n')
            return False

    def show_board(self):
        white_captures: str = self.get_capture_names('white')
        black_score: int = self.get_score('black')
        black_captures: str = self.get_capture_names('black')
        white_score: int = self.get_score('white')
        print(
            f'\n{white_captures} [{black_score}]\n= = = = = = = = = = = = = = = = = = = = = =\n')
        for i in range(8):
            for ch in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                if self._squares[f'{ch}{8 - i}'] is None:
                    print('-     ', end='')
                else:
                    print(self._squares[f'{ch}{8 - i}'], '    ', end='')
            print('\n')
        print(
            f'\n= = = = = = = = = = = = = = = = = = = = = =\n{black_captures} [{white_score}]\n')

    def update(self, *clear_positions: str):
        for piece in self._pieces.values():
            self._squares[piece.get_position()] = piece

        for position in clear_positions:
            self._squares[position] = None

    def get_piece_at(self, position: str) -> Piece | None:
        return self._squares.get(position)

    def get_piece_object(self, piece_name: str) -> Piece | None:
        return self._pieces.get(piece_name, None)

    def add_piece_to_captures(self, piece: Piece) -> None:
        self._captures[piece.__str__()] = piece
        piece.move_off_board()

    def is_check_mate(self) -> bool:
        return self._is_check_mate

    def list_captures(self, color: str, sort: bool) -> list[Piece]:
        from Piece import Piece
        result_list: list[Piece] = list()

        for piece in self._captures.values():
            if piece.get_color() == color:
                result_list.append(piece)

        if sort:
            return sorted(result_list, key=lambda piece: piece.get_value(), reverse=True)

        return result_list

    def get_capture_names(self, color: str) -> str:
        result: str = ''
        for piece in self.list_captures(color, True):
            result += piece.__str__() + ' '
        return result.strip()

    def get_score(self, color: str) -> int:
        other_color = ''
        if color == 'white':
            other_color = 'black'
        else:
            other_color = 'white'
        return sum(piece.get_value() for piece in self.list_captures(other_color, False))
