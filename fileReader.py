from animals import Empty
from animals import Plankton
from animals import Killerwhale
from animals import Shark
from animals import Dolphin
from living import Animals
import numpy as np


class FileReader:
    @classmethod
    def saveToFile(cls, ocean: [[]]) -> None:
        fout = open("state.txt", 'w')
        fout.write(str(len(ocean)) + '\n')
        for line in ocean:
            for animal in line:
                fout.write(str(animal.getType()) + '\n')
                if animal.getType() == Animals.plankton:
                    fout.write(str(animal.getX()) + '\n')
                    fout.write(str(animal.getY()) + '\n')
                    fout.write(str(animal.getHp()) + '\n')
                    fout.write(str(animal.getAge()) + '\n')
                    continue
                if animal.getType() == Animals.EMPTY:
                    fout.write(str(animal.getX()) + '\n')
                    fout.write(str(animal.getY()) + '\n')
                    continue
                fout.write(str(animal.getX()) + '\n')
                fout.write(str(animal.getY()) + '\n')
                fout.write(str(animal.getHp()) + '\n')
                if animal.getMale():
                    fout.write("male" + '\n')
                else:
                    fout.write("female" + '\n')
                fout.write(str(animal.getAge()) + '\n')
        fout.close()

    @classmethod
    def downloadFromFile(cls) -> [[]]:
        fin = open("state.txt", 'r')
        try:
            size: int = int(fin.readline())
            ocean = np.empty((size, size), dtype="object")
            for number in range(size * size):
                typeOfAnimal: str = str(fin.readline())
                x: int = int(fin.readline())
                y: int = int(fin.readline())
                if typeOfAnimal == "Animals.EMPTY" + '\n':
                    ocean[x][y] = Empty(x, y)
                    continue
                if typeOfAnimal == "Animals.plankton" + '\n':
                    hp: int = int(fin.readline())
                    age: int = int(fin.readline())
                    ocean[x][y] = Plankton(x, y, hp, age)
                    continue
                hp: int = int(fin.readline())
                strMale: str = str(fin.readline())
                male: bool = True
                if strMale == "female":
                    male = False
                age: int = int(fin.readline())
                if typeOfAnimal == "Animals.dolphin" + '\n':
                    ocean[x][y] = Dolphin(x, y, hp, male, age)
                    continue
                if typeOfAnimal == "Animals.shark" + '\n':
                    ocean[x][y] = Shark(x, y, hp, male, age)
                    continue
                if typeOfAnimal == "Animals.killerwhale" + '\n':
                    ocean[x][y] = Killerwhale(x, y, hp, male, age)
                    continue
            return ocean
        except ValueError:
            print("Invalid file")
            exit(0)
