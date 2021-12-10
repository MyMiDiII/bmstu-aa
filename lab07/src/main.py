import matplotlib.pyplot as plt

from colored import fg, attr

from dictionary import Dictionary

from utils import *
from experiments import getTimes, getComps

DATADIR = './data/'
FULL_COMB_SEARCH = 1
BIN_SEARCH = 2
SEGM_SEARCH = 3

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
    print("2 -- сравнение различных алгоритмов по времени;")
    print("3 -- сравнение различных алгоритмов по количеству сравнений;")
    print("0 -- выход")
    print()
    print("Выбор:")


def singleExperiment(myDict):
    name = input('Введите название игры: ')

    print("%sПолный перебор%s" % (fg('blue'), attr(0)))
    res, compNum = myDict.bruteForce(name)
    printRes(res, name)
    print("Количество сравнений:", compNum)

    print("%sБинарный поиск%s" % (fg('blue'), attr(0)))
    res, compNum = myDict.binSearch(name)
    printRes(res, name)
    print("Количество сравнений:", compNum)

    print("%sСегментация словаря%s" % (fg('blue'), attr(0)))
    res, compNum = myDict.segSearch(name)
    printRes(res, name)
    print("Количество сравнений:", compNum)


def massExperimentsTime(myDict):
    keys = myDict.getKeys()
    inds = [i + 1 for i in range(len(keys))]
    funcs = [
            myDict.bruteForce,
            myDict.binSearch,
            myDict.segSearch
            ]

    times = getTimes(funcs, keys)

    labels = ['бинарный поиск', 'сегментация']

    for i, algTime in enumerate(times):
        if None not in algTime:
            plt.plot(inds, algTime, label=labels[i])

    plt.xlabel("Индекс ключа", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.show()


def massExperimentsComp(myDict):
    keys = myDict.getKeys()
    inds = [i + 1 for i in range(len(keys))]
    funcs = [
            myDict.bruteForce,
            myDict.binSearch,
            myDict.segSearch
            ]
    algs = [
            'перебор',
            'бинарный',
            'сегментация'
           ]

    comps = getComps(funcs, keys)


    for j in range(3):
        fig, ax = plt.subplots(2, 1)

        ax[0].bar(inds, comps[j], color='c')
        ax[0].set(title=algs[j])

        sortComps = sorted(comps[j], reverse=True)

        ax[1].bar(inds, sortComps, color='c')
        ax[1].set(title=algs[j] + '(по убыванию)')
        
        for i in range(2):
            ax[i].set_xlabel("Индекс ключа")
            ax[i].set_ylabel("Количество сравнений")

        plt.subplots_adjust(hspace=0.5)
        plt.get_current_fig_manager().window.showMaximized()

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
    print("Загрузка словаря...")
    myDict = Dictionary(DATADIR + 'games.csv')

    menuFuncs = [lambda: True, singleExperiment, massExperimentsTime,
                 massExperimentsComp, wrongAnswer]
    args = [[], [myDict], [myDict], [myDict], []]

    answer = 1
    while answer:
        printMenu()
        answer = getAnswer()
        menuFuncs[answer](*args[answer])

    print("Спасибо за использование программы!")
