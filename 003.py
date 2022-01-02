""" 
index: 003
problem: 가장 큰 소인수 구하기, 600851475143의 소인수 중에서 가장 큰 수를 구하세요.
"""


def main(N=600851475143):
    flag = False
    prime = 1
    for i in range(2, N // 2):
        if N % i == 0:
            flag = True
            prime = i
            break
    if flag:
        return max(prime, main(N // prime))
    else:
        return N


print("\n", main())
