import matplotlib.pyplot as plt

from colored import fg, attr

from dictionary import Dictionary

from utils import *

DATADIR = './data/'

def printInfo():
    print("Сравнение алгоритмов поиска в словаре")


def printAuthor():
    print("АВТОР: Маслова Марина")
    print("ГРУППА: ИУ7-53Б")


def printGreeting():
    print("ПОИСК В СЛОВАРЕ")
    print()
    printInfo();
    print()
    printAuthor();


def printMenu():
    print()
    print("МЕНЮ")
    print()
    print("1 -- поиск;")
    print("2 -- сравнение различных алгоритмов;")
    print("0 -- выход")
    print()
    print("Выбор:")


def singleExperiment(myDict):
    name = input('Введите название игры: ')

    print(myDict.bruteForce(name))
    print(myDict.binSearch(name))
    #print(myDict.segSearch(name))
    

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
    myDict = Dictionary(DATADIR + 'games.csv')

    printGreeting()
    menuFuncs = [lambda: True, singleExperiment, massExperiments, wrongAnswer]
    args = [[], [myDict], [myDict], []]

    answer = 1
    while answer:
        printMenu()
        answer = getAnswer()
        menuFuncs[answer](*args[answer])

    print("Спасибо за использование программы!")
