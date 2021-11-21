import string
import random
import time
from enum import Enum
from copy import deepcopy

def getRandomArr(size):
    return [random.randint(-10000, 10000) for x in range(size)]


def getIncreaseArr(size):
    return sorted(getRandomArr(size))


def getDecreaseArr(size):
    return sorted(getRandomArr(size), reverse=True)


class Mode(Enum):
    INC = getIncreaseArr
    DEC = getDecreaseArr
    RAN = getRandomArr


def getTime(arg1, arg2, func, num):
    arrCopy = deepcopy(arg1)
    avgTime = 0

    print("Подсчет для функции", func.__name__)
    for i in range(num):
        arg1 = deepcopy(arrCopy)
        start = time.process_time_ns()
        func(arg1, arg2)
        avgTime += time.process_time_ns() - start

    avgTime = avgTime / num

    return int(avgTime)


def getTimes(funcs, sizes, mode):
    times = [[] for x in range(len(funcs))]

    print("\nИдет подсчет времени. Пожалуйста, подождите...")
    for size in sizes:
        print("Подсчет для последовательности размером %d" % (size))
        arr = mode(size)
        
        for i, func in enumerate(funcs):
            funcTime = getTime(arr, size, func, 500)
            times[i].append(funcTime)

    return times
