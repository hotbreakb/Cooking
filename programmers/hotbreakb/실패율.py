def solution(N, stages):
    answer = []
    levelpercentage = dict()
    levelCount = [0] * (N+1)

    for user in stages:
        if user > N:
            continue
        levelCount[user] += 1

    allUser = len(stages)

    for level in range(1, N+1):
        if allUser < 1:
            levelpercentage[level] = 0
        else:
            levelpercentage[level] = levelCount[level]/allUser
            allUser -= levelCount[level]

    levelpercentage = sorted(levelpercentage.items(),
                             key=lambda item: (-item[1], item[0]))

    answer = [level for level, percentage in levelpercentage]

    return answer


N = 10
stages = [4, 4, 4, 4, 5]
print(solution(N, stages))
