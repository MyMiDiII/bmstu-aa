from math import inf


def dijkstra(graph, start):
    rows = len(graph)                                          #1
    columns = len(graph[0])                                    #2

    dists = [inf] * rows                                       #3
    dists[start] = 0                                           #4 

    queue = [i for i in range(rows)]                           #5

    while queue:                                               #6
        minVal = inf                                           #7
        minInd = -1                                            #8

        for i, dist in enumerate(dists):                       #9
            if dist < minVal and i in queue:                   #10
                minVal = dist                                  #11
                minInd = i                                     #12

        queue.remove(minInd)                                   #13

        for i in range(columns):                               #14
            if graph[minInd][i] and i in queue:                #15
                newDist = dists[minInd] + graph[minInd][i]     #16
                if newDist < dists[i]:                         #17
                    dists[i] = newDist                         #18

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

    if res == [0, 2, 5, 9, 9]:
        print("OK")
    else:
        print("NO")
