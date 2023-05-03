from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Board import Board


def get_file_index(file: str) -> int:
    files_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return files_list.index(file)


def increment_file(file: str) -> str:
    files_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    file_index = get_file_index(file)
    return files_list[file_index + 1]


def decrement_file(file: str) -> str:
    files_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    file_index = get_file_index(file)
    return files_list[file_index - 1]


class Piece:
    def __init__(self, val: int, position: str, color: str, board: 'Board') -> None:
        self._value: int = val
        self._start_position: str = position
        self._position: str = self._start_position
        self.board: 'Board' = board
        self._color: str = color
        self.has_moved: bool = False

    def get_value(self) -> int:
        return self._value

    def get_position(self) -> str:
        return self._position

    def get_rank(self) -> int:
        return int(self.get_position()[1])

    def get_file(self) -> str:
        return self.get_position()[0]

    def get_color(self) -> str:
        return self._color

    def move(self, destination: str) -> bool:
        if self.is_valid_move(destination):
            self._position = destination
            self.has_moved = True
            return True
        return False

    def move_off_board(self) -> None:
        self._position = 'captured'

    def is_valid_move(self, destination: str) -> bool:
        destination_file: str = destination[0]
        destination_rank: int = int(destination[1])

        if destination_rank not in range(1, 9) or destination_file not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return False

        piece_at_destination: Piece | None = self.board.get_piece_at(
            destination)
        if isinstance(piece_at_destination, Piece) and piece_at_destination.get_color() == self.get_color():
            return False

        return True

    def is_valid_rook_move(self, destination: str) -> bool:
        origin_file: str = self._position[0]
        origin_rank: int = int(self._position[1])
        destination_file: str = destination[0]
        destination_rank: int = int(destination[1])
        current_file: str = origin_file
        current_rank: int = origin_rank

        if origin_file != destination_file and origin_rank != destination_rank:
            return False

        while (current_file, current_rank) != (destination_file, destination_rank):
            if get_file_index(origin_file) < get_file_index(destination_file):
                current_file = increment_file(current_file)

            elif get_file_index(origin_file) > get_file_index(destination_file):
                current_file = decrement_file(current_file)

            if origin_rank < destination_rank:
                current_rank += 1

            elif origin_rank > destination_rank:
                current_rank -= 1

            current_square_occupied: bool = self.board.get_piece_at(
                f'{current_file}{current_rank}') is not None
            current_square_not_destination = (current_file, current_rank) != (
                destination_file, destination_rank)

            if current_square_occupied and current_square_not_destination:
                return False

        return True

    def is_valid_bishop_move(self, destination: str) -> bool:
        origin_file: str = self._position[0]
        origin_rank: int = int(self._position[1])
        destination_file: str = destination[0]
        destination_rank: int = int(destination[1])
        current_file: str = origin_file
        current_rank: int = origin_rank

        if abs(destination_rank - origin_rank) != abs(get_file_index(destination_file) - get_file_index(origin_file)):
            return False

        while (current_file, current_rank) != (destination_file, destination_rank):
            if get_file_index(origin_file) < get_file_index(destination_file):
                current_file = increment_file(current_file)

            else:
                current_file = decrement_file(current_file)

            if origin_rank < destination_rank:
                current_rank += 1

            else:
                current_rank -= 1

            current_square_occupied: bool = self.board.get_piece_at(
                f'{current_file}{current_rank}') is not None
            current_square_not_destination = (current_file, current_rank) != (
                destination_file, destination_rank)

            if current_square_occupied and current_square_not_destination:
                return False

        return True


class King(Piece):  # TODO: Still need to add restrictions on check
    def __init__(self, val: int, position: str, color: str, board: 'Board') -> None:
        super().__init__(val, position, color, board)
        self._has_moved: bool = False

    def move(self, destination: str) -> bool | str:
        valid_move_result: bool | str = self.is_valid_move(destination)

        if valid_move_result == True:
            self._has_moved = True
            self._position = destination
            return True

        if valid_move_result == 'castle' and self.do_castle_move(destination):
            return 'castle'

        return False

    def do_castle_move(self, destination: str) -> bool:
        self._has_moved = True
        piece_at_destination: Piece | None = self.board.get_piece_at(
            destination)

        if not piece_at_destination:
            return False

        # Castling with rook 2 moves king to G file and rook to F file
        if piece_at_destination in [self.board.get_piece_object('wR2'), self.board.get_piece_object('bR2')]:
            self._position = f'g{self._position[1]}'
            piece_at_destination._position = f'f{piece_at_destination._position[1]}'
            return True

        # Castling with rook 1 moves king to C file and rook to D file
        if piece_at_destination in [self.board.get_piece_object('wR1'), self.board.get_piece_object('bR1')]:
            self._position = f'c{self._position[1]}'
            piece_at_destination._position = f'd{piece_at_destination._position[1]}'
            return True

        return False

    def is_valid_move(self, destination: str) -> bool | str:
        if not super(King, self).is_valid_move(destination):
            return False

        origin_file: str = self._position[0]
        origin_rank: int = int(self._position[1])
        destination_file: str = destination[0]
        destination_rank: int = int(destination[1])
        current_file: str = origin_file
        current_rank: int = origin_rank
        target_piece = self.board.get_piece_at(destination)

        if not isinstance(target_piece, Piece):
            return False

        # castling
        king_has_not_moved: bool = not self._has_moved
        correct_target_piece: bool = target_piece.get_color(
        ) == self.get_color() and isinstance(target_piece, Rook)
        rook_has_not_moved: bool = not target_piece.has_moved
        conditions_for_castling: bool = king_has_not_moved and correct_target_piece and rook_has_not_moved

        if conditions_for_castling:

            while (current_file, current_rank) != (destination_file, destination_rank):
                if get_file_index(current_file) < get_file_index(destination_file):
                    current_file = increment_file(current_file)
                elif get_file_index(origin_file) > get_file_index(destination_file):
                    current_file = decrement_file(current_file)

                if origin_rank < destination_rank:
                    current_rank += 1
                elif origin_rank > destination_rank:
                    current_rank -= 1

                current_square_occupied: bool = self.board.get_piece_at(
                    f'{current_file}{current_rank}') is not None
                current_square_not_destination = (current_file, current_rank) != (
                    destination_file, destination_rank)

                if current_square_occupied and current_square_not_destination:
                    return False
            return 'castle'

        moved_more_than_one = abs(destination_rank - origin_rank) > 1 or abs(
            get_file_index(destination[0]) - get_file_index(self._position[0])) > 1

        return not moved_more_than_one

    def __str__(self) -> str:
        if self.get_color() == 'black':
            return 'k'
        else:
            return 'K'


class Queen(Piece):
    def __init__(self, val: int, position: str, color: str, board: 'Board') -> None:
        super().__init__(val, position, color, board)

    def move(self, destination: str) -> bool:
        if self.is_valid_move(destination):
            self.has_moved = True
            self._position = destination
            return True
        return False

    def is_valid_move(self, destination: str) -> bool:
        return super(Queen, self).is_valid_move(destination) and (super(Queen, self).is_valid_rook_move(destination) or super(Queen, self).is_valid_bishop_move(destination))

    def __str__(self) -> str:
        if self.get_color() == 'black':
            return 'q'
        else:
            return 'Q'


class Rook(Piece):
    def __init__(self, val: int, position: str, color: str, board: 'Board') -> None:
        super().__init__(val, position, color, board)

    def move(self, destination: str) -> bool:
        if self.is_valid_move(destination):
            self.has_moved = True
            self._position = destination
            return True
        return False

    def is_valid_move(self, destination: str) -> bool:
        return super(Rook, self).is_valid_move(destination) and super(Rook, self).is_valid_rook_move(destination)

    def __str__(self) -> str:
        if self.get_color() == 'black':
            return 'r'
        else:
            return 'R'


class Bishop(Piece):
    def __init__(self, val: int, position: str, color: str, board: 'Board') -> None:
        super().__init__(val, position, color, board)

    def move(self, destination: str) -> bool:
        if self.is_valid_move(destination):
            self.has_moved = True
            self._position = destination
            return True
        return False

    def is_valid_move(self, destination) -> bool:
        return super(Bishop, self).is_valid_move(destination) and super(Bishop, self).is_valid_bishop_move(destination)

    def __str__(self) -> str:
        if self.get_color() == 'black':
            return 'b'
        else:
            return 'B'


class Knight(Piece):
    def __init__(self, val: int, position: str, color: str, board: 'Board') -> None:
        super().__init__(val, position, color, board)

    def move(self, destination: str) -> bool:
        if self.is_valid_move(destination):
            self.has_moved = True
            self._position = destination
            return True
        return False

    def is_valid_move(self, destination) -> bool:
        origin_file: str = self._position[0]
        origin_rank: int = int(self._position[1])
        destination_file: str = destination[0]
        destination_rank: int = int(destination[1])

        if not super(Knight, self).is_valid_move(destination):
            return False

        rank_distance: int = abs(destination_rank - origin_rank)

        file_distance: int = abs(get_file_index(destination_file) -
                                 get_file_index(origin_file))

        return rank_distance * file_distance == 2

    def __str__(self) -> str:
        if self.get_color() == 'black':
            return 'n'
        else:
            return 'N'


class Pawn(Piece):  # TODO: Still need to add "En Passant" functionality
    def __init__(self, val: int, position: str, color: str, board: 'Board') -> None:
        super().__init__(val, position, color, board)

    def move(self, destination: str) -> bool:
        if self.is_valid_move(destination):
            self.has_moved = True
            self._position = destination
            return True
        return False

    def is_valid_move(self, destination) -> bool:
        origin_file: str = self._position[0]
        origin_rank: int = int(self._position[1])
        destination_file: str = destination[0]
        destination_rank: int = int(destination[1])
        rank_distance = abs(destination_rank - origin_rank)
        file_distance = abs(get_file_index(
            destination_file) - get_file_index(origin_file))
        piece_at_destination = self.board.get_piece_at(destination)

        if not super(Pawn, self).is_valid_move(destination):
            print('invalid piece move altogether')
            return False

        if file_distance > 1:
            print('can\'t move that far pal (file)!')
            return False

        if (destination_rank > origin_rank and self.get_color() == 'black') or (
                destination_rank < origin_rank and self.get_color() == 'white'):
            print('can\'t move backwards pal!')
            return False

        if (rank_distance != 1 and self.has_moved) or rank_distance not in [1, 2]:
            print('can\'t move that far pal (rank)!')
            return False

        no_opponent_piece_at_destination: bool = not piece_at_destination or piece_at_destination.get_color() == self.get_color()

        if file_distance == 1 and no_opponent_piece_at_destination:
            print('no opponent at destination')
            return False

        return True

    def __str__(self) -> str:
        if self.get_color() == 'black':
            return 'p'
        else:
            return 'P'
