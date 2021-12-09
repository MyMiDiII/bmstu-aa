from itertools import permutations

def getTourCost(tour, graph):
    cost = 0

    for i in range(len(tour) - 1):
        cost += graph[tour[i]][tour[i + 1]]

    return cost


def salesman(graph):
    if len(graph) > 10:
        return ()
    tour = []
    minCost = float("inf")

    for perm in permutations(list(range(len(graph)))):
        curTour = list(perm)
        curTour.append(perm[0])

        curCost = getTourCost(curTour, graph) 

        if curCost < minCost:
            tour = curTour
            minCost = curCost

    return tour, minCost
