import random
from animals import Empty
from animals import Plankton
from animals import Killerwhale
from animals import Shark
from animals import Dolphin
from living import Living
from living import Animals
import string


class God:
    def __init__(self, size: int):
        self.n: int = size

    def init(self, paramOcean: [[]], planktonNumber: int, dolphinNumber: int, sharkNumber: int, killerwhaleNumber: int) -> None:
        for i in range(0, self.n):
            for j in range(0, self.n):
                paramOcean[i][j] = Empty(i, j)

        x = random.randrange(1, self.n)
        y = random.randrange(1, self.n)
        for i in range(0, planktonNumber + 1):
            while paramOcean[x][y].getType() != Animals.EMPTY:
                x = random.randrange(1, self.n)
                y = random.randrange(1, self.n)
            paramOcean[x][y] = Plankton(x, y, 2, 0)
        for i in range(0, dolphinNumber + 1):
            while paramOcean[x][y].getType() != Animals.EMPTY:
                x = random.randrange(1, self.n)
                y = random.randrange(1, self.n)
            paramOcean[x][y] = Dolphin(x, y, 4, True, 0)
        for i in range(0, sharkNumber + 1):
            while paramOcean[x][y].getType() != Animals.EMPTY:
                x = random.randrange(1, self.n)
                y = random.randrange(1, self.n)
            paramOcean[x][y] = Shark(x, y, 5, True, 0)
        for i in range(0, killerwhaleNumber + 1):
            while paramOcean[x][y].getType() != Animals.EMPTY:
                x = random.randrange(1, self.n)
                y = random.randrange(1, self.n)
            paramOcean[x][y] = Killerwhale(x, y, 6, True, 0)

    def update(self, paramOcean: [[]]) -> None:
        for i in range(1, self.n - 1):
            for j in range(1, self.n - 1):
                tempOcean = paramOcean[i][j].next(paramOcean)
                if tempOcean:
                    for h in tempOcean:
                        paramOcean[h.getX()][h.getY()] = h

    def deleteOcean(self, paramOcean: []) -> None:
        for i in range(1, self.n - 1):
            for j in range(1, self.n - 1):
                paramOcean[i][j] = None

    def showOcean(self, paramOcean: []) -> None:
        for i in range(1, self.n - 1):
            for j in range(1, self.n - 1):
                if paramOcean[i][j].getType() == Animals.EMPTY:
                    print("E", end=" ")
                if paramOcean[i][j].getType() == Animals.plankton:
                    print("P", end=" ")
                if paramOcean[i][j].getType() == Animals.dolphin:
                    print("D", end=" ")
                if paramOcean[i][j].getType() == Animals.shark:
                    print("S", end=" ")
                if paramOcean[i][j].getType() == Animals.killerwhale:
                    print("K", end=" ")
            print()

    def getSizeOfTheOcean(self) -> int:
        return self.n

    def setSizeOfTheOcean(self, size: int) -> None:
        self.n = size

    def addAnimal(self, ocean: [[]]) -> None:
        print("p - plankton")
        print("d - dolphin")
        print("s - shark")
        print("k - killerwhale")
        choice = str(input())
        males = ["male", "female"]
        if choice == "p":
            x = int(input("input x "))
            while x < 1 or x > self.n - 2:
                x = int(input("try more "))
            y = int(input("input y "))
            while y < 1 or y > self.n - 2:
                y = int(input("try more "))
            hp = int(input("input hp "))
            while hp < 1 or hp > 2:
                hp = int(input("try more "))
            age = int(input("input age "))
            while age < 1 or age > 2:
                age = int(input("try more "))
            ocean[x][y] = Plankton(x, y, hp, age)
            return
        if choice == "d":
            x = int(input("input x "))
            while x < 1 or x > self.n - 2:
                x = int(input("try more "))
            y = int(input("input y "))
            while y < 1 or y > self.n - 2:
                y = int(input("try more "))
            hp = int(input("input hp "))
            while hp < 1 or hp > 4:
                hp = int(input("try more "))
            male = str(input("input male "))
            while not male in males:
                male = str(input("try more "))
            age = int(input("input age "))
            while age < 1 or age > 4:
                age = int(input("try more "))
            ocean[x][y] = Dolphin(x, y, hp, male, age)
            return
        if choice == "s":
            x = int(input("input x "))
            while x < 1 or x > self.n - 2:
                x = int(input("try more "))
            y = int(input("input y "))
            while y < 1 or y > self.n - 2:
                y = int(input("try more "))
            hp = int(input("input hp "))
            while hp < 1 or hp > 5:
                hp = int(input("try more "))
            male = str(input("input male "))
            while not male in males:
                male = str(input("try more "))
            age = int(input("input age "))
            while age < 1 or age > 5:
                age = int(input("try more "))
            ocean[x][y] = Shark(x, y, hp, male, age)

            return
        if choice == "k":
            x = int(input("input x "))
            while x < 1 or x > self.n - 2:
                x = int(input("try more "))
            y = int(input("input y "))
            while y < 1 or y > self.n - 2:
                y = int(input("try more "))
            hp = int(input("input hp "))
            while hp < 1 or hp > 6:
                hp = int(input("try more "))
            male = str(input("input male "))
            while not male in males:
                male = str(input("try more "))
            age = int(input("input age "))
            while age < 1 or age > 6:
                age = int(input("try more "))
            ocean[x][y] = Killerwhale(x, y, hp, male, age)
            return
        print("invalid letter")
    def killAnimal(self, ocean:[]) -> None:
        x = int(input("input x "))
        while x < 1 or x > self.n - 2:
            x = int(input("try more "))
        y = int(input("input y "))
        while y < 1 or y > self.n - 2:
            y = int(input("try more "))
        ocean[x][y] = Empty(x, y)
