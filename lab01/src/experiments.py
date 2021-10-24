import string
import random
import time

from levenstein import *
from dameraulevenstein import *


def get2strings(length):
    str1 = ''.join((random.choice(string.ascii_lowercase))
                   for i in range(length))

    str2 = ''.join((random.choice(string.ascii_lowercase))
                   for i in range(length))

    return str1, str2


def getTime(str1, str2, editDistance, num):
    avgTime = 0

    for i in range(num):
        start = time.process_time_ns()
        editDistance(str1, str2)
        avgTime += time.process_time_ns() - start

    avgTime = avgTime / 10

    return int(avgTime)


def getTimes(funcs, lens):
    times = [[] for x in range(len(funcs))]

    print("\nИдет подсчет времени. Пожалуйста, подождите...")
    for length in lens:
        print("Подсчет для длины =", length)
        str1, str2 = get2strings(length)

        for i, func in enumerate(funcs):
            funcTime = (None if func == recursiveLevenstein and length > 10
                            else getTime(str1, str2, func, 10))
            times[i].append(funcTime)

    return times
