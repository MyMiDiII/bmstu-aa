import time

def getTime(key, func, num):
    avgTime = 0

    for i in range(num):
        start = time.process_time_ns()
        func(key)
        avgTime += time.process_time_ns() - start

    avgTime = avgTime / num

    return int(avgTime)


def getTimes(funcs, keys):
    times = [[] for x in range(len(funcs))]

    for i, key in enumerate(keys):
        for j, func in enumerate(funcs):
            funcTime = getTime(key, func, 10)
            times[j].append(funcTime)

        if (i + 1) % 50 == 0:
            print("Обработано", i + 1, "ключей")

    return times


def getComps(funcs, keys):
    comps = [[] for x in range(len(funcs))]

    for i, key in enumerate(keys):
        for j, func in enumerate(funcs):
            _, compNum = func(key)
            comps[j].append(compNum)

        if (i + 1) % 50 == 0:
            print("Обработано", i + 1, "ключей")

    return comps

