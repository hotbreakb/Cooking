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
        skill_index_list = []
        for skill in skills:
            temp_index = tree.find(skill)  # 인덱스를 구함
            if temp_index == -1:  # 못찾았다면 21이라는 큰 값을 줌
                temp_index = 21
            skill_index_list.append(temp_index)
        # 오름차순이라면 정확한 스킬트리!
        if sorted(skill_index_list) == skill_index_list:
            count += 1

    return count


if __name__ == "__main__":
    skills = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skills, skill_trees))
