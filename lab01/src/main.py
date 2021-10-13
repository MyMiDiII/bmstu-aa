from levenstein import *

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
    str1 = input("Первая строка: ")
    str2 = input("Вторая строка: ")
    print()
    print("РЕЗУЛЬТАТЫ")
    print("Расстояния Левенштейна")
    print("Рекурсивный алгоритм: ", recursiveLevenstein(str1, str2))
    # ! в схему присваивание расстояния ячейке
    matrRes, matr = matrixLevenstein(str1, str2)
    print("Матричный алгоритм: ", matrRes)
    printDistMatrix(matr, str1, str2)


def func2():
    print("func2")

def wrongAnswer():
    print("Нет такого пунтка меню!")
    print("Попробуйте ещё раз!")

def getAnswer():
    answer = input()
    answer = -1 if answer not in ("0", "1", "2") else int(answer)
    return answer

if __name__ == "__main__":
    printGreeting()
    menuFuncs = [lambda: True, singleExperiment, func2, wrongAnswer]

    answer = 1
    while answer:
        printMenu()
        answer = getAnswer()
        menuFuncs[answer]()

    print("Спасибо за использование программы!")
