""" 
index: 008
problem: 1000자리 수 안에서 연속된 13개 숫자 곱의 최댓값
"""


def main(N=100):
    pow_and_sum = sum([pow(i, 2) for i in range(1, N + 1)])
    sum_and_pow = pow(sum(range(1, N + 1)), 2)
    return abs(pow_and_sum - sum_and_pow)


print("\n", main())
