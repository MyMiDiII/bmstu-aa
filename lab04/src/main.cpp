#include <iostream>

#include "integral.h"
#include "actions.h"

using namespace std;

#define HEADER "РАСПАРАЛЛЕЛИВАНИЕ АЛГОРИТМА ЧИСЛЕННОГО ИНТЕГРИРОВАНИЯ"

#define MENU_MSG \
"\n     МЕНЮ\n\
1 -- подсчет интеграла;\n\
2 -- сравнение последовательного и параллельного алгоритмов;\n\
0 -- выход.\n\n\
Выбор: "

int main(void)
{
    cout << HEADER << endl;
    int ch = BEGIN;

    while (ch)
    {
        cout << MENU_MSG << endl;

        cin >> ch;

        switch(ch)
        {
            case SINGLE:
                single(ch);
                break;
            case MASS:
                mass(ch);
                break;
            default:
                ch = 0;
        }
    }

    return 0;
}
