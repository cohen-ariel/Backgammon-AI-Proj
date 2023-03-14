from copy import deepcopy
from cell import Cell

B = 'b'  # for black
W = 'w'  # for white
N = 'n'  # for None
CELLS_NUM = 26

# NUM OF CELLS AT THE BEGINNING
I1, I2, I3, I4, I5, I6, I7, I8 = 1, 6, 8, 12, 13, 17, 19, 24

# NUM OF PIPS AT THE BEGINNING
PIPS1, PIPS2, PIPS3 = 2, 3, 5


class Board:
    def __init__(self, board=None, turn='b'):
        # SET BOARD

        if board is None:
            temp = []
            for i in range(CELLS_NUM):
                if i == I1:
                    c = Cell(B, PIPS1, i)
                elif i == I2:
                    c = Cell(W, PIPS3, i)
                elif i == I3:
                    c = Cell(W, PIPS2, i)
                elif i == I4:
                    c = Cell(B, PIPS3, i)
                elif i == I5:
                    c = Cell(W, PIPS3, i)
                elif i == I6:
                    c = Cell(B, PIPS2, i)
                elif i == I7:
                    c = Cell(B, PIPS3, i)
                elif i == I8:
                    c = Cell(W, PIPS1, i)
                else:
                    c = Cell(N, 0, i)

                temp.append(c)
            self.board = deepcopy(temp)

        else:
            temp = []
            for i in range(CELLS_NUM):
                c = board[i]
                color = c.get_color()
                pips = c.get_pips()
                num = c.get_num()
                new_cell = Cell(color, pips, num)
                temp.append(new_cell)

                self.board = deepcopy(temp)

        # SET TURN
        self.turn = turn

    def print_board(self):
        nums = []
        pips = []
        colors = []
        temp = self.get_board()
        for i in range(26):
            nums.append(temp[i].get_num())
            pips.append(temp[i].get_pips())
            colors.append(temp[i].get_color())

    def get_board(self):
        return self.board

    def get_turn(self):
        return self.turn

    def switch_turn(self):
        if self.turn == 'b':
            self.turn = 'w'
        else:
            self.turn = 'b'

    def conquer(self, cell):
        num_of_cell = cell.get_num()
        color = self.board[num_of_cell]
        self.board[num_of_cell].conquer(color)

    def add(self, cell):
        num_of_cell = cell.get_num()
        self.board[num_of_cell].add()

    def eat(self, cell):
        if cell.get_color() == 'b':
            cell.set_color('w')
            self.board[0].set_color('b')
            self.board[0].add()
        else:
            cell.set_color('b')
            self.board[25].set_color('w')
            self.board[25].add()

    def copy_board(self):
        # returns a copy of the board
        cells = []
        for i in range(26):
            c = self.board[i]
            color = c.get_color()
            pips = c.get_pips()
            num = c.get_num()
            cells.append(Cell(color, pips, num))

        new_board = Board(cells, self.get_turn())
        return new_board

    def is_same(self, other):
        # gets another Board object and returns if self and other boards are same
        other_board = other.get_board()
        for i in range(26):
            if self.board[i].get_color() != other_board[i].get_color():
                return False
            if self.board[i].get_pips() != other_board[i].get_pips():
                return False
        return True

    def get_winner(self):
        # returns the winner if there is one
        cells = self.board
        black_won = True
        white_won = True
        for i in range(25):
            if cells[i].get_color() == B:
                black_won = False
            if cells[i+1].get_color() == W:
                white_won = False

        if black_won:
            return "BLACK"
        elif white_won:
            return "WHITE"
        else:
            return None

    def all_in_last_quarter(self):
        # returns if all the pips of the current turn are in the last quarter (meaning moving pips
        # out is legal)
        board = self.get_board()
        turn = self.get_turn()

        all_in_last_quarter = True
        if turn == B:
            for cell in board:
                if cell.get_color() == turn and not (18 < cell.get_num() < 25):
                    all_in_last_quarter = False
        else:
            for cell in board:
                if cell.get_color() == turn and not (0 < cell.get_num() < 7):
                    all_in_last_quarter = False

        return all_in_last_quarter

    def from_legal(self, num_cell):
        # gets a cell number and returns if it's legal to move it
        from_color = self.board[num_cell].get_color()
        turn = self.get_turn()
        legal = True

        if turn == B:
            if num_cell == 25:
                legal = False
            if self.board[0].get_pips() != 0 and num_cell != 0:
                legal = False
        if turn == W:
            if num_cell == 0:
                legal = False
            if self.board[25].get_pips() != 0 and num_cell != 25:
                legal = False

        return from_color == turn and legal

    def legal_move(self, tup_cells, tup_dices):
        # gets 2 tuples (from cell A, to cell B) and (dice 1, dice 2)
        # returns if the move is legal

        from_cell = self.board[tup_cells[0]]
        to_cell = self.board[tup_cells[1]]
        dice1 = tup_dices[0]
        dice2 = tup_dices[1]

        from_color = from_cell.get_color()
        to_color = to_cell.get_color()
        turn = self.get_turn()

        from_legal = from_color == turn
        legal_take_out = True
        if turn == B:
            if to_cell.get_num() == 25 and not self.all_in_last_quarter():
                legal_take_out = False
            if dice1 is None:
                dice_legal = to_cell.get_num() - from_cell.get_num() == dice2
            elif dice2 is None:
                dice_legal = to_cell.get_num() - from_cell.get_num() == dice1
            else:
                dice_legal = to_cell.get_num() - from_cell.get_num() == dice1 or to_cell.get_num() - from_cell.get_num() == dice2

        if turn == W:
            if to_cell.get_num() == 0 and not self.all_in_last_quarter():
                legal_take_out = False
            if dice1 is None:
                dice_legal = to_cell.get_num() - from_cell.get_num() == -dice2
            elif dice2 is None:
                dice_legal = to_cell.get_num() - from_cell.get_num() == -dice1
            else:
                dice_legal = to_cell.get_num() - from_cell.get_num() == -dice1 or to_cell.get_num() - from_cell.get_num() == -dice2

        if to_cell.get_num() == 0 or to_cell.get_num() == 25:
            to_legal = legal_take_out
        else:
            to_legal = from_color == to_color or to_color == N or to_cell.get_pips() == 1

        move_legal = from_legal and to_legal

        return move_legal and dice_legal


    def is_stuck(self, tup_dices):
        # gets a dices tuple and returns if there's any legal move to be done
        for i in range(26):
            from_cell = self.board[i]
            color = from_cell.get_color()

            if color == self.turn:
                for j in range(26):
                    to_cell = self.board[j]
                    from_num = from_cell.get_num()
                    to_num = to_cell.get_num()

                    tup_cells = (from_num, to_num)

                    if self.legal_move(tup_cells, tup_dices):
                        return False
        return True

    def h_func1(self):
        # calculates the heuristic value of the board by the following strategy:
        # the less pips that are "single", the higher the h value is.
        # (also affecting the value considering enemy "single" pips)

        h = 0
        cells = self.get_board()
        for c in cells:
            if c.get_pips() == 1:
                if c.get_color() == self.get_turn():
                    h -= 1
                else:
                    h += 1

        max_h = 30
        # h's range is between -15 (every player's pip is single) to 15 (all enemy's pips are single)
        # to normalize h: add 16 to h (so the range is 1-31) and then divide by the maximum (30)

        normalized_h = (h + 16) / max_h
        return normalized_h

    def h_func2(self):
        # calculates the heuristic value of the board by the following strategy:
        # the higher the sum of distances of pips from the end of the board, the lower the h value.
        # (also affecting the value considering sum distances of enemy pips)

        h = 0
        cells = self.get_board()
        turn = self.get_turn()

        for c in cells:
            if c.get_color() == turn:
                if turn == B:
                    distance = 25 - c.get_num()
                else:
                    distance = c.get_num()
                h -= c.get_pips() * distance

            else:
                if turn == B:
                    distance = 25 - c.get_num()
                else:
                    distance = c.get_num()
                h += c.get_pips() * distance

        return abs(h)

    def h_func3(self):
        # calculates the heuristic value of the board by the following strategy:
        # the more enemy pips are eaten, the higher the h value is.
        # (also affecting the value considering self pips eaten)

        h = 0
        cells = self.get_board()
        turn = self.get_turn()
        if turn == B:
            first_cell = 0
            enemys_cell = 25
        else:
            first_cell = 25
            enemys_cell = 0

        h -= cells[first_cell].get_pips()
        h += cells[enemys_cell].get_pips()

        max_h = 30
        # h's range is between -15 (all pips are eaten) to 15 (all enemy's pips are eaten)
        # to normalize h: add 16 to h (so the range is 1-31) and then divide by the maximum (30)
        normalized_h = (h + 16) / max_h

        return normalized_h

    def get_h_value(self, h_set):
        # get an h_set
        w1 = h_set.get_w1()
        w2 = h_set.get_w2()
        w3 = h_set.get_w3()

        h = self.h_func1() * w1 + self.h_func2() * w2 + self.h_func3() * w3
        return h


