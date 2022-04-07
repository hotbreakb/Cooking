def solution(lottos, win_nums):
    success = 0
    zeros = 0

    for num in lottos:
        if num in win_nums:
            success += 1
        elif num == 0:
            zeros += 1

    return getRank(success, zeros)


def getRank(success: int, zeros: int) -> list:
    maxRank = 7 - (success + zeros)
    minRank = 7 - success

    if maxRank > 6:
        maxRank = 6
    elif maxRank < 1:
        maxRank = 1
    if minRank > 6:
        minRank = 6
    elif minRank < 1:
        minRank = 1

    return [maxRank, minRank]


lottos = [1, 1, 1, 1, 1, 1]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))
