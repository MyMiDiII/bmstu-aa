INF = -1

def recursiveLevenstein(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    dist = 0
    if len1 == 0:
        dist = len2
    elif len2 == 0:
        dist = len1
    else:
        addDist = 0 if str1[-1] == str2[-1] else 1
        dist = 1 + min(recursiveLevenstein(str1, str2[:-1]),
                       recursiveLevenstein(str1[:-1], str2))
        dist = min(dist, addDist + recursiveLevenstein(str1[:-1], str2[:-1]))

    return dist


def matrixInit(len1, len2):
    matrix = [[i + j if i * j == 0 else INF for i in range(len1 + 1)]
               for j in range(len2 + 1)]

    return matrix


def matrixLevenstein(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    matr = matrixInit(len1, len2)
    dist = 0
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            addDist = 0 if str1[i - 1] == str2[j - 1] else 1
            dist = 1 + min(matr[i - 1][j], matr[i][j - 1])
            dist = min(dist, addDist + matr[i - 1][j - 1])
            matr[i][j] = dist

    return dist

