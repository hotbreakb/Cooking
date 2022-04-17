#
#  스킬트리
#  https://programmers.co.kr/learn/courses/30/lessons/49993
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/17.
#


def solution(skills: str, skill_trees: list) -> int:
    count = 0  # 정답 변수
    for tree in skill_trees:
        index = -1
        for skill in skills:

            temp_index = tree.find(skill)  # 스킬이 있는지 확인
            if temp_index == -1:  # 찾지 못했다면 값을 크게 만들어버림
                index = 21
                continue

            if index < temp_index:  # 순차적으로 스킬을 구성했다면 index 업데이트
                index = temp_index
            else:  # 아니면 스킬트리 잘못 짠 거임!
                break
        else:  # 정확한 스킬트리라면 for-else문에 의해 count 증가
            count += 1

    return count


if __name__ == "__main__":
    skills = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skills, skill_trees))
