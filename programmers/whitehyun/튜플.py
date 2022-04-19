#
#  튜플
#  https://programmers.co.kr/learn/courses/30/lessons/64065
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/19.
#


def solution(s):
    answer = []
    # == 집합 값 추출 ==
    value_list = s[2:-2].split("},{")
    value_list = sorted(value_list, key=len)

    for sequence in value_list:
        # == 집합 내 원소 값 추출 ==
        for element in map(int, sequence.split(",")):
            if element not in answer:
                answer.append(element)
    return answer


if __name__ == "__main__":
    inputs = [
        "{{2},{2,1},{2,1,3},{2,1,3,4}}",
        "{{1,2,3},{2,1},{1,2,4,3},{2}}",
        "{{20,111},{111}}",
        "{{123}}",
        "{{4,2,3},{3},{2,3,4,1},{2,3}}",
    ]
    y = [[2, 1, 3, 4], [2, 1, 3, 4], [111, 20], [123], [3, 2, 4, 1]]

    for predict, answer in zip(map(lambda value: solution(value), inputs), y):
        print(predict)
        assert predict == answer
