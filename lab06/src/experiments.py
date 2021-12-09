import random
import time
import csv

import brute_force
import ants

def getGraph(size, dFrom, dTo):
    matrix = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            if (i == j):
                num = 0
            else:
                num = random.randint(dFrom, dTo)

            matrix[i][j] = num

    return matrix


def getTime(arg1, args, func, num):
    avgTime = 0

    print("Подсчет для функции", func.__name__)
    for i in range(num):
        start = time.process_time_ns()
        func(arg1, *args)
        avgTime += time.process_time_ns() - start

    avgTime = avgTime / num

    return int(avgTime)


def getTimes(funcs, args, sizes):
    times = [[] for x in range(len(funcs))]

    print("\nИдет подсчет времени. Пожалуйста, подождите...")
    for size in sizes:
        print("Подсчет для графа с количеством вершин =  %d" % (size))
        graph = getGraph(size, 1, 10)

        for i, func in enumerate(funcs):
            funcTime = getTime(graph, args[i], func, 10)
            times[i].append(funcTime)

    return times

def addParamsRow(alpha, evarpolation, daysNum, mistake, file):
    writer = csv.writer(file, delimiter=',')
    writer.writerow([alpha, evarpolation, daysNum, int(mistake)])


def parametrization():
    alphas = [num / 10 for num in range(0, 11)]
    evarpolations = [num / 10 for num in range(0, 11)]
    daysNums = [1, 5, 10, 50, 100, 500, 1000]

    size = 9

    with open('./data/lowGraph.txt', 'r') as file:
        graphLow = [[float(cost) for cost in row.split()] for row in file]

    with open('./data/highGraph.txt', 'r') as file:
        graphHigh = [[float(cost) for cost in row.split()] for row in file]

    _, trueLowCost = brute_force.salesman(graphLow)
    _, trueHighCost = brute_force.salesman(graphHigh)

    low = open('../docs/data/csv/lowParam.csv', 'w', newline='')
    high = open('../docs/data/csv/highParam.csv', 'w', newline='')

    for alpha in alphas:
        beta = 1 - alpha

        for evarpolation in evarpolations:
            for daysNum in daysNums:
                print(("Подчет результатов для alpha = %f, evarpolation = %f,"
                      + "days = %d") % (alpha, evarpolation, daysNum))
                _, resLow = ants.salesman(graphLow, alpha, evarpolation, daysNum)
                _, resHigh = ants.salesman(graphHigh, alpha, evarpolation,
                                        daysNum)
                addParamsRow(alpha, evarpolation, daysNum,
                             round(abs(resLow - trueLowCost)), low)
                addParamsRow(alpha, evarpolation, daysNum,
                             round(abs(resHigh - trueHighCost)), high)


if __name__ == "__main__":
    pass
    # with open("./data/lowGraph.txt", "w") as file:
    #     gMtrx = getGraph(9, 1, 10)
    #     for row in gMtrx:
    #         file.write(' '.join([str(el) for el in row]) + '\n')

    # with open("./data/highGraph.txt", "w") as file:
    #     gMtrx = getGraph(9, 1, 2500)
    #     for row in gMtrx:
    #         file.write(' '.join([str(el) for el in row]) + '\n')
