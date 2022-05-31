from animals import FantomAnimal
from animals import Plankton
from animals import Killerwhale
from animals import Shark
from animals import Dolphin
from living import AnimalsType
import numpy as np
import json

class FileReader:
    @classmethod
    def saveToFile(cls, ocean: [[]]) -> None:
        fout = open('size.txt', 'w')
        fout.write(str(len(ocean)))
        fout.close()
        data = {'Plankton': [], 'Shark': [], 'FantomAnimal': [], 'Killerwhale': [], 'Dolphin': []}
        for line in ocean:
            for animal in line:
                if animal.getType() == AnimalsType.PLANKTON:
                    data['Plankton'].append(animal.__dict__)
                if animal.getType() == AnimalsType.EMPTY:
                    data['FantomAnimal'].append(animal.__dict__)
                if animal.getType() == AnimalsType.DOLPHIN:
                    data['Dolphin'].append(animal.__dict__)
                if animal.getType() == AnimalsType.SHARK:
                    data['Shark'].append(animal.__dict__)
                if animal.getType() == AnimalsType.KILLERWHALE:
                    data['Killerwhale'].append(animal.__dict__)

        with open('state.json', 'w') as outfile:
            json.dump(data, outfile)



    @classmethod
    def loadFromFile(cls) -> [[]]:
        fin = open("size.txt", 'r')
        try:
            size: int = int(fin.readline())
            fin.close()
            ocean = np.empty((size, size), dtype="object")

            with open('state.json') as infile:
                data = json.load(infile)
                for plankton in data['Plankton']:
                    ocean[plankton['x']][plankton['y']] = Plankton(plankton['x'], plankton['y'], plankton['hp'], plankton['age'])
                for fantomAnimal in data['FantomAnimal']:
                    ocean[fantomAnimal['x']][fantomAnimal['y']] = FantomAnimal(fantomAnimal['x'], fantomAnimal['y'])
                for dolphin in data['Dolphin']:
                    ocean[dolphin['x']][dolphin['y']] = Dolphin(dolphin['x'], dolphin['y'], dolphin['hp'], dolphin['male'], dolphin['age'])
                for shark in data['Shark']:
                    ocean[shark['x']][shark['y']] = Shark(shark['x'], shark['y'], shark['hp'], shark['male'], shark['age'])
                for killerwhale in data['Killerwhale']:
                    ocean[killerwhale['x']][killerwhale['y']] = Killerwhale(killerwhale['x'], killerwhale['y'], killerwhale['hp'], killerwhale['male'], killerwhale['age'])
            return ocean
        except ValueError:
            print("Invalid file")
            exit(0)
