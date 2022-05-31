from living import Animals
import numpy as np
from oceanController import OceanController
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
        setattr(Animals, 'n', size)
        oceanController = OceanController(size)
        oceanController.init(ocean, amountOfPlanktons, amountOfDolphins, amountOfSharks, amountOfKillerwhales)
    if choice == 2:
        ocean = np.empty((11, 11), dtype="object")
        setattr(Animals, 'n', 11)
        oceanController = OceanController(11)
        oceanController.init(ocean, 20, 10, 5, 5)
    if choice == 3:
        ocean = FileReader.loadFromFile()
        oceanController = OceanController(len(ocean))
        setattr(Animals, 'n', len(ocean))
    oceanController.showOcean(ocean)
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
            oceanController.update(ocean)
            oceanController.showOcean(ocean)
            print("number of the step - ", stepNumber)
            stepNumber += 1
        if choice == 3:
            oceanController.addAnimal(ocean)
            oceanController.showOcean(ocean)
        if choice == 4:
            oceanController.killAnimal(ocean)
            oceanController.showOcean(ocean)
        if choice == 5:
            FileReader.saveToFile(ocean)
except Exception:
    print("Invalid information")
    exit(0)
