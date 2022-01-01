from random import random

START_PHEROMONE = 1
MIN_PHEROMONE = START_PHEROMONE / 10


def findCostOrder(graph):
    size = len(graph)
    return sum(graph[i][j] if i != j else 0
               for j in range(size)
               for i in range(size)) / size


def getEdgeCoefs(graph):
    size = len(graph)

    eta = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j and graph[i][j]:
                eta[i][j] = 1 / graph[i][j]

    tau = [[START_PHEROMONE for j in range(size)] for i in range(size)]

    return eta, tau


def getProbNumerator(cFrom, cTo, vis, phero, alpha):
    return pow(phero[cFrom][cTo], alpha) * pow(vis[cFrom][cTo], 1 - alpha)


def getProbabilities(citiesNum, tabu, vis, phero, alpha):
    probabilities = [0] * citiesNum

    for city in range(citiesNum):
        if city not in tabu:
            curCity = tabu[-1]

            probabilities[city] = getProbNumerator(curCity, city, vis, phero,
                                                   alpha)

    denominator = sum(probabilities)

    for i in range(citiesNum):
        probabilities[i] /= denominator

    return probabilities


def chooseCity(tabuList, size, vis, phero, alpha):
    probabilities = getProbabilities(size, tabuList, vis, phero, alpha)

    choise = random()
    probSum = probabilities[0]
    nextCity = 0

    while choise > probSum and nextCity < size - 1:
        nextCity += 1
        probSum += probabilities[nextCity]

    return nextCity


def getAntTour(ant, graph, vis, phero, alpha):
    size = len(graph)

    while len(ant['tabu']) != size:
        nextCity = chooseCity(ant['tabu'], size, vis, phero, alpha)

        ant['cost'] += graph[ant['tabu'][-1]][nextCity]
        ant['tabu'].append(nextCity)

    ant['cost'] += graph[ant['tabu'][-1]][ant['tabu'][0]]
    ant['tabu'].append(ant['tabu'][0])

    return ant


def updatePheromones(phero, ants, Q, evarpolation):
    size = len(phero)

    addPhero = [[0 for i in range(size)] for j in range(size)]

    for ant in ants:
        delta = Q / ant['cost']
        for i in range(size - 1):
            addPhero[ant['tabu'][i]][ant['tabu'][i + 1]] += delta

    for i in range(size):
        for j in range(size):
            phero[i][j] *= (1 - evarpolation)
            phero[i][j] += addPhero[i][j]
            phero[i][j] = 0.1 if phero[i][j] < MIN_PHEROMONE else phero[i][j]


def salesman(graph, alpha, evarpolation, daysNum):
    num = len(graph)

    if num <= 1:
        return [0] if num else [], 0
    
    Q = findCostOrder(graph)
    vis, phero = getEdgeCoefs(graph)
    tour = []
    minCost = float("inf")

    for i in range(daysNum):
        ants = [{'tabu' : [j], 'cost' : 0} for j in range(num)]

        for j, ant in enumerate(ants):
            ants[j] = getAntTour(ant, graph, vis, phero, alpha)

            if ants[j]['cost'] < minCost:
                minCost = ants[j]['cost']
                tour = ants[j]['tabu']

        updatePheromones(phero, ants, Q, evarpolation)

    return tour, minCost
