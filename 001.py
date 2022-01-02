""" 
index: 001
problem: 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면?
"""


def total():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


def main(N=1000):
    sum_03 = (3 + 999) / 2 * int(N // 3)
    sum_05 = (5 + 995) / 2 * int(N // 5 - 1)
    sum_15 = (15 + 990) / 2 * int(N // 15)

    return int(sum_03 + sum_05 - sum_15)


print("\n")
print("\n", main())
print("\n", total())
