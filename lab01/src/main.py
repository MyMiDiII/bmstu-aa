import matplotlib.pyplot as plt

from prettytable import PrettyTable

from levenstein import *
from dameraulevenstein import *
from experiments import *


def printInfo():
    print("Программа предоставляет интерфейс для поиска расстояний\n"
          + "Левенштейна и Дамерау-Левенштейна между двумя строками\n" 
          + "и дает возможность сравнить быстродействие различных "
          + "реализаций."
         )


def printAuthor():
    print("АВТОР: Маслова Марина")
    print("ГРУППА: ИУ7-53Б")


def printGreeting():
    print("РАССТОЯНИЕ ЛЕВЕНШТЕЙНА И ДАМЕРАУ-ЛЕВЕНШТЕЙНА")
    print()
    printInfo();
    print()
    printAuthor();


def printMenu():
    print()
    print("МЕНЮ")
    print()
    print("1 -- расстояние между двумя строками;")
    print("2 -- сравнение различных реализаций;")
    print("0 -- выход")
    print()
    print("Выбор:")


def singleExperiment():
    print("ЕДИНИЧНЫЙ ЭКСПЕРИМЕНТ")
    str1 = input("Первая строка: ").lower()
    str2 = input("Вторая строка: ").lower()
    print()
    print("РЕЗУЛЬТАТЫ")
    print("Расстояния Левенштейна")
    print("Рекурсивный алгоритм:", recursiveLevenstein(str1, str2))
    matrRes, matr = matrixLevenstein(str1, str2)
    print("Матричный алгоритм:", matrRes)
    print("Рекурсивный алгоритм с кэшем:", cacheLevenstein(str1, str2))
    printDistMatrix(matr, str1, str2)
    print("Расстояние Дамерау-Левенштейна")
    print("Рекурсивный алгоритм с кэшем:",
           сacheDamerauLevenstein(str1, str2))


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
    lens = [10, 30, 50, 70, 90, 110, 130, 150, 170]
    funcs = [
             recursiveLevenstein,
             matrixLevenstein,
             cacheLevenstein
            ]
    timesLev = getTimes(funcs, lens)

    funcs = [
            cacheLevenstein,
            сacheDamerauLevenstein
            ]
    timesLevVSDam = getTimes(funcs, lens)

    print()
    names = ['Длина', 'Рекурсивный', 'Матричный', 'С кэшем']
    print("Таблица времени выполнения разных реализаций алгоритма поиска")
    print("        расстояния Левенштейна(время в наносекундах)")
    printTable(lens, timesLev, names, 6)

    print()
    names = ['Длина', 'Левенштейн с кэшем', 'Дамерау-Левенштейн с кэшем']
    print("Таблица времени выполнения алгоритмов поиска расстояний Левенштейна")
    print("        и Дамераy-Левенштейна с кэшем (время в наносекундах)")
    printTable(lens, timesLevVSDam, names, 4)

    plt.figure(figsize=(7, 9))
    plt.subplots_adjust(hspace=0.7)
    plt.subplot(2, 1, 1)
    labels = ['рекурсивный', 'матричный', 'с кэшем']
    for i, algTime in enumerate(timesLev):
        if None not in algTime:
            plt.plot(lens, algTime, label=labels[i])
    plt.title("Сравнение реализаций алгоритма поиска расстояния Левенштейна\n")
    plt.xlabel("Длина строк", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    labels = ['Левенштейн', 'Дамерау-Левенштейн']
    for i, algTime in enumerate(timesLevVSDam):
        if None not in algTime:
            plt.plot(lens, algTime, label=labels[i])
    plt.title("Сравнение времени выполнения поиска расстояния Левенштейна и"
              + "\nпоиска расстояния Дамерау-Левенштейна\n")
    plt.xlabel("Длина строк", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.get_current_fig_manager().window.move(960, 0)
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
