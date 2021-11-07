import matplotlib.pyplot as plt

from prettytable import PrettyTable

from matrixes import *
from experiments import *

def printInfo():
    print("Программа предоставляет интерфейс для вычисления произведения\n"
            + "двух матриц стандартным алгоритмом и алгоритмом Винограда и\n"
            + "дает возможность сравнить быстродействие различных реализаций.")


def printAuthor():
    print("АВТОР: Маслова Марина")
    print("ГРУППА: ИУ7-53Б")


def printGreeting():
    print("ПРОИЗВЕДЕНИЕ МАТРИЦ")
    print()
    printInfo();
    print()
    printAuthor();


def printMenu():
    print()
    print("МЕНЮ")
    print()
    print("1 -- произведение двух матриц;")
    print("2 -- сравнение различных реализаций;")
    print("0 -- выход")
    print()
    print("Выбор:")


def singleExperiment():
    try:
        print("ЕДИНИЧНЫЙ ЭКСПЕРИМЕНТ")

        print("Размеры первой матрицы:")
        n = int(input('Строки: '))

        if n <= 0:
            raise ValueError

        p1 = int(input('Столбцы: '))

        if p1 <= 0:
            raise ValueError

        print("Размеры второй матрицы:")
        p2 = int(input('Строки: '))

        if p2 <= 0:
            raise ValueError

        if p1 != p2:
            print("\033[31mОперация умножения матриц с такими размерами не "
                  + "определена\033[00m")
            return

        m = int(input('Столбцы: '))

        if m <=0:
            raise ValueError

    except ValueError:
        print("\033[31mРазмер матрицы -- натуральное число!\033[00m")
        return

    print("Введите первую матрицу (%dx%d):" % (n, p1))
    try:
        matr1 = readMatr(n, p1)
    except ValueError:
        print("\033[31mЭлементы матрицы -- целые числа!\033[00m")
        return
    except IndexError:
        print("\033[31mВведите матрицу в %d строк по %d столбцов!\033[00m"
              % (n, p1))
        return

    print("Введите вторую матрицу (%dx%d):" % (p1, m))
    try:
        matr2 = readMatr(p2, m)
    except ValueError:
        print("\033[31mЭлементы матрицы -- целые числа!\033[00m")
        return
    except IndexError:
        print("\033[31mВведите матрицу в %d строк по %d столбцов!\033[00m"
              % (p1, m))
        return

    print()
    print("РЕЗУЛЬТАТЫ")
    print("Стандартный алгоритм:")
    printMatr(standartMatrProd(matr1, matr2))
    print("Алгоритм Винограда:")
    printMatr(WinogradMatrProd(matr1, matr2))
    print("Оптимизированный алгоритм\nВинограда:")
    printMatr(optWinogradMatrProd(matr1, matr2))


def printTable(lens, times, names, align=0):
    table = PrettyTable()
    table.field_names = names
    for i in range(len(lens)):
        table.add_row([lens[i]] + [col[i] for col in times])

    table.align = 'r'
    print(
        align * ' ',
        table.get_string().replace('\n', '\n' + align * ' '),
        sep=''
        )


def massExperiments():
    sizes = [10, 20, 30, 40, 50, 70, 90, 110, 130, 150, 170, 200]
    funcs = [
            standartMatrProd,
            WinogradMatrProd,
            optWinogradMatrProd
            ]
    timesEven = getTimes(funcs, sizes)
    timesOdd  = getTimes(funcs, [size + 1 for size in sizes])

    print()
    names = [
            'Размеры',
            'Стандартный, нс',
            'Винограда, нс',
            'Оптимизированный, нс'
            ]
    print("      Таблица времени выполнения алгоритмов на четных рамерах")
    printTable(
            [str(size) + 'x' + str(size) for size in sizes],
            timesEven,
            names,
            0)

    print()
    print("     Таблица времени выполнения алгоритмов на нечетных рамерах")
    printTable(
            [str(size) + 'x' + str(size) for size in sizes],
            timesOdd,
            names,
            0)

    plt.figure(figsize=(15.5, 9))
    plt.subplots_adjust(hspace=0.5)
    plt.subplot(1, 2, 1)
    labels = ['стандартный', 'Винограда', 'оптимизированный Винограда']
    for i, algTime in enumerate(timesEven):
        if None not in algTime:
            plt.plot(sizes, algTime, label=labels[i])
    plt.title("Сравнение алгоритмов умножения матриц на четных значениях\n")
    plt.xlabel("Размер матриц", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    labels = ['стандартный', 'Винограда', 'оптимизированный Винограда']
    for i, algTime in enumerate(timesEven):
        if None not in algTime:
            plt.plot(sizes, algTime, label=labels[i])
    plt.title("Сравнение алгоритмов умножения матриц на нечетных значениях\n")
    plt.xlabel("Размер матриц", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.get_current_fig_manager().window.move(0, 0)
    plt.show()


def wrongAnswer():
    print("Нет такого пунтка меню!")
    print("Попробуйте ещё раз!")


def getAnswer():
    answer = input()
    answer = -1 if answer not in ("0", "1", "2") else int(answer)
    return answer


if __name__ == "__main__":
    printGreeting()
    menuFuncs = [lambda: True, singleExperiment, massExperiments, wrongAnswer]

    answer = 1
    while answer:
        printMenu()
        answer = getAnswer()
        menuFuncs[answer]()

    print("Спасибо за использование программы!")
