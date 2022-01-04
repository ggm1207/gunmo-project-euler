""" 
index: 014
problem: 백만 이하로 시작하는 우박수 중 가장 긴 과정을 거치는 것은?
"""


def main(N=1000000):
    visited = dict()
    max_cnt = 0
    max_n = 0

    for n in range(N, 0, -1):
        temp = n
        cnt = 0

        while n != 1:
            n = n // 2 if n % 2 == 0 else 3 * n + 1

            if n not in visited:
                visited[n] = cnt
                cnt += 1
                continue

            if cnt > visited[n]:
                visited[n] = cnt
                cnt += 1
            else:
                break

        if n == 1 and cnt > max_cnt:
            max_cnt = cnt
            max_n = temp

    return max_n


print("\n", main())
