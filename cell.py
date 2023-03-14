class Cell:
    def __init__(self, color='n', pips=0, num=0):
        self.color = color  # 'b' for BLACK, 'w' for WHITE or 'n' for NONE
        self.pips = pips # num of pips in cell (0-15)
        self.num = num  # num of cell (0-25)

    def get_color(self):
        return self.color

    def get_num(self):
        return self.num

    def get_pips(self):
        return self.pips

    def set_color(self, color):
        self.color = color

    def set_num(self, num):
        self.num = num

    def set_pips(self, pips):
        self.pips = pips

    def take_off(self):
        self.pips -= 1
        if self.pips == 0:
            self.color = 'n'

    def conquer(self, new_color):
        self.pips += 1
        self.color = new_color

    def add(self):
        self.pips += 1

    def eat(self):
        if self.color == 'b':
            self.color = 'w'
            num = 0
        else:
            self.color = 'b'
            num = 25
        self.board[num].add()
