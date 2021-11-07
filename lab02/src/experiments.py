import string
import random
import time

def getMatrix(N, M):
    return [[random.randint(-100, 100) for j in range(M)] for i in range(N)]

def getTime(arg1, arg2, func, num):
    avgTime = 0

    print("Подсчет для функции", func.__name__)
    for i in range(num):
        print("Итерация", i)
        start = time.process_time_ns()
        func(arg1, arg2)
        avgTime += time.process_time_ns() - start

    avgTime = avgTime / num

    return int(avgTime)


def getTimes(funcs, sizes):
    times = [[] for x in range(len(funcs))]

    print("\nИдет подсчет времени. Пожалуйста, подождите...")
    for size in sizes:
        print("Подсчет для матрицы размером %dx%d" % (size, size))
        matr1 = getMatrix(size, size)
        matr2 = getMatrix(size, size)
        
        for i, func in enumerate(funcs):
            funcTime = getTime(matr1, matr2, func, 10)
            times[i].append(funcTime)

    return times
