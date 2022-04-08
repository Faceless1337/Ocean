from living import Living
from living import Animals
import numpy as np
import random


class Dolphin(Living):
    def __init__(self, row: int, column: int, HP: int, male: bool, age: int):
        self.x = row
        self.y = column
        self.hp = HP
        self.male = male
        self.age = age

    def getType(self) -> Animals:
        return Animals.dolphin

    def death(self, ocean: []) -> []:
        if ocean[self.x][self.y].getHp() == 0 or ocean[self.x][self.y].getAge() == 4:
            return [Empty(self.x, self.y)]
        return []

    def giveLife(self, ocean: []) -> []:
        male: bool = False
        female: bool = False
        sm = np.zeros(5)
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        if ocean[self.x][self.y].getMale():
            male = True
        else:
            female = True
        self.sum(ocean, sm)
        if sm[Animals.dolphin.value] >= 2:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ocean[self.x + i][self.y + j].getType() == Animals.dolphin and ocean[self.x + i][
                        self.y + j].getMale():
                        male = True
                    if ocean[self.x + i][self.y + j].getType() == Animals.dolphin and ocean[self.x + i][
                        self.y + j].getMale() != True:
                        female = True
            if female and male:
                if sm[Animals.EMPTY.value] > 0:
                    while ocean[self.x + tempX][
                        self.y + tempY].getType() != Animals.EMPTY or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                        tempX = random.randrange(-1, 2)
                        tempY = random.randrange(-1, 2)

                    answer.append(Dolphin(self.x + tempX, self.y + tempY, 4, self.randomMale(), 0))
                    answer.append(
                        Dolphin(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getMale(),
                                ocean[self.x][self.y].getAge() + 1))
                    return answer
                if sm[Animals.EMPTY.value] == 0:
                    if sm[Animals.plankton.value] > 0:
                        while ocean[self.x + tempX][
                            self.y + tempY].getType() != Animals.plankton or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                            tempX = random.randrange(-1, 2)
                            tempY = random.randrange(-1, 2)
                        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.plankton:
                            answer.append(Dolphin(self.x + tempX, self.y + tempY, 4, self.randomMale(), 0))
                            answer.append(Dolphin(self.x, self.y, ocean[self.x][self.y].getHp() + 1,
                                                  ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
                            return answer
                    if sm[Animals.plankton.value] == 0:
                        answer.append(
                            Dolphin(self.x, self.y, ocean[self.x][self.y].getHp() + 2, ocean[self.x][self.y].getMale(),
                                    ocean[self.x][self.y].getAge() + 1))
                        return answer
        return []

    def moveAndEatSomebody(self, ocean: []) -> []:
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        while ocean[self.x + tempX][
            self.y + tempY].getType() == Animals.dolphin or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
            tempX = random.randrange(-1, 2)
            tempY = random.randrange(-1, 2)
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.EMPTY:
            answer.append(Dolphin(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() - 1,
                                  ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.plankton:
            answer.append(Dolphin(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() + 1,
                                  ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.shark:
            answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 2,
                                ocean[self.x + tempX][self.y + tempY].getMale(),
                                ocean[self.x + tempX][self.y + tempY].getAge()))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.killerwhale:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 2,
                                      ocean[self.x + tempX][self.y + tempY].getMale(),
                                      ocean[self.x + tempX][self.y + tempY].getAge()))
            answer.append(Empty(self.x, self.y))
            return answer
        answer.append(Dolphin(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getMale(),
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


class Empty(Living):
    def __init__(self, row: int, column: int):
        self.x = row
        self.y = column

    def getType(self) -> Animals:
        return Animals.EMPTY

    def next(self, ocean: [[]]) -> []:
        answer = []
        sm = np.zeros(5)
        self.sum(ocean, sm)
        if sm[Animals.killerwhale.value] >= 1:
            toFind = np.zeros(5)
            toFind[Animals.dolphin.value] = toFind[Animals.plankton.value] = toFind[Animals.EMPTY.value] = toFind[
                Animals.shark.value] = 0
            toFind[Animals.killerwhale.value] = 1
            coords: [] = self.position(ocean, toFind)
            tempX: int = coords[0]
            tempY: int = coords[1]
            answer.append(Killerwhale(self.x, self.y, ocean[self.x + tempX][self.y + tempY].getHp() - 1,
                                      ocean[self.x + tempX][self.y + tempY].getMale(),
                                      ocean[self.x + tempX][self.y + tempY].getAge() + 1))
            answer.append(Empty(self.x + tempX, self.y + tempY))
            return answer
        else:
            if sm[Animals.shark.value] >= 1:
                toFind = np.zeros(5)
                toFind[Animals.dolphin.value] = toFind[Animals.plankton.value] = toFind[Animals.EMPTY.value] = toFind[
                    Animals.killerwhale.value] = 0
                toFind[Animals.shark.value] = 1
                coords: [] = self.position(ocean, toFind)
                tempX: int = coords[0]
                tempY: int = coords[1]
                answer.append(Shark(self.x, self.y, ocean[self.x + tempX][self.y + tempY].getHp() - 1,
                                    ocean[self.x + tempX][self.y + tempY].getMale(),
                                    ocean[self.x + tempX][self.y + tempY].getAge() + 1))
                answer.append(Empty(self.x + tempX, self.y + tempY))
                return answer

            else:
                if sm[Animals.dolphin.value] >= 1:
                    toFind = np.zeros(5)
                    toFind[Animals.shark.value] = toFind[Animals.plankton.value] = toFind[Animals.EMPTY.value] = toFind[
                        Animals.killerwhale.value] = 0
                    toFind[Animals.dolphin.value] = 1
                    coords: [] = self.position(ocean, toFind)
                    tempX: int = coords[0]
                    tempY: int = coords[1]
                    answer.append(Dolphin(self.x, self.y, ocean[self.x + tempX][self.y + tempY].getHp() - 1,
                                          ocean[self.x + tempX][self.y + tempY].getMale(),
                                          ocean[self.x + tempX][self.y + tempY].getAge() + 1))
                    answer.append(Empty(self.x + tempX, self.y + tempY))
                    return answer

                else:
                    if sm[Animals.plankton.value] >= 1:
                        toFind = np.zeros(5)
                        toFind[Animals.dolphin.value] = toFind[Animals.killerwhale.value] = toFind[
                            Animals.EMPTY.value] = toFind[
                            Animals.shark.value] = 0
                        toFind[Animals.plankton.value] = 1
                        coords: [] = self.position(ocean, toFind)
                        tempX: int = coords[0]
                        tempY: int = coords[1]
                        answer.append(Plankton(self.x, self.y, ocean[self.x + tempX][self.y + tempY].getHp() - 1,
                                               ocean[self.x + tempX][self.y + tempY].getAge() + 1))
                        answer.append(Empty(self.x + tempX, self.y + tempY))
                        return answer
        return [Empty(self.x, self.y)]


class Killerwhale(Living):
    def __init__(self, row: int, column: int, HP: int, male: bool, age: int):
        self.x = row
        self.y = column
        self.hp = HP
        self.male = male
        self.age = age

    def getType(self) -> Animals:
        return Animals.killerwhale

    def giveLife(self, ocean: []) -> []:
        male: bool = False
        female: bool = False
        sm = np.zeros(5)
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        if ocean[self.x][self.y].getMale():
            male = True
        else:
            female = True
        self.sum(ocean, sm)
        if sm[Animals.killerwhale.value] >= 2:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ocean[self.x + i][self.y + j].getType() == Animals.killerwhale and ocean[self.x + i][
                        self.y + j].getMale():
                        male = True
                    if ocean[self.x + i][self.y + j].getType() == Animals.killerwhale and ocean[self.x + i][
                        self.y + j].getMale() != True:
                        female = True
            if female and male:
                if sm[Animals.EMPTY.value] > 0:
                    while ocean[self.x + tempX][
                        self.y + tempY].getType() != Animals.EMPTY or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                        tempX = random.randrange(-1, 2)
                        tempY = random.randrange(-1, 2)

                    answer.append(Killerwhale(self.x + tempX, self.y + tempY, 6, self.randomMale(), 0))
                    answer.append(
                        Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getMale(),
                                    ocean[self.x][self.y].getAge() + 1))
                    return answer
                if sm[Animals.EMPTY.value] == 0:
                    toFind = np.zeros(5)
                    if sm[Animals.plankton.value] + sm[Animals.dolphin.value] > 0:
                        while ocean[self.x + tempX][
                            self.y + tempY].getType() == Animals.killerwhale or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                            tempX = random.randrange(-1, 2)
                            tempY = random.randrange(-1, 2)
                        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.plankton:
                            answer.append(Killerwhale(self.x + tempX, self.y + tempY, 6, self.randomMale(), 0))
                            answer.append(Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() + 1,
                                                      ocean[self.x][self.y].getMale(),
                                                      ocean[self.x][self.y].getAge() + 1))
                            return answer
                        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.dolphin:
                            answer.append(Killerwhale(self.x + tempX, self.y + tempY, 6, self.randomMale(), 0))
                            answer.append(Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() + 2,
                                                      ocean[self.x][self.y].getMale(),
                                                      ocean[self.x][self.y].getAge() + 1))
                            return answer
                        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.shark:
                            answer.append(Killerwhale(self.x + tempX, self.y + tempY, 6, self.randomMale(), 0))
                            answer.append(Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() + 3,
                                                      ocean[self.x][self.y].getMale(),
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
            self.y + tempY].getType() == Animals.killerwhale or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
            tempX: int = random.randrange(-1, 2)
            tempY: int = random.randrange(-1, 2)
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.EMPTY:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() - 1,
                                      ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.plankton:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() + 1,
                                      ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.dolphin:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 2,
                                      ocean[self.x + tempX][self.y + tempY].getMale(),
                                      ocean[self.x + tempX][self.y + tempY].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.shark:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 3,
                                      ocean[self.x + tempX][self.y + tempY].getMale(),
                                      ocean[self.x + tempX][self.y + tempY].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        answer.append(Killerwhale(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getMale(),
                                  ocean[self.x][self.y].getAge() + 1))
        return answer

    def death(self, ocean: []) -> []:
        if ocean[self.x][self.y].getHp() == 0 or ocean[self.x][self.y].getAge() == 6:
            return [Empty(self.x, self.y)]

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


class Plankton(Living):
    def __init__(self, row: int, column: int, HP: int, age: int):
        self.x = row
        self.y = column
        self.hp = HP
        self.age = age

    def getType(self) -> Animals:
        return Animals.plankton

    def giveLife(self, ocean: [[]]) -> []:
        sm = np.zeros(5)
        answer = []
        self.sum(ocean, sm)
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        if sm[Animals.EMPTY.value] > 0:
            while ocean[self.x + tempX][
                self.y + tempY].getType() != Animals.EMPTY or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
                tempX: int = random.randrange(-1, 2)
                tempY: int = random.randrange(-1, 2)
            if ocean[self.x + tempX][self.y + tempY].getType() == Animals.EMPTY:
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
        if ocean[self.x + tempX][self.y + tempY].getType() != Animals.EMPTY:
            if ocean[self.x + tempX][self.y + tempY].getType() == Animals.dolphin:
                answer.append(Dolphin(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 1,
                                      ocean[self.x + tempX][self.y + tempY].getMale(),
                                      ocean[self.x + tempX][self.y + tempY].getAge()))
            if ocean[self.x + tempX][self.y + tempY].getType() == Animals.shark:
                answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 1,
                                    ocean[self.x + tempX][self.y + tempY].getMale(),
                                    ocean[self.x + tempX][self.y + tempY].getAge()))
            if ocean[self.x + tempX][self.y + tempY].getType() == Animals.killerwhale:
                answer.append(
                    Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 1,
                                ocean[self.x + tempX][self.y + tempY].getMale(),
                                ocean[self.x + tempX][self.y + tempY].getAge()))
            answer.append(Empty(self.x, self.y))
            return answer
        answer.append(Empty(self.x, self.y))
        return answer

    def death(self, ocean: [[]]) -> []:
        if ocean[self.x][self.y].getAge() == 2 or ocean[self.x][self.y].getHp() == 0:
            return [Empty(self.x, self.y)]
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


class Shark(Living):
    def __init__(self, row: int, column: int, HP: int, male: bool, age: int):
        self.x = row
        self.y = column
        self.hp = HP
        self.male = male
        self.age = age

    def getType(self) -> Animals:
        return Animals.shark

    def giveLife(self, ocean: []) -> []:
        male: bool = False
        female: bool = False
        sm = np.zeros(5)
        answer = []
        tempX: int = random.randrange(-1, 2)
        tempY: int = random.randrange(-1, 2)
        if ocean[self.x][self.y].getMale():
            male = True
        else:
            female = True
        Living.sum(self, ocean, sm)
        if sm[Animals.shark.value] >= 2:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ocean[self.x + i][self.y + j].getType() == Animals.shark and ocean[self.x + i][
                        self.y + j].getMale():
                        male = True
                    if ocean[self.x + i][self.y + j].getType() == Animals.shark and ocean[self.x + i][
                        self.y + j].getMale() != True:
                        female = True
            if female and male:
                if sm[Animals.EMPTY.value] > 0:
                    while ocean[self.x + tempX][
                        self.y + tempY].getType() != Animals.EMPTY or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                        tempX = random.randrange(-1, 2)
                        tempY = random.randrange(-1, 2)
                    answer.append(Shark(self.x + tempX, self.y + tempY, 5, self.randomMale(), 0))
                    answer.append(
                        Shark(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getMale(),
                              ocean[self.x][self.y].getAge() + 1))
                    return answer
                if sm[Animals.EMPTY.value] == 0:
                    toFind = np.zeros(5)
                    if sm[Animals.plankton.value] + sm[Animals.dolphin.value] > 0:
                        while ocean[self.x + tempX][
                            self.y + tempY].getType() == Animals.killerwhale or ocean[self.x + tempX][
                            self.y + tempY].getType() == Animals.shark or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == 0 or self.y + tempY == self.n - 1:
                            tempX = random.randrange(-1, 2)
                            tempY = random.randrange(-1, 2)
                        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.plankton:
                            answer.append(Shark(self.x + tempX, self.y + tempY, 5, self.randomMale(), 0))
                            answer.append(Shark(self.x, self.y, ocean[self.x][self.y].getHp() + 1,
                                                ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
                            return answer
                        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.dolphin:
                            answer.append(Shark(self.x + tempX, self.y + tempY, 5, Living.randomMale(), 0))
                            answer.append(Shark(self.x, self.y, ocean[self.x][self.y].getHp() + 2,
                                                ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
                            return answer
                    if sm[Animals.plankton.value] + sm[Animals.dolphin.value] == 0:
                        answer.append(
                            Shark(self.x, self.y, ocean[self.x][self.y].getHp() + 3, ocean[self.x][self.y].getMale(),
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
            self.y + tempY].getType() == Animals.shark or self.x + tempX == 0 or self.x + tempX == self.n - 1 or self.y + tempY == self.n - 1 or self.y + tempY == 0:
            tempX = random.randrange(-1, 2)
            tempY = random.randrange(-1, 2)
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.EMPTY:
            answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() - 1,
                                ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.plankton:
            answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x][self.y].getHp() + 1,
                                ocean[self.x][self.y].getMale(), ocean[self.x][self.y].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.dolphin:
            answer.append(Shark(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 2,
                                ocean[self.x + tempX][self.y + tempY].getMale(),
                                ocean[self.x + tempX][self.y + tempY].getAge() + 1))
            answer.append(Empty(self.x, self.y))
            return answer
        if ocean[self.x + tempX][self.y + tempY].getType() == Animals.killerwhale:
            answer.append(Killerwhale(self.x + tempX, self.y + tempY, ocean[self.x + tempX][self.y + tempY].getHp() + 3,
                                      ocean[self.x + tempX][self.y + tempY].getMale(),
                                      ocean[self.x + tempX][self.y + tempY].getAge()))
            answer.append(Empty(self.x, self.y))
            return answer
        answer.append(Shark(self.x, self.y, ocean[self.x][self.y].getHp() - 1, ocean[self.x][self.y].getMale(),
                            ocean[self.x][self.y].getAge() + 1))
        return answer

    def death(self, ocean: []) -> []:
        if ocean[self.x][self.y].getHp() == 0 or ocean[self.x][self.y].getAge() == 5:
            return [Empty(self.x, self.y)]
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
