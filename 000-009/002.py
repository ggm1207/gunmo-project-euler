""" 
index: 002
problem: 피보나치 수열에서 4백만 이하이면서 짝수인 항의 합
"""


def main(N=4000000):
    fib_n = 1
    fib_n1 = 2

    total = 0

    while fib_n1 <= N:
        if fib_n1 % 2 == 0:
            total += fib_n1

        fib_n, fib_n1 = fib_n1, fib_n + fib_n1

    return total


print("\n", main())
