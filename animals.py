from living import Animals
from living import AnimalsType
import numpy as np
import random


class Dolphin(Animals):
    def __init__(self, row: int, column: int, HP: int, male: bool, age: int):
        self.x = row
        self.y = column
        self.hp = HP
        self.male = male
        self.age = age

    def getType(self) -> AnimalsType:
        return AnimalsType.DOLPHIN

    def death(self, ocean: []) -> []:
        if ocean[self.x][self.y].getHp() == 0 or ocean[self.x][self.y].getAge() == 4:
            return [FantomAnimal(self.x, self.y)]
        return []

    def giveLife(self, ocean: []) -> []:
        male: bool = False
        female: bool = False
        sm = np.zeros(5)
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        if ocean[self.x][self.y].getSex():
            male = True
        else:
            female = True
        self.sum(ocean, sm)
        if sm[AnimalsType.DOLPHIN.value] >= 2:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ocean[self.x + i][self.y + j].getType() == AnimalsType.DOLPHIN and ocean[self.x + i][
                        self.y + j].getSex():
                        male = True
                    if ocean[self.x + i][self.y + j].getType() == AnimalsType.DOLPHIN and ocean[self.x + i][
                        self.y + j].getSex() != True:
                        female = True
            if female and male:
                if sm[AnimalsType.EMPTY.value] > 0:
                    while ocean[self.x + tempX][
                        self.y + tempY].getType() != AnimalsType.EMPTY or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                        tempX = random.randrange(-1, 2)
                        tempY = random.randrange(-1, 2)

                    answer.append(Dolphin(self.x + tempX, self.y + tempY, 4, self.randomSex(), 0))
                    answer.append(
                        Dolphin(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getSex(),
                                ocean[self.x][self.y].getAge() + 1))
                    return answer
                if sm[AnimalsType.EMPTY.value] == 0:
                    if sm[AnimalsType.PLANKTON.value] > 0:
                        while ocean[self.x + tempX][
                            self.y + tempY].getType() != AnimalsType.PLANKTON or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                            tempX = random.randrange(-1, 2)
                            tempY = random.randrange(-1, 2)
                        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.PLANKTON:
                            answer.append(Dolphin(self.x + tempX, self.y + tempY, 4, self.randomSex(), 0))
                            answer.append(Dolphin(self.x, self.y, ocean[self.x][self.y].getHp() + 1,
                                                  ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
                            return answer
                    if sm[AnimalsType.PLANKTON.value] == 0:
                        answer.append(
                            Dolphin(self.x, self.y, ocean[self.x][self.y].getHp() + 2, ocean[self.x][self.y].getSex(),
                                    ocean[self.x][self.y].getAge() + 1))
                        return answer
        return []

    def moveAndEatSomebody(self, ocean: []) -> []:
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        while ocean[self.x + tempX][
            self.y + tempY].getType() == AnimalsType.DOLPHIN or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
            tempX = random.randrange(-1, 2)
            tempY = random.randrange(-1, 2)
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.EMPTY:
            answer.append(Dolphin(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() - 1,
                                  ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.PLANKTON:
            answer.append(Dolphin(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() + 1,
                                  ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.SHARK:
            answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 2,
                                ocean[self.x + tempX][self.y + tempY].getSex(),
                                ocean[self.x + tempX][self.y + tempY].getAge()))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.KILLERWHALE:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 2,
                                      ocean[self.x + tempX][self.y + tempY].getSex(),
                                      ocean[self.x + tempX][self.y + tempY].getAge()))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        answer.append(Dolphin(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getSex(),
                              ocean[self.x][self.y].getAge() + 1))
        return answer

    def next(self, ocean: []) -> []:
        answer = []
        answer = self.death(ocean)
        if answer:
            return answer
        answer = self.giveLife(ocean)
        if answer:
            return answer
        answer = self.moveAndEatSomebody(ocean)
        if answer:
            return answer


class FantomAnimal(Animals):
    def __init__(self, row: int, column: int):
        self.x = row
        self.y = column

    def getType(self) -> AnimalsType:
        return AnimalsType.EMPTY

    def next(self, ocean: [[]]) -> []:
        answer = []
        sm = np.zeros(5)
        self.sum(ocean, sm)
        if sm[AnimalsType.KILLERWHALE.value] >= 1:
            toFind = np.zeros(5)
            toFind[AnimalsType.DOLPHIN.value] = toFind[AnimalsType.PLANKTON.value] = toFind[AnimalsType.EMPTY.value] = toFind[
                AnimalsType.SHARK.value] = 0
            toFind[AnimalsType.KILLERWHALE.value] = 1
            coords: [] = self.position(ocean, toFind)
            tempX: int = coords[0]
            tempY: int = coords[1]
            answer.append(Killerwhale(self.x, self.y, ocean[self.x + tempX][self.y + tempY].getHp() - 1,
                                      ocean[self.x + tempX][self.y + tempY].getSex(),
                                      ocean[self.x + tempX][self.y + tempY].getAge() + 1))
            answer.append(FantomAnimal(self.x + tempX, self.y + tempY))
            return answer
        else:
            if sm[AnimalsType.SHARK.value] >= 1:
                toFind = np.zeros(5)
                toFind[AnimalsType.DOLPHIN.value] = toFind[AnimalsType.PLANKTON.value] = toFind[AnimalsType.EMPTY.value] = toFind[
                    AnimalsType.KILLERWHALE.value] = 0
                toFind[AnimalsType.SHARK.value] = 1
                coords: [] = self.position(ocean, toFind)
                tempX: int = coords[0]
                tempY: int = coords[1]
                answer.append(Shark(self.x, self.y, ocean[self.x + tempX][self.y + tempY].getHp() - 1,
                                    ocean[self.x + tempX][self.y + tempY].getSex(),
                                    ocean[self.x + tempX][self.y + tempY].getAge() + 1))
                answer.append(FantomAnimal(self.x + tempX, self.y + tempY))
                return answer

            else:
                if sm[AnimalsType.DOLPHIN.value] >= 1:
                    toFind = np.zeros(5)
                    toFind[AnimalsType.SHARK.value] = toFind[AnimalsType.PLANKTON.value] = toFind[AnimalsType.EMPTY.value] = toFind[
                        AnimalsType.KILLERWHALE.value] = 0
                    toFind[AnimalsType.DOLPHIN.value] = 1
                    coords: [] = self.position(ocean, toFind)
                    tempX: int = coords[0]
                    tempY: int = coords[1]
                    answer.append(Dolphin(self.x, self.y, ocean[self.x + tempX][self.y + tempY].getHp() - 1,
                                          ocean[self.x + tempX][self.y + tempY].getSex(),
                                          ocean[self.x + tempX][self.y + tempY].getAge() + 1))
                    answer.append(FantomAnimal(self.x + tempX, self.y + tempY))
                    return answer

                else:
                    if sm[AnimalsType.PLANKTON.value] >= 1:
                        toFind = np.zeros(5)
                        toFind[AnimalsType.DOLPHIN.value] = toFind[AnimalsType.KILLERWHALE.value] = toFind[
                            AnimalsType.EMPTY.value] = toFind[
                            AnimalsType.SHARK.value] = 0
                        toFind[AnimalsType.PLANKTON.value] = 1
                        coords: [] = self.position(ocean, toFind)
                        tempX: int = coords[0]
                        tempY: int = coords[1]
                        answer.append(Plankton(self.x, self.y, ocean[self.x + tempX][self.y + tempY].getHp() - 1,
                                               ocean[self.x + tempX][self.y + tempY].getAge() + 1))
                        answer.append(FantomAnimal(self.x + tempX, self.y + tempY))
                        return answer
        return [FantomAnimal(self.x, self.y)]


class Killerwhale(Animals):
    def __init__(self, row: int, column: int, HP: int, male: bool, age: int):
        self.x = row
        self.y = column
        self.hp = HP
        self.male = male
        self.age = age

    def getType(self) -> AnimalsType:
        return AnimalsType.KILLERWHALE

    def giveLife(self, ocean: []) -> []:
        male: bool = False
        female: bool = False
        sm = np.zeros(5)
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        if ocean[self.x][self.y].getSex():
            male = True
        else:
            female = True
        self.sum(ocean, sm)
        if sm[AnimalsType.KILLERWHALE.value] >= 2:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ocean[self.x + i][self.y + j].getType() == AnimalsType.KILLERWHALE and ocean[self.x + i][
                        self.y + j].getSex():
                        male = True
                    if ocean[self.x + i][self.y + j].getType() == AnimalsType.KILLERWHALE and ocean[self.x + i][
                        self.y + j].getSex() != True:
                        female = True
            if female and male:
                if sm[AnimalsType.EMPTY.value] > 0:
                    while ocean[self.x + tempX][
                        self.y + tempY].getType() != AnimalsType.EMPTY or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                        tempX = random.randrange(-1, 2)
                        tempY = random.randrange(-1, 2)

                    answer.append(Killerwhale(self.x + tempX, self.y + tempY, 6, self.randomSex(), 0))
                    answer.append(
                        Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getSex(),
                                    ocean[self.x][self.y].getAge() + 1))
                    return answer
                if sm[AnimalsType.EMPTY.value] == 0:
                    toFind = np.zeros(5)
                    if sm[AnimalsType.PLANKTON.value] + sm[AnimalsType.DOLPHIN.value] > 0:
                        while ocean[self.x + tempX][
                            self.y + tempY].getType() == AnimalsType.KILLERWHALE or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                            tempX = random.randrange(-1, 2)
                            tempY = random.randrange(-1, 2)
                        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.PLANKTON:
                            answer.append(Killerwhale(self.x + tempX, self.y + tempY, 6, self.randomSex(), 0))
                            answer.append(Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() + 1,
                                                      ocean[self.x][self.y].getSex(),
                                                      ocean[self.x][self.y].getAge() + 1))
                            return answer
                        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.DOLPHIN:
                            answer.append(Killerwhale(self.x + tempX, self.y + tempY, 6, self.randomSex(), 0))
                            answer.append(Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() + 2,
                                                      ocean[self.x][self.y].getSex(),
                                                      ocean[self.x][self.y].getAge() + 1))
                            return answer
                        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.SHARK:
                            answer.append(Killerwhale(self.x + tempX, self.y + tempY, 6, self.randomSex(), 0))
                            answer.append(Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() + 3,
                                                      ocean[self.x][self.y].getSex(),
                                                      ocean[self.x][self.y].getAge() + 1))
                            return answer
        return []

    def moveAndEatSomebody(self, ocean: []) -> []:
        sm = np.zeros(5)
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        self.sum(ocean, sm)
        while ocean[self.x + tempX][
            self.y + tempY].getType() == AnimalsType.KILLERWHALE or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
            tempX: int = random.randrange(-1, 2)
            tempY: int = random.randrange(-1, 2)
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.EMPTY:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() - 1,
                                      ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.PLANKTON:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() + 1,
                                      ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.DOLPHIN:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 2,
                                      ocean[self.x + tempX][self.y + tempY].getSex(),
                                      ocean[self.x + tempX][self.y + tempY].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.SHARK:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 3,
                                      ocean[self.x + tempX][self.y + tempY].getSex(),
                                      ocean[self.x + tempX][self.y + tempY].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        answer.append(Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getSex(),
                                  ocean[self.x][self.y].getAge() + 1))
        return answer

    def death(self, ocean: []) -> []:
        if ocean[self.x][self.y].getHp() == 0 or ocean[self.x][self.y].getAge() == 6:
            return [FantomAnimal(self.x, self.y)]

    def next(self, ocean: []) -> []:
        answer = []
        answer = self.death(ocean)
        if answer:
            return answer
        answer = self.giveLife(ocean)
        if answer:
            return answer
        answer = self.moveAndEatSomebody(ocean)
        if answer:
            return answer


class Plankton(Animals):
    def __init__(self, row: int, column: int, HP: int, age: int):
        self.x = row
        self.y = column
        self.hp = HP
        self.age = age

    def getType(self) -> AnimalsType:
        return AnimalsType.PLANKTON

    def giveLife(self, ocean: [[]]) -> []:
        sm = np.zeros(5)
        answer = []
        self.sum(ocean, sm)
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        if sm[AnimalsType.EMPTY.value] > 0:
            while ocean[self.x + tempX][
                self.y + tempY].getType() != AnimalsType.EMPTY or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
                tempX: int = random.randrange(-1, 2)
                tempY: int = random.randrange(-1, 2)
            if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.EMPTY:
                answer.append(Plankton(self.x + tempX, self.y + tempY, 2, 0))
                answer.append(
                    Plankton(self.x, self.y, ocean[self.x][self.y].getHp(), ocean[self.x][self.y].getAge() + 1))
                return answer
        return []

    def move(self, ocean: [[]]) -> []:
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        while self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
            tempX: int = random.randrange(-1, 2)
            tempY: int = random.randrange(-1, 2)
        if ocean[self.x + tempX][self.y + tempY].getType() != AnimalsType.EMPTY:
            if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.DOLPHIN:
                answer.append(Dolphin(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 1,
                                      ocean[self.x + tempX][self.y + tempY].getSex(),
                                      ocean[self.x + tempX][self.y + tempY].getAge()))
            if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.SHARK:
                answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 1,
                                    ocean[self.x + tempX][self.y + tempY].getSex(),
                                    ocean[self.x + tempX][self.y + tempY].getAge()))
            if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.KILLERWHALE:
                answer.append(
                    Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 1,
                                ocean[self.x + tempX][self.y + tempY].getSex(),
                                ocean[self.x + tempX][self.y + tempY].getAge()))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        answer.append(FantomAnimal(self.x, self.y))
        return answer

    def death(self, ocean: [[]]) -> []:
        if ocean[self.x][self.y].getAge() == 2 or ocean[self.x][self.y].getHp() == 0:
            return [FantomAnimal(self.x, self.y)]
        return []

    def next(self, ocean: [[]]) -> []:
        answer = []
        answer = self.death(ocean)
        if answer:
            return answer
        answer = self.giveLife(ocean)
        if answer:
            return answer
        answer = self.move(ocean)
        if answer:
            return answer


class Shark(Animals):
    def __init__(self, row: int, column: int, HP: int, male: bool, age: int):
        self.x = row
        self.y = column
        self.hp = HP
        self.male = male
        self.age = age

    def getType(self) -> AnimalsType:
        return AnimalsType.SHARK

    def giveLife(self, ocean: []) -> []:
        male: bool = False
        female: bool = False
        sm = np.zeros(5)
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        if ocean[self.x][self.y].getSex():
            male = True
        else:
            female = True
        Animals.sum(self, ocean, sm)
        if sm[AnimalsType.SHARK.value] >= 2:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ocean[self.x + i][self.y + j].getType() == AnimalsType.SHARK and ocean[self.x + i][
                        self.y + j].getSex():
                        male = True
                    if ocean[self.x + i][self.y + j].getType() == AnimalsType.SHARK and ocean[self.x + i][
                        self.y + j].getSex() != True:
                        female = True
            if female and male:
                if sm[AnimalsType.EMPTY.value] > 0:
                    while ocean[self.x + tempX][
                        self.y + tempY].getType() != AnimalsType.EMPTY or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                        tempX = random.randrange(-1, 2)
                        tempY = random.randrange(-1, 2)
                    answer.append(Shark(self.x + tempX, self.y + tempY, 5, self.randomSex(), 0))
                    answer.append(
                        Shark(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getSex(),
                              ocean[self.x][self.y].getAge() + 1))
                    return answer
                if sm[AnimalsType.EMPTY.value] == 0:
                    toFind = np.zeros(5)
                    if sm[AnimalsType.PLANKTON.value] + sm[AnimalsType.DOLPHIN.value] > 0:
                        while ocean[self.x + tempX][
                            self.y + tempY].getType() == AnimalsType.KILLERWHALE or ocean[self.x + tempX][
                            self.y + tempY].getType() == AnimalsType.SHARK or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                            tempX = random.randrange(-1, 2)
                            tempY = random.randrange(-1, 2)
                        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.PLANKTON:
                            answer.append(Shark(self.x + tempX, self.y + tempY, 5, self.randomSex(), 0))
                            answer.append(Shark(self.x, self.y, ocean[self.x][self.y].getHp() + 1,
                                                ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
                            return answer
                        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.DOLPHIN:
                            answer.append(Shark(self.x + tempX, self.y + tempY, 5, Animals.randomSex(), 0))
                            answer.append(Shark(self.x, self.y, ocean[self.x][self.y].getHp() + 2,
                                                ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
                            return answer
                    if sm[AnimalsType.PLANKTON.value] + sm[AnimalsType.DOLPHIN.value] == 0:
                        answer.append(
                            Shark(self.x, self.y, ocean[self.x][self.y].getHp() + 3, ocean[self.x][self.y].getSex(),
                                  ocean[self.x][self.y].getAge() + 1))
                        return answer
        return []

    def moveAndEatSomebody(self, ocean: []) -> []:
        sm = np.zeros(5)
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        self.sum(ocean, sm)
        while ocean[self.x + tempX][
            self.y + tempY].getType() == AnimalsType.SHARK or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
            tempX = random.randrange(-1, 2)
            tempY = random.randrange(-1, 2)
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.EMPTY:
            answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() - 1,
                                ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.PLANKTON:
            answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() + 1,
                                ocean[self.x][self.y].getSex(), ocean[self.x][self.y].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.DOLPHIN:
            answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 2,
                                ocean[self.x + tempX][self.y + tempY].getSex(),
                                ocean[self.x + tempX][self.y + tempY].getAge() + 1))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == AnimalsType.KILLERWHALE:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 3,
                                      ocean[self.x + tempX][self.y + tempY].getSex(),
                                      ocean[self.x + tempX][self.y + tempY].getAge()))
            answer.append(FantomAnimal(self.x, self.y))
            return answer
        answer.append(Shark(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getSex(),
                            ocean[self.x][self.y].getAge() + 1))
        return answer

    def death(self, ocean: []) -> []:
        if ocean[self.x][self.y].getHp() == 0 or ocean[self.x][self.y].getAge() == 5:
            return [FantomAnimal(self.x, self.y)]
        return []

    def next(self, ocean: []) -> []:
        answer = []
        answer = self.death(ocean)
        if answer:
            return answer
        answer = self.giveLife(ocean)
        if answer:
            return answer
        answer = self.moveAndEatSomebody(ocean)
        if answer:
            return answer
