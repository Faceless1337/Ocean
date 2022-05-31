from enum import Enum

import random


class AnimalsType(Enum):
    PLANKTON = 0
    DOLPHIN = 1
    SHARK = 2
    KILLERWHALE = 3
    EMPTY = 4


# ocean = np.empty((10, 10), dtype="object")


class Animals:
    def __init__(self, size: int):
        self.x: int = None
        self.y: int = None

    # self.n = size

    def getType(self) -> AnimalsType:
        pass

    def next(self, paramOcean) -> []:
        pass

    def getX(self) -> int:
        return self.x

    def getY(self) -> int:
        return self.y

    def getHp(self) -> int:
        return self.hp

    def getAge(self) -> int:
        return self.age

    def getSex(self) -> bool:
        return self.male

    def randomSex(self) -> bool:
        return random.choice([True, False])

    def sum(self, paramOcean: [], sm: []) -> None:

        if self.x == 1 and 1 < self.y < self.n - 2:
            for i in range(0, 2):
                for j in range(-1, 2):
                    # typE = paramOcean[self.x + i][self.y + j].getType()
                    sm[paramOcean[self.x + i][self.y + j].getType().value] += 1
            return

        if self.x == self.n - 2 and 1 < self.y < self.n - 2:
            for i in range(-1, 1):
                for j in range(-1, 2):
                    sm[paramOcean[self.x + i][self.y + j].getType().value] += 1
            return

        if 1 < self.x < self.n - 2 and 1 == self.y:
            for i in range(-1, 2):
                for j in range(0, 2):
                    sm[paramOcean[self.x + i][self.y + j].getType().value] += 1
            return

        if 1 < self.x < self.n - 2 and self.y == self.n - 2:
            for i in range(-1, 2):
                for j in range(-1, 1):
                    sm[paramOcean[self.x + i][self.y + j].getType().value] += 1
            return

        if self.x == 1 and self.y == 1:
            for i in range(0, 2):
                for j in range(0, 2):
                    # number = int(paramOcean[self.x + i][self.y + j].getType())
                    # type = paramOcean[self.x + i][self.y + j].getType()
                    sm[paramOcean[self.x + i][self.y + j].getType().value] += 1
            return
        if self.x == self.n - 2 and self.y == self.n - 2:
            for i in range(-1, 1):
                for j in range(-1, 1):
                    sm[paramOcean[self.x + i][self.y + j].getType().value] += 1
            return
        if self.x == self.n - 2 and self.y == 1:
            for i in range(-1, 1):
                for j in range(0, 2):
                    sm[paramOcean[self.x + i][self.y + j].getType().value] += 1
            return
        if self.x == 1 and self.y == self.n - 2:
            for i in range(0, 2):
                for j in range(-1, 1):
                    sm[paramOcean[self.x + i][self.y + j].getType().value] += 1
            return

    def position(self, ocean: [], needToFind: []):
        if self.x == 1 and 1 < self.y < self.n - 2:
            for i in range(0, 2):
                for j in range(-1, 2):
                    typeOfAnimal = ocean[self.x + i][self.y + j].getType().value
                    if needToFind[typeOfAnimal] == 1:
                        return [i, j]
        if self.x == self.n - 2 and 1 < self.y < self.n - 2:
            for i in range(-1, 1):
                for j in range(-1, 2):
                    typeOfAnimal = ocean[self.x + i][self.y + j].getType().value
                    if needToFind[typeOfAnimal] == 1:
                        return [i, j]

        if 1 < self.x < self.n - 2 and self.y == 1:
            for i in range(-1, 2):
                for j in range(0, 2):
                    typeOfAnimal = ocean[self.x + i][self.y + j].getType().value
                    if needToFind[typeOfAnimal] == 1:
                        return [i, j]

        if 1 < self.x < self.n - 2 and self.y == self.n - 2:
            for i in range(-1, 2):
                for j in range(-1, 1):
                    typeOfAnimal = ocean[self.x + i][self.y + j].getType().value
                    if needToFind[typeOfAnimal] == 1:
                        return [i, j]

        if self.x == 1 and self.y == 1:
            for i in range(0, 2):
                for j in range(0, 2):
                    typeOfAnimal = ocean[self.x + i][self.y + j].getType().value
                    if needToFind[typeOfAnimal] == 1:
                        return [i, j]

        if self.x == self.n - 2 and self.y == self.n - 2:
            for i in range(-1, 1):
                for j in range(-1, 1):
                    typeOfAnimal = ocean[self.x + i][self.y + j].getType().value
                    if needToFind[typeOfAnimal] == 1:
                        return [i, j]

        if self.x == self.n - 2 and self.y == 1:
            for i in range(-1, 1):
                for j in range(0, 2):
                    typeOfAnimal = ocean[self.x + i][self.y + j].getType().value
                    if needToFind[typeOfAnimal] == 1:
                        return [i, j]

        if self.x == 1 and self.y == self.n - 2:
            for i in range(0, 2):
                for j in range(-1, 1):
                    typeOfAnimal = ocean[self.x + i][self.y + j].getType().value
                    if needToFind[typeOfAnimal] == 1:
                        return [i, j]
