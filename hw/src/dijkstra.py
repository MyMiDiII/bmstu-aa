from math import inf


def dijkstra(graph, start):
    rows = len(graph)                                          #1
    columns = len(graph[0])                                    #2

    dists = [inf] * rows
    dists[start] = 0

    queue = [i for i in range(rows)]

    while queue:
        minVal = inf
        minInd = -1

        for i, dist in enumerate(dists):
            if dist < minVal and i in queue:
                minVal = dist
                minInd = i

        queue.remove(minInd)

        for i in range(columns):
            if graph[minInd][i] and i in queue:
                newDist = dists[minInd] + graph[minInd][i]
                if newDist < dists[i]:
                    dists[i] = newDist

    return dists


if __name__ == '__main__':
    example = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
              ]

    example2 = [[0, 2, 0, 0, 10],
                [0, 0, 3, 0, 7],
                [0, 0, 0, 4, 0],
                [0, 0, 0, 0, 5],
                [0, 0, 6, 0, 0]]

    res = dijkstra(example, 0)
    print(res)

    if res == [0, 4, 12, 19, 21, 11, 9, 8, 14]:
        print("OK")
    else:
        print("NO")

    res = dijkstra(example2, 0)
    print(res)
