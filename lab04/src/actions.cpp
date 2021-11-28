#include <iostream>
#include <iomanip>
#include <cmath>
#include <chrono>

#include "actions.h"
#include "integral.h"

using namespace std;

#define FUNC_MSG \
"Функции:\n\
     1 -- x^2;\n\
     2 -- x * sin(x);\n\
     3 -- sqrt(e^x + 6);\n\
Выберете функцию: "

enum funcs_t
{
    SQR,
    SIN,
    X
};

long double f1(double x)
{
    return x * x;
}

long double f2(double x)
{
    return x * sin(x);
}

long double f3(double x)
{
    return sqrt(exp(sin(x) * cos(x)) + 6 * abs(x + 6)) + \
           log(abs(x * x * x - 3 * x + 1));
}

void single(void)
{
    int func;
    cout << FUNC_MSG;
    cin >> func;

    function_t f = NULL;

    switch (func)
    {
        case SQR + 1:
            f = f1;
            break;
        case SIN + 1:
            f = f2;
            break;
        case X + 1:
            f = f3;
            break;
        default:
            cout << "Неверный ввод!";
            return;
    }

    interval_t interval = {.begin = 0, .end = 0, .eps = 1};

    cout << "Введите нижний предел: ";
    cin >> interval.begin;

    cout << "Введите верхний предел: ";
    cin >> interval.end;

    unsigned int digit_num;
    cout << "Введите количество знаков после запятой: ";
    cin >> digit_num;
    cout << "digit_num" << digit_num;
    interval.eps = 1 / pow(10, digit_num);
    cout << "eps " << interval.eps << endl;

    unsigned int th_num;
    cout << "Введите количество потоков:";
    cin >> th_num;

    cout.setf(ios_base::fixed);
    long double s_res, p_res;
    //cout << "not parallel" << endl;
    auto start = chrono::system_clock::now();
    s_res = integralByPrecision(interval, f);
    auto finish = chrono::system_clock::now();
    double t = chrono::duration_cast<chrono::nanoseconds> (finish - start).count();

    cout << "ЗНАЧЕНИЕ ИНТЕГРАЛА" << endl;
    cout << "Последовательный алгоритм: " << setprecision(digit_num) << s_res << endl;
    cout << "Время: " << setprecision(0) << t << " нс" << endl;

    start = chrono::system_clock::now();
    p_res = parallelIntegralByPrecision(th_num, interval, f);
    finish = chrono::system_clock::now();
    t = chrono::duration_cast<chrono::nanoseconds> (finish - start).count();

    cout << "Параллельный алгоритм: " << setprecision(digit_num) << p_res << endl;
    cout << "Время: " << setprecision(0) << t << " нс" << endl;
}
