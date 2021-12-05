#include <iostream>
#include <iomanip>
#include <cmath>
#include <chrono>
#include <vector>

#include "actions.h"
#include "integral.h"

using namespace std;

#define FUNC_MSG \
"Функции:\n\
     1 -- x^2;\n\
     2 -- x * sin x;\n\
     3 -- √(e^(sin x * cos x) + 6 * |x + 6|) +\n\
          + ln|x^3 - 3x + 1|;\n\
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

void single(int &ch)
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
            cout << "Неверный ввод!" << endl;
            ch = EXIT;
            return;
    }

    interval_t interval = {.begin = 0, .end = 0, .eps = 1};

    cout << "Введите нижний предел: ";
    cin >> interval.begin;

    if (cin.fail())
    {
        cin.clear();
        cin.ignore(32767,'\n');
        cout << "Неверный ввод!" << endl;
        ch = EXIT;
        return;
    }

    cout << "Введите верхний предел: ";
    cin >> interval.end;

    if (cin.fail())
    {
        cin.clear();
        cin.ignore(32767,'\n');
        cout << "Неверный ввод!" << endl;
        ch = EXIT;
        return;
    }

    short int sign = 1;
    if (interval.end < interval.begin)
    {
        swap(interval.end, interval.begin);
        sign = -1;
    }

    unsigned int digit_num;
    cout << "Введите количество знаков после запятой: ";
    cin >> digit_num;

    if (cin.fail())
    {
        cin.clear();
        cin.ignore(32767,'\n');
        cout << "Неверный ввод!" << endl;
        ch = EXIT;
        return;
    }

    if (digit_num > 7)
    {
        cout << "К сожалению, это будет долго!" << endl;
        cout << "Возьми поменьше!" << endl;
        ch = 0;
        return;
    }

    interval.eps = 1 / pow(10, digit_num);

    unsigned int th_num;
    cout << "Введите количество потоков: ";
    cin >> th_num;

    if (cin.fail())
    {
        cin.clear();
        cin.ignore(32767,'\n');
        cout << "Неверный ввод!" << endl;
        ch = EXIT;
        return;
    }

    cout.setf(ios_base::fixed);
    long double s_res, p_res;
    auto start = chrono::system_clock::now();
    s_res = sign * integralByPrecision(interval, f);
    auto finish = chrono::system_clock::now();
    double t = chrono::duration_cast<chrono::nanoseconds> (finish - start).count();

    cout << endl << "ЗНАЧЕНИЕ ИНТЕГРАЛА" << endl;
    cout << "Последовательный алгоритм: " << setprecision(digit_num) << s_res << endl;
    cout << "Время: " << setprecision(0) << t << " нс" << endl;

    start = chrono::system_clock::now();
    p_res = sign * parallelIntegralByPrecision(th_num, interval, f);
    finish = chrono::system_clock::now();
    t = chrono::duration_cast<chrono::nanoseconds> (finish - start).count();

    cout << "Параллельный алгоритм: " << setprecision(digit_num) << p_res << endl;
    cout << "Время: " << setprecision(0) << t << " нс" << endl;
}

enum time_mode_t
{
    BY_THREADS,
    BY_EPS
};

#define TIME_MSG \
"Режимы:\n\
     1 -- по количеству потоков;\n\
     2 -- по точности при фиксированном числе потоков.\n\
Выберете режим: "

#define RUN_NUM 10

double getSTime(interval_t &interval)
{
    auto start = chrono::system_clock::now();
    integralByPrecision(interval, f3);
    auto finish = chrono::system_clock::now();

    return chrono::duration_cast<chrono::nanoseconds> (finish - start).count();
}

double getPTime(const int threads_num, interval_t &interval)
{
    auto start = chrono::system_clock::now();
    parallelIntegralByPrecision(threads_num, interval, f3);
    auto finish = chrono::system_clock::now();

    return chrono::duration_cast<chrono::nanoseconds> (finish - start).count();
}

void getThreadsTime(const int num)
{
    interval_t interval = {.begin = -10, .end = 10, .eps = 1e-6};
    int nums[] = {1, 2, 4, 8, 16, 32, 64};
    const int len = sizeof(nums) / sizeof(nums[0]);
    double times[len] = {0};

    double s_res = 0;

    for (int i = 0; i < num; ++i)
    {
        s_res += getSTime(interval);

        for (int j = 0; j < len; ++j)
        {
            times[j] += getPTime(nums[j], interval);
        }
    }

    for (auto &t : times)
    {
        t /= num;
    }

    cout.setf(ios_base::fixed);
    cout << "Последовательный Алгоритм" << endl;
    cout << setprecision(0) << s_res / num << "нс" << endl;
    cout << endl;

    cout << "Параллельный Алгоритм" << endl;
    cout << "Число потоков/Время, нс" << endl;

    for (int i = 0; i < len; ++i)
    {
        cout.width(2);
        cout << nums[i] << " / ";
        cout.width(11);
        cout << times[i] << endl;
    }
}

void getEpsTime(const int num)
{
    interval_t interval = {.begin = -10, .end = 10, .eps = 0.1};

    double s_res = 0, p_res = 0;

    cout << "Точность  Последовательный   8 потоков" << endl;

    for (int i = 0; i < 7; ++i)
    {
        for (int j = 0; j < num; ++j)
        {
            s_res += getSTime(interval);
            p_res += getPTime(8, interval);
        }

        cout.width(8);
        std::cout << std::defaultfloat;
        cout << interval.eps << "  ";
        cout.setf(ios_base::fixed);
        cout << setprecision(0);
        cout.width(16);
        cout << s_res / num << "  ";
        cout.width(10);
        cout << p_res / num << endl;

        interval.eps /= 10;
    }
}

void mass(int &ch)
{
    int mode;
    cout << TIME_MSG;
    cin >> mode;

    switch (mode)
    {
        case BY_THREADS + 1:
            getThreadsTime(RUN_NUM);
            break;
        case BY_EPS + 1:
            getEpsTime(RUN_NUM);
            break;
        default:
            cout << "Неверный ввод!" << endl;
            ch = EXIT;
            return;
    }
}
