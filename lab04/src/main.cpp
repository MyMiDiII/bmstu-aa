#include <iostream>

#include "integral.h"
#include "actions.h"

using namespace std;

#define MENU_MSG \
"     МЕНЮ\n\
1 -- подсчет интеграла;\n\
2 -- сравнение последовательного и параллельного алгоритмов;\n\
0 -- выход.\n\n\
Выбор: "

int main(void)
{
    int ch = BEGIN;

    while (ch)
    {
        cout << MENU_MSG << endl;

        cin >> ch;

        switch(ch)
        {
            case SINGLE:
                single();
                break;
            case MASS:
                cout << "mass!" << endl;
                //mass();
                break;
            default:
                ch = 0;
        }
    }

    return 0;
}
