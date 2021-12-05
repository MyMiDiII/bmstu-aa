#ifndef INTEGRAL_H
#define INTEGRAL_H

struct interval_t{
    double begin;
    double end;
    double eps;
};

typedef long double(*function_t)(double);

long double integralByPrecision(interval_t &interval, function_t func);
long double parallelIntegralByPrecision(int threads_num, interval_t &interval, function_t func);

#endif // INTEGRAL_H
