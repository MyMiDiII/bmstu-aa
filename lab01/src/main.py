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
    print("Рекурсивный алгоритм:", recursiveDamerauLevenstein(str1, str2))


def printTimeTable(lens, times):
    table = PrettyTable()
    print("Таблица времени выполнения алгоритмов на разных длинах строк")
    print("                  (время в наносекундах)")

    table.field_names = ['Длина', 'Рекурсивный', 'Матричный', 'С кэшем']
    for i in range(len(lens)):
        table.add_row([lens[i], times[0][i], times[1][i], times[2][i]])

    table.align = 'r'
    print('     ', table.get_string().replace('\n', '\n      '))

def massExperiments():
    lens = [10, 30, 50, 70, 90, 110, 130, 150, 170]
    funcs = [
             recursiveLevenstein,
             matrixLevenstein,
             cacheLevenstein
            ]
    times = getTimes(funcs, lens)

    printTimeTable(lens, times)
    for algTime in times:
        if None not in algTime:
            plt.plot(lens, algTime)

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
