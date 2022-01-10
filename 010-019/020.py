""" 
index: 020
problem: 100! 의 자릿수를 모두 더하면? 
"""


def main():
    total = 1

    for i in range(2, 101):
        total *= i

    return eval("+".join(list(str(total))))


print("\n", main())
