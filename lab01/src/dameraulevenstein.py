def recursiveDamerauLevenstein(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dist = 0

    if len1 == 0:
        dist = len2
    elif len2 == 0:
        dist = len1
    else:
        addDist = 0 if str1[-1] == str2[-1] else 1
        dist = 1 + min(recursiveDamerauLevenstein(str1, str2[:-1]),
                       recursiveDamerauLevenstein(str1[:-1], str2))
        dist = min(dist, addDist
                         + recursiveDamerauLevenstein(str1[:-1], str2[:-1]))

        if (len1 > 1 and len2 > 1
                and str1[-1] == str2[-2] and str1[-2] == str2[-1]):
            dist = min(
                      dist,
                      recursiveDamerauLevenstein(str1[:-2], str2[:-2]) + 1
                   )

    return dist