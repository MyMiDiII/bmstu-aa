from levenstein import matrixInit, INF

def recursiveCacheDamerauLevenstein(str1, str2, matr):
    len1 = len(str1)
    len2 = len(str2)
    dist = 0

    if matr[len1][len2] == INF:
        addDist = 0 if str1[-1] == str2[-1] else 1
        dist = 1 + min(recursiveCacheDamerauLevenstein(str1, str2[:-1], matr),
                       recursiveCacheDamerauLevenstein(str1[:-1], str2, matr))
        dist = min(dist, addDist
                       + recursiveCacheDamerauLevenstein(str1[:-1], str2[:-1],
                                                         matr))

        if (len1 > 1 and len2 > 1
                and str1[-1] == str2[-2] and str1[-2] == str2[-1]):
            dist = min(
                    dist,
                    recursiveCacheDamerauLevenstein(str1[:-2], str2[:-2], matr) 
                    + 1
                  )
        matr[len1][len2] = dist
    else:
        dist = matr[len1][len2]

    return dist


def сacheDamerauLevenstein(str1, str2):
    matr = matrixInit(len(str1), len(str2))

    dist = recursiveCacheDamerauLevenstein(str1, str2, matr)

    return dist
