#
#  위장
#  https://programmers.co.kr/learn/courses/30/lessons/42578
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/18.
#

def solution(clothes):
    answer = 1
    cloth_dict = dict()
    for cloth, cloth_type in clothes:
        if cloth_type not in cloth_dict.keys():
            cloth_dict[cloth_type] = [cloth]
        else:
            cloth_dict[cloth_type].append(cloth)

    for cloth_type in cloth_dict.keys():
        answer *= len(cloth_dict[cloth_type])+1

    return answer-1


clothes = [["crowmask", "face"], [
    "bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
