#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

#include "integral.h"

long double midpoint(double begin, double end, unsigned int n, function_t func)
{
    double res = 0;
    double step = (end - begin) / n;
    double x = begin + step / 2;

    while (x < end + step / 2)
    {
        res += func(x) * step;
        x += step;
    }

    return res;
}

long double integralByPrecision(interval_t &interval, function_t func)
{
    unsigned long n = 2;
    long double delta = 1;
    long double res = 0, obt_res = 0;

    while (delta > interval.eps)
    {
        res = obt_res;
        obt_res = midpoint(interval.begin, interval.end, n, func);
        n *= 2;
        delta = abs(res - obt_res);
    }

    return res;
}

void parallelMidpoint(double begin, double end, unsigned int n, function_t func,
                      long double &res, int threads_num, int i, mutex &mut)
{
    double local_res = 0;
    double step = (end - begin) / n;
    double x = begin + i * step + step / 2;

    while (x < end + step / 2)
    {
        local_res += func(x) * step;
        x += step * threads_num;
    }

    mut.lock();
    res += local_res;
    mut.unlock();
}

long double multithreading(int threads_num, interval_t &interval,
                           unsigned int n, function_t func)
{
    long double res = 0;
    mutex res_mut;

    vector<thread> threads(threads_num);

    for (int i = 0; i < threads_num; i++)
    {
        threads[i] = thread(parallelMidpoint, interval.begin, interval.end, n,
                            func, ref(res), threads_num, i, ref(res_mut));
    }

    for (int i = 0; i < threads_num; i++)
    {
        threads[i].join();
    }

    return res;
}

long double parallelIntegralByPrecision(int threads_num, interval_t &interval, function_t func)
{
    unsigned long n = 2;
    long double delta = 1;
    long double res = 0, obt_res = 0;

    while (delta > interval.eps)
    {
        res = obt_res;
        obt_res = multithreading(threads_num, interval, n, func);
        n *= 2;
        delta = abs(res - obt_res);
    }

    return res;
}
