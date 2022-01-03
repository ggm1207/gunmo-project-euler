""" 
index: 010
problem: 이백만 이하 소수의 합
"""


def main(N=2000000):
    primes = [False, False] + [True] * (N - 1)

    for k in range(2, int(N ** 0.5 + 1.5)):
        if primes[k]:
            primes[k * 2 :: k] = [False] * ((N - k) // k)

    return sum([x for x in range(N + 1) if primes[x]])


print("\n", main())
