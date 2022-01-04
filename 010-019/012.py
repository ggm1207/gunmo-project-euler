""" 
index: 012
problem: 500개 이상의 약수를 갖는 가장 작은 삼각수는?
"""


def get_division(n):
    divisors = set()

    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return divisors


def main():

    add_num = 2
    triangle_num = 1

    while len(get_division(triangle_num)) < 500:
        triangle_num += add_num
        add_num += 1

    return triangle_num


print("\n", main())
