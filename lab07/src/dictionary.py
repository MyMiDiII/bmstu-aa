import csv

#from prettytable import PrettyTable
#
#class Values:
#    def __init(self, dictionary):
#        self.dictionary = dictionary
#
#    def __str__(self):
#        table = PrettyTable()
#        table.field_names = dictionary.keys()

class Dictionary:
    def __init__(self, filename):
        self.keyName = ''
        self.keys = []
        self.values = []

        self.sortedKeys = []
        self.sortedValues = []

        self.__load(filename)

    def __load(self, filename):
        types = [int, int, float]

        with open(filename, 'r') as file:
            reader = csv.reader(file)
            columnsNames = next(reader)
            self.keyName = columnsNames[0]

            for i, row in enumerate(reader):
                #if row[0] not in self.keys:
                self.keys.append(row[0])
                curVal = {}

                for j, val in enumerate(row[1:]):
                    curVal[columnsNames[j + 1]] = types[j](val)

                self.values.append(curVal)

        forSort = zip(self.keys, self.values)
        sortedDict = sorted(forSort, key=lambda el: el[0])
        self.sortedKeys = [el[0] for el in sortedDict]
        self.sortedValues = [el[1] for el in sortedDict]

    def __str__(self):
        for key, val in zip(self.keys, self.values):
            print(key, ":", val)
        return ""

    def bruteForce(self, name):
        compNum = 0

        for i, key in enumerate(self.keys):
            compNum += 1

            if key == name:
                return self.values[i], compNum

        return None, compNum

    def binSearch(self, name):
        compNum = 0

        iFrom, iTo, iMid = 0, len(self.keys), 0

        while iFrom <= iTo:
            iMid = (iFrom + iTo) // 2

            compNum += 1
            if name == self.sortedKeys[iMid]:
                return self.sortedValues[iMid], compNum

            compNum += 1
            if name < self.sortedKeys[iMid]:
                iTo = iMid - 1
            else:
                iFrom = iMid + 1

        return None, compNum


