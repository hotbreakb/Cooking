#
#  스킬트리
#  https://programmers.co.kr/learn/courses/30/lessons/49993
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/16.
#

def solution(skill, skill_trees):
    set_skill_trees = []
    result = 0

    for order_skill in skill_trees:
        set_skill_trees.append(''.join(list(filter(
            lambda one_skill_tree: one_skill_tree in skill, order_skill))))

    for set_skill in set_skill_trees:
        set_skill_len = len(set_skill)
        if set_skill == skill[:set_skill_len]:
            result += 1

    return result


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
