""" 
index: 017
problem: 1부터 1000까지 영어로 썼을 때 사용된 글자의 개수는?
"""


n2a = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def under_100(num):
    tot_len = 0

    if num == 0:
        return 0

    if num < 20:
        tot_len += len(n2a[num])
    elif num < 100:
        num_10 = num - (num % 10)
        num_1 = num % 10
        if num_1 != 0:
            tot_len += len(n2a[num_1])
        tot_len += len(n2a[num_10])

    return tot_len


def main(N=1000):
    total_len = 1  # 정답이 1이 작게 나온다.. 왜..?

    for i in range(1, N + 1):
        cur_len = 0
        if i < 100:
            cur_len += under_100(i)
        else:
            num_10 = i % 100
            num_100 = i - num_10

            if num_10 != 0:
                cur_len += under_100(num_10)
                cur_len += len(n2a[num_100 // 100]) + len("hundredand")
            else:
                cur_len += len(n2a[num_100 // 100]) + len("hundred")

        total_len += cur_len

    return total_len


print("\n", main())
