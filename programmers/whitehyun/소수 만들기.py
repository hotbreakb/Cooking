#
#  소수 만들기
#  https://programmers.co.kr/learn/courses/30/lessons/12977
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/07.
#


def solution(nums):
    prime_count = 0
    prime_list = [True] * 2998  # 1000+999+998 + 1
    prime_list[0] = prime_list[1] = False

    # 에라토스테네스의 체
    for i in range(2, 55):  # 55 == int(2997 ** 0.5) + 1
        if prime_list[i]:
            for j in range(2 * i, 2998, i):
                prime_list[j] = False

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                number = nums[i] + nums[j] + nums[k]
                if prime_list[number]:
                    prime_count += 1
    return prime_count


if __name__ == "__main__":
    for nums in [[1, 2, 3, 4], [1, 2, 7, 6, 4]]:
        print(solution(nums))
