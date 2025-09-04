"""
Problem Description
We are trying to create a video game, in which aliens are attacking a friendly base. You can imagine the base to be a 1D line that goes from 0 to n. The alien's attack length is always 1 but it can choose to attack anywhere along the base. We would like to implement two functions for the video game - attack and is_game_over.

For the attack function, it takes a number from 0 to n, and should mark the corresponding place to start the attack. For example, if attack is called with 3, then the line subset 3-4 should be marked as destroyed.

For the is_game_over function, it should return a boolean, which specifies whether or not the entire base has been destroyed.

Imagine the following sequences of calls:

b = Base(10)
b.attack(0)           -> segment 0-1 is attacked
b.attack(1)           -> segment 1-2 is attacked
b.attack(2)           -> segment 2-3 is attacked
b.attack(3)           -> segment 3-4 is attacked
b.attack(4)           -> segment 4-5 is attacked
b.is_game_over()      -> return False
b.attack(5)           -> segment 5-6 is attacked
b.attack(6)           -> segment 6-7 is attacked
b.attack(7)           -> segment 7-8 is attacked
b.attack(8)           -> segment 8-9 is attacked
b.attack(9)           -> segment 9-10 is attacked
b.is_game_over()      -> return True

"""
class Base:

    def __init__(self, n):
        self.maps = {}
        for i in range(0, n):
            self.maps[i] = (i, i + 1)

        print(self.maps)

    def attack(self, n):

        # 2 cases int and float

        if n == int(n):
            self.maps[n] = (0, 0)
        else:
            n1 = int(n)
            v1 = self.maps[n1]
            if abs(v1[0] - v1[1]) > 0:
                self.maps[n1] = (n1, min(v1[1], n))
            if n1 + 1 in self.maps:
                v2 = self.maps[n1 + 1]
                if abs(v2[0] - v2[1]) > 0:
                    self.maps[n1 + 1] = (max(v2[0], n+1), v2[1])

        print(self.maps)

    def is_game_over(self):
        summ = 0
        for i in self.maps:
            diff = abs(self.maps[i][0] - self.maps[i][1])
            summ += diff
        return summ == 0


if __name__ == '__main__':
    b = Base(3)
    b.attack(0.1)
    b.attack(0)
    b.attack(1.2)
    b.attack(1)
    b.attack(2.0)

    print(b.is_game_over())
