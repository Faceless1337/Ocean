from living import Living
import numpy as np
from god import God
from fileReader import FileReader

try:
    print("1 - manual modeling")
    print("2 - automatic modeling")
    print("3 - download state from file")
    choice: int = int(input())
    if choice == 1:
        size: int = int(input("input size ")) + 2
        if size < 1:
            print("invalid size")
            exit(0)
        amountOfPlanktons: int = int(input("input amount of planktons "))
        amountOfDolphins: int = int(input("input amount of dolphins "))
        amountOfSharks: int = int(input("input amount of sharks "))
        amountOfKillerwhales: int = int(input("input amount of killerwales "))
        if amountOfSharks + amountOfKillerwhales + amountOfDolphins + amountOfPlanktons > size * size:
            print("too much animals")
            exit(0)
        ocean = np.empty((size, size), dtype="object")
        setattr(Living, 'n', size)
        god = God(size)
        god.init(ocean, amountOfPlanktons, amountOfDolphins, amountOfSharks, amountOfKillerwhales)
    if choice == 2:
        ocean = np.empty((11, 11), dtype="object")
        setattr(Living, 'n', 11)
        god = God(11)
        god.init(ocean, 20, 10, 5, 5)
    if choice == 3:
        ocean = FileReader.downloadFromFile()
        god = God(len(ocean))
        setattr(Living, 'n', len(ocean))
    god.showOcean(ocean)
    stepNumber: int = 1
    choice: int = 1
    while True:
        print("1 - exit")
        print("2 - next step")
        print("3 - add animal")
        print("4 - kill animal")
        print("5 - save state to file")
        choice = int(input())
        if choice == 1:
            break
        if choice == 2:
            god.update(ocean)
            god.showOcean(ocean)
            print("number of the step - ", stepNumber)
            stepNumber += 1
        if choice == 3:
            god.addAnimal(ocean)
            god.showOcean(ocean)
        if choice == 4:
            god.killAnimal(ocean)
            god.showOcean(ocean)
        if choice == 5:
            FileReader.saveToFile(ocean)
except Exception:
    print("Invalid information")
    exit(0)
