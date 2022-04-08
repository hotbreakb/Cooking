SIZE = 10001


def solution(answers):
    success = {1: 0, 2: 0, 3: 0}
    user1 = [1, 2, 3, 4, 5]*2001
    user2 = [2, 1, 2, 3, 2, 4, 2, 5]*1251
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1001

    for i in range(len(answers)):
        a = answers[i]
        if a == user1[i]:
            success[1] += 1
        if a == user2[i]:
            success[2] += 1
        if a == user3[i]:
            success[3] += 1

    success = list(dict(filter(lambda item: item[1] >= max(
        success.values()), success.items())).keys())

    return success


answers = [1, 2, 3]
print(solution(answers))
