""" 
index: 015
problem: 20×20 격자의 좌상단에서 우하단으로 가는 경로의 수
"""
import math


def main(N=20):
    return math.comb(N * 2, N)


print("\n", main())
