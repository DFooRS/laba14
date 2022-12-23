#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def fun1(a):
    def fun2(b):
        f = a * math.pow(b, a)
        l = f"Для значений {a},{b} функция f(a,b) = {f}"
        return l

    return fun2


if __name__ == "__main__":
    test_fun = fun1(2)
    print(test_fun(3))