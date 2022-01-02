""" 
index: 004
problem: 세자리 수를 곱해 만들 수 있는 가장 큰 대칭수
"""


def is_mul_of_hundreds(n: int):
    for i in range(100, 1000):
        if n % i == 0:
            if n / i < 1000:
                return True
    return False


def is_pelindrom(n: str):
    l, r = 0, len(n) - 1

    while l <= r and n[l] == n[r]:
        l, r = l + 1, r - 1

    return r <= l


def main():
    minimum_range = 100 * 100
    maximum_range = 999 * 999

    print(maximum_range)

    while maximum_range >= minimum_range:

        if not is_pelindrom(str(maximum_range)):
            maximum_range -= 1
            continue

        if not is_mul_of_hundreds(maximum_range):
            maximum_range -= 1
            continue

        break

    return maximum_range


print("\n", main())
