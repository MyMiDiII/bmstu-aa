import csv


class Dictionary:
    def __init__(self, filename):
        self.keyName = ''
        self.keys = []
        self.values = []

        self.sortedKeys = []
        self.sortedValues = []

        self.segmMarkers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        self.segments = {}

        self.__load(filename)

    def __load(self, filename):
        types = [int, int, float]

        with open(filename, 'r') as file:
            reader = csv.reader(file)
            columnsNames = next(reader)
            self.keyName = columnsNames[0]

            for i, row in enumerate(reader):
                if row[0] not in self.keys:
                    self.keys.append(row[0])
                    curVal = {}

                    for j, val in enumerate(row[1:]):
                        curVal[columnsNames[j + 1]] = types[j](val)

                    self.values.append(curVal)

        self.__getSort()
        self.__getSegments()

    def __getSort(self):
        forSort = zip(self.keys, self.values)
        sortedDict = sorted(forSort, key=lambda el: el[0])
        self.sortedKeys = [el[0] for el in sortedDict]
        self.sortedValues = [el[1] for el in sortedDict]

    def __getSegments(self):
        freqVals = [[ch, 0] for ch in self.segmMarkers + '@']

        for key in self.keys:
            segMarker = key[0] if key[0] in self.segmMarkers else '@'
            for j, freq in enumerate(freqVals):
                if freq[0] == segMarker:
                    freqVals[j][1] += 1

        freqVals.sort(key=lambda el: el[1], reverse=True)

        self.segments = [(freqVal[0], {'keys':[], 'vals':[]})
                            for freqVal in freqVals]

        for i, key in enumerate(self.sortedKeys):
            segMarker = key[0] if key[0] in self.segmMarkers else '@'

            for j, segment in enumerate(self.segments):
                if segment[0] == segMarker:
                    self.segments[j][1]['keys'].append(key)
                    self.segments[j][1]['vals'].append(self.sortedValues[i])


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

    def __segBinSearch(self, segNum, name):
        compNum = 0
        keys = self.segments[segNum][1]['keys']
        vals = self.segments[segNum][1]['vals']

        iFrom, iTo, iMid = 0, len(keys), 0

        while iFrom <= iTo:
            iMid = (iFrom + iTo) // 2

            compNum += 1
            if name == keys[iMid]:
                return vals[iMid], compNum

            compNum += 1
            if name < keys[iMid]:
                iTo = iMid - 1
            else:
                iFrom = iMid + 1

        return None, compNum


    def segSearch(self, name):
        compNum = 0

        nameSeg = name[0] if name[0] in self.segmMarkers else '@'

        for i, segment in enumerate(self.segments):
            compNum += 1

            if nameSeg == segment[0]:
                vals, tmpCompNum = self.__segBinSearch(i, name)
                compNum += tmpCompNum

                return vals, compNum

        return None, compNum

    def getKeys(self):
        return self.keys

    def getVals(self):
        return self.values
