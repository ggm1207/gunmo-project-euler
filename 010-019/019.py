""" 
index: 019
problem: 20세기에서, 매월 1일이 일요일인 경우는 몇 번?
- 20세기(1901 1월 1일 ~ 2000년 12월 31일)
- (욕망) datetime으로 풀고싶다.
"""

month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def is_leapyear(year):
    return year % 4 == 0 and ((year % 100 == 0) and (year % 400 == 0))


def main():
    answer = 0
    monday_key = 1

    for year in range(1901, 2001):
        for i in range(1, 13):
            if is_leapyear(year) and i == 2:
                monday_key = (monday_key + 29) % 7
                continue

            monday_key = (monday_key + month[i]) % 7

            if monday_key == 0:
                answer += 1

    return answer


print("\n", main())
