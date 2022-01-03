""" 
index: 009
problem: a + b + c = 1000 이 되는 피타고라스 수
"""


def is_triangle(a, b, c):
    return pow(a, 2) + pow(b, 2) == pow(c, 2)


def main(N=1000):
    for c in range(N, 0, -1):
        for b in range(N - c, 0, -1):
            for a in range(N - c - b, 0, -1):
                if a + b + c == N and is_triangle(a, b, c):
                    return a * b * c


print("\n", main(N=1000))
