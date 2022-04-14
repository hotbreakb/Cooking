#
#  [1차] 비밀지도
#  https://programmers.co.kr/learn/courses/30/lessons/17681
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


def solution(n, arr1, arr2):
    combined_map = list(map(lambda values: values[0] | values[1], zip(arr1, arr2)))
    combined_map = list(map(lambda number: bin(number)[2:].zfill(n), combined_map))
    combined_map = list(map(lambda string: string.replace("1", "#"), combined_map))
    combined_map = list(map(lambda string: string.replace("0", " "), combined_map))
    return combined_map
