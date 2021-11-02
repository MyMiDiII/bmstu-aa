def readMatr(n, m):
    matr = []
    for i in range(n):
        matr.append(list(map(int, input().split())))
        
        if len(matr[i]) != m:
            raise IndexError

    return matr


def printMatr(matrix):
    for str in matrix:
        for el in str:
            print(el, end=" ")
        print()


def standartMatrProd(m1, m2):
    N = len(m1)
    P = len(m2)
    M = len(m2[0])

    res = [[0 for j in range(N)] for i in range(M)]

    for i in range(N):
        for j in range(M):
            for k in range(P):
                res[i][j] += m1[i][k] * m2[k][j]

    return res


def countMulH(matrix):
    N = len(matrix)
    P = len(matrix[0])

    mulH = [0] * N

    for i in range(N):
        for j in range(P // 2):
            mulH[i] = mulH[i] + matrix[i][2 * j + 1] * matrix[i][2 * j]

    return mulH


def countMulV(matrix):
    P = len(matrix)
    M = len(matrix[0])

    mulV = [0] * M

    for i in range(M):
        for j in range(P // 2):
            mulV[i] = mulV[i] + matrix[2 * j + 1][i] * matrix[2 * j][i]

    return mulV


def WinogradMatrProd(m1, m2):
    N = len(m1)
    P = len(m2)
    M = len(m2[0])

    res = [[0 for j in range(N)] for i in range(M)]

    mulH = countMulH(m1)
    mulV = countMulV(m2)

    for i in range(N):
        for j in range(M):
            res[i][j] = - mulH[i] - mulV[j]

            for k in range(P // 2):
                res[i][j] = (res[i][j]
                            + (m1[i][2 * k] + m2[2 * k + 1][j])
                            * (m1[i][2 * k + 1] + m2[2 * k][j]))

            if P % 2:
                res[i][j] = res[i][j] + m1[i][P - 1] * m2[P - 1][j]

    return res


def optCountMulH(matrix):
    N = len(matrix)
    P = len(matrix[0])

    mulH = [0] * N

    for i in range(N):
        for j in range(0, P - 1, 2):
            mulH[i] += matrix[i][j + 1] * matrix[i][j]

    return mulH


def optCountMulV(matrix):
    P = len(matrix)
    M = len(matrix[0])

    mulV = [0] * M

    for i in range(M):
        for j in range(0, P - 1, 2):
            mulV[j] += matrix[j + 1][i] * matrix[j][i]

    return mulV


def optWinogradMatrProd(m1, m2):
    N = len(m1)
    P = len(m2)
    M = len(m2[0])

    res = [[0 for j in range(N)] for i in range(M)]

    mulH = countMulH(m1)
    mulV = countMulV(m2)

    for i in range(N):
        for j in range(M):
            res[i][j] -= mulH[i] + mulV[j]

            for k in range(0, P - 1, 2):
                res[i][j] += (
                        (m1[i][k] + m2[k + 1][j])
                        * (m1[i][k + 1] + m2[k][j])
                        )

            if P % 2:
                res[i][j] += m1[i][P - 1] * m2[P - 1][j]

    return res
