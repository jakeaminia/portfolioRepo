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
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) + 1]
                elif self.board.get_files().index(self.position[0]) > self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) - 1]
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
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) + 1]
                else:
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) - 1]
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
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) + 1]
                elif self.board.get_files().index(self.position[0]) > self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) - 1]
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
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) + 1]
                elif self.board.get_files().index(self.position[0]) > self.board.get_files().index(destination[0]):
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) - 1]
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
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) + 1]
                else:
                    current_position[0] = self.board.get_files(
                    )[self.board.get_files().index(current_position[0]) - 1]
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
