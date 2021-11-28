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
        long double y = func(x);
        res += y * step;
        x += step;
    }

    return res;
}

long double integralByPrecision(interval_t &interval, function_t func)
{
    unsigned long n = 2;
    long double res = 0;
    long double obt_res = midpoint(interval.begin, interval.end, n, func);

    while (abs(res - obt_res) > interval.eps)
    {
        res = obt_res;
        n *= 2;
        obt_res = midpoint(interval.begin, interval.end, n, func);
    }

    return res;
}

long double parallelIntegral(interval_t &interval, function_t func,
                             long double &res, int threads_num, int i,
                             mutex &res_mut)
{
    double delta = (interval.end - interval.begin) / threads_num;

    interval_t part = {
        .begin = interval.begin + i * delta,
        .end = 0,
        .eps = interval.eps
    };
    part.end = part.begin + delta;
    cout << "limits " << part.begin << " " << part.end << endl;

    long double local_res = trunc(integralByPrecision(part, func) * 1 / interval.eps) * interval.eps;

    res_mut.lock();
    res += local_res;
    res_mut.unlock();

    return res;
}

long double multithreading(int threads_num, interval_t &interval, function_t func)
{
    //cout << "parallel" << endl;
    long double res = 0;
    mutex res_mut;

    vector<thread> threads(threads_num);

    for (int i = 0; i < threads_num; i++)
    {
        threads[i] = thread(parallelIntegral, ref(interval), func, ref(res),
                            threads_num, i, ref(res_mut));
    }

    for (int i = 0; i < threads_num; i++)
    {
        threads[i].join();
    }

    return res;
}
