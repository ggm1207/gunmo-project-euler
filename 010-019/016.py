""" 
index: 016
problem: 21000의 각 자릿수를 모두 더하면?
"""


def main(N=1000):
    return eval("+".join(list(str(pow(2, 1000)))))


print("\n", main())
