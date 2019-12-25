import os
import time
n = 10

class Disc():
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return str(self.size)


class Pillar():
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return f'{[i for i in self.stack]}'

    def build(self, disc):
        self.stack.insert(0, disc)

    def add(self, disc):
        self.stack.append(disc)

    def remove(self):
        return self.stack.pop()

    def next_disc(self):
        return self.stack[-1]

    def can_accept(self, disc):
        if len(self.stack) == 0:
            return True
        elif disc.size < self.stack[-1].size:
            return True
        else:
            return False


class Game():
    def __init__(self, n):
        self.pillar1 = Pillar()
        self.pillar2 = Pillar()
        self.pillar3 = Pillar()
        for i in range(1, n + 1):
            self.pillar1.build(Disc(i))

    def __repr__(self):
        return f'Pillar 1: {self.pillar1}\nPillar 2: {self.pillar2}\nPillar 3: {self.pillar3}'

    def solve(self):
        for _ in range(15):
            os.system('clear')
            print(self)
            time.sleep(1)
            next_disc = self.pillar1.next_disc()
            if self.pillar2.can_accept(next_disc):
                self.pillar2.add(self.pillar1.remove())
            elif self.pillar3.can_accept(next_disc):
                self.pillar3.add(self.pillar1.remove())
            else:
                if self.pillar3.can_accept(self.pillar2.next_disc()):
                    self.pillar3.add(self.pillar2.remove())
                elif self.pillar2.can_accept(self.pillar3.next_disc()):
                    self.pillar2.add(self.pillar3.remove())


my_game = Game(n)
print(my_game.solve())

