import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import filedialog as fd
from prettytable import PrettyTable
from colored import fg, attr

import overdone

from print_utils import *

def printInfo():
    print("Полный перебор и муравьиный алгоритм для задачи коммивояжера")


def printAuthor():
    print("АВТОР: Маслова Марина")
    print("ГРУППА: ИУ7-53Б")


def printGreeting():
    print("ЗАДАЧА КОММИВОЯЖЕРА")
    print()
    printInfo();
    print()
    printAuthor();


def printMenu():
    print()
    print("МЕНЮ")
    print()
    print("1 -- решение задачи коммивояжера;")
    print("2 -- сравнение различных алгритмов;")
    print("3 -- параметризация муравьиного алгоритма;")
    print("0 -- выход")
    print()
    print("Выбор:")


def singleExperiment():
    print("ЗАДАЧА КОММИВОЯЖЕРА")

    root = tk.Tk()
    root.withdraw()
    filename = fd.askopenfilename(initialdir='./data')
    
    if not filename:
        print("%sФайл не выбран!%s" % (fg('red'), attr(0)))
        return

    with open(filename, 'r') as file:
        graph = [[float(cost) for cost in row.split()] for row in file]

    res = overdone.salesman(graph)

    print()
    print("%sРЕЗУЛЬТАТЫ%s" % (fg('green'), attr(0)))
    print("Полный перебор")
    if not res:
        print("%sСлишком большое количество городов!%s" % (fg('red'), attr(0)))
    else:
        print("Тур с минимальной стоимостью:")
        printTour(res[0])
        print("Стоимость: ", res[1])


def massExperiments():
    sizes = [x for x in range(100, 1001, 100)]
    funcs = [
            insertionSort,
            shakerSort,
            selectionSort
            ]
    timesIncrease = getTimes(funcs, sizes, Mode.INC)
    timesDecrease = getTimes(funcs, sizes, Mode.DEC)
    timesRandom= getTimes(funcs, sizes, Mode.RAN)

    print()
    names = [
            'Размер',
            'Вставками, нс',
            'Перемешиванием, нс',
            'Выбором, нс'
            ]
    print("      Таблица времени выполнения алгоритмов сортировки\n"
          "           на отсортированных последовательностях")
    printTable(
            [size for size in sizes],
            timesIncrease,
            names,
            0)

    print()
    print("      Таблица времени выполнения алгоритмов сортировки\n"
          " на последовательностях, отсортированных в обратном порядке")
    printTable(
            [size for size in sizes],
            timesDecrease,
            names,
            0)

    print()
    print("      Таблица времени выполнения алгоритмов сортировки\n"
          "              на случайных последовательностях")
    printTable(
            [size for size in sizes],
            timesRandom,
            names,
            0)

    plt.figure(figsize=(15.5, 9))
    plt.subplots_adjust(hspace=0.5)
    plt.subplot(2, 2, 1)
    labels = ['вставками', 'перемешиванием', 'выбором']
    for i, algTime in enumerate(timesIncrease):
        if None not in algTime:
            plt.plot(sizes, algTime, label=labels[i])
    plt.title("Отсортированные\nпоследовательности\n")
    plt.xlabel("Размер", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 2)
    for i, algTime in enumerate(timesIncrease[:-1]):
        if None not in algTime:
            plt.plot(sizes, algTime, label=labels[i])
    plt.title("Отсортированные\nпоследовательности (без выбора)\n")
    plt.xlabel("Размер", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 3)
    for i, algTime in enumerate(timesDecrease):
        if None not in algTime:
            plt.plot(sizes, algTime, label=labels[i])
    plt.title("Отсортированные в обратном\nпорядке последовательности\n")
    plt.xlabel("Размер", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 4)
    for i, algTime in enumerate(timesRandom):
        if None not in algTime:
            plt.plot(sizes, algTime, label=labels[i])
    plt.title("Случайные последовательности")
    plt.xlabel("Размер", fontsize=14)
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
    answer = -1 if answer not in ("0", "1", "2", "3") else int(answer)
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
