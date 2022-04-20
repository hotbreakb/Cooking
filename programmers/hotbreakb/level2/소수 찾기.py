#
#  소수 찾기
#  https://programmers.co.kr/learn/courses/30/lessons/42839
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/18.
#

from itertools import permutations

MAX_NUM = 100
prime_list = [False] * (MAX_NUM+1)  # 0 ~ MAX_NUM
prime_list[1] = True


def solution(numbers):
    answer = 0

    number_list = list(permutations(numbers))
    return answer


def make_prime_list():
    for i in range(2, int((MAX_NUM+1)**(0.5))+1):
        if not prime_list[i]:
            for j in range(i*2, MAX_NUM+1, i):
                prime_list[j] = True


prime_list = make_prime_list()

numbers = input().rstrip()
print(solution(numbers))
