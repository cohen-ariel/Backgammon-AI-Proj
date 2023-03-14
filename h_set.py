import random

B = 'b'
W = 'w'
N = 'n'


class H_Set:
    def __init__(self, w1=None, w2=None, w3=None):
        if w1 is not None:
            self.w1 = w1
            self.w2 = w2
            self.w3 = w3
        else:
            self.w1 = random.randint(1, 99) / 100
            self.w2 = random.randint(1, 99) / 100
            self.w3 = random.randint(1, 99) / 100

    def get_w1(self):
        return self.w1

    def get_w2(self):
        return self.w2

    def get_w3(self):
        return self.w3

    def set_w1(self, w1):
        self.w1 = w1

    def set_w2(self, w2):
        self.w2 = w2

    def set_w3(self, w3):
        self.w3 = w3

    def print_h_set(self):
        print("w1: "+str(self.w1))
        print("w2: "+str(self.w2))
        print("w3: "+str(self.w3))

    def mutation(self):
        # gets a number of h_sets (20% of the population), and slightly changes their
        # weight values randomly.

        change_w1 = random.randint(-10, 10) / 100
        change_w2 = random.randint(-10, 10) / 100
        change_w3 = random.randint(-10, 10) / 100

        if self.w1 < 0.1:
            self.w1 = self.w1 + abs(change_w1)
        elif 0.1 <= self.w1 <= 0.9:
            self.w1 = self.w1 + change_w1
        else:
            self.w1 = self.w1 - abs(change_w1)

        if self.w2 < 0.1:
            self.w2 = self.w2 + abs(change_w2)
        elif 0.1 <= self.w2 <= 0.9:
            self.w2 = self.w2 + change_w2
        else:
            self.w2 = self.w2 - abs(change_w2)

        if self.w3 < 0.1:
            self.w3 = self.w3 + abs(change_w3)
        elif 0.1 <= self.w3 <= 0.9:
            self.w3 = self.w3 + change_w3
        else:
            self.w3 = self.w3 - abs(change_w3)


