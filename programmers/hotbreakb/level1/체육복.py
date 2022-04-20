def solution(n, lost, reserve):
    isReserveList = [False] * (n+1)

    lostAndReserveStudents = set(lost) & set(reserve)
    lost = set(lost)-set(lostAndReserveStudents)
    reserve = set(reserve)-set(lostAndReserveStudents)

    losted = len(lost)

    for r in reserve:
        isReserveList[r] = True

    for l in lost:
        if isReserveList[l]:
            isReserveList[l] = False
            losted -= 1
        elif l-1 > 0 and isReserveList[l-1]:
            isReserveList[l-1] = False
            losted -= 1
        elif l+1 <= n and isReserveList[l+1]:
            isReserveList[l+1] = False
            losted -= 1

    return n-losted


n = 5
lost = [1]
reserve = [1, 5]
print(solution(n, lost, reserve))
