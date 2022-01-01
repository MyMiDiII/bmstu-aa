import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import filedialog as fd
from colored import fg, attr

import brute_force
import ants

from utils import *
from experiments import getTimes, parametrization

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

    res = brute_force.salesman(graph)

    print()
    print("%sРЕЗУЛЬТАТЫ%s" % (fg('green'), attr(0)))
    print("Полный перебор")
    if not res:
        print("%sСлишком большое количество городов!%s" % (fg('red'), attr(0)))
    else:
        print("Тур с минимальной стоимостью:")
        printTour(res[0])
        print("Стоимость: ", res[1])

    try:
        alpha = float(input("Введите вес следа феромона α: "))
        evarpolation = float(input(
                             "Введите коэффициент испарения феромона p: "))
        daysNum = int(input("Введите количество дней: "))
    except:
        print("%sНеверный ввод!%s" % (fg('red'), attr(0)))
        return

    res = ants.salesman(graph, alpha, evarpolation, daysNum)
    print("Муравьиный алгоритм")
    print("Тур с минимальной стоимостью:")
    printTour(res[0])
    print("Стоимость: ", res[1])


def massExperiments():
    sizes = [x for x in range(2, 11)]
    funcs = [
            brute_force.salesman,
            ants.salesman
            ]
    args  = [
            [],
            [0.5, 0.5, 250]
            ]
    times = getTimes(funcs, args, sizes)

    print()
    names = [
            'Размер',
            'Перебор, нс',
            'Муравьиный, нс',
            ]
    print("Таблица зависимостей времени работы от количества городов")
    printTable(sizes, times, names, 0)
    saveTableAsCSV(sizes, times)

    labels = ['перебор', 'муравьиный']
    for i, algTime in enumerate(times):
        if None not in algTime:
            plt.plot(sizes, algTime, label=labels[i])

    plt.xlabel("Размер", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

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
    menuFuncs = [lambda: True, singleExperiment, massExperiments, 
                 parametrization, wrongAnswer]

    answer = 1
    while answer:
        printMenu()
        answer = getAnswer()
        menuFuncs[answer]()

    print("Спасибо за использование программы!")
