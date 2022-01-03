""" 
index: 007
problem: 10001번째의 소수
"""


def main(N=10001):
    primes = [2]
    num = 3

    while len(primes) != N:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)

        num += 1

    return primes[-1]


print("\n", main())
