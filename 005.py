""" 
index: 005
problem: 1~20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
"""


import math
from functools import reduce


def lcm(a, b):
    return a * b // math.gcd(a, b)


def main(N=20):
    return reduce(lambda x, y: lcm(x, y), range(2, N + 1))


print("\n", main())
