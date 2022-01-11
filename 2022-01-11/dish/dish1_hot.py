#
#  1107번: 리모컨
#  https://www.acmicpc.net/problem/1107
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/11.
#


from sys import stdin

read = stdin.readline

INIT_CHANNEL = 100


def getMinimumTouch(target: str, notworkingNums: int, notworkingList: list) -> int:
    targetInt = int(target)
    if targetInt == INIT_CHANNEL:
        return 0

    # +, -만 되는 리모컨
    if notworkingNums == 10:
        return abs(INIT_CHANNEL - targetInt)

    # 잘 눌리는 숫자 리스트
    workingNumList = sorted(set([num for num in range(0, 10)]) - notworkingList)
    targetLen = len(target)
    nearNumList, nearNumDiffer = [], ()

    # 숫자 하나만 되는 리모컨
    if notworkingNums == 9:
        nearNumList = [
            int(str(workingNumList[0]) * targetLen),
            int(str(workingNumList[0]) * (targetLen + 1)),
        ]
        if targetInt - 1 > 0:
            nearNumList.append(int(str(workingNumList[0]) * (targetLen - 1)))

        bestNearNumDiffer = 10000000
        for nearnum in nearNumList:
            if abs(nearnum - targetInt) < bestNearNumDiffer:
                bestNearNumDiffer = abs(nearnum - targetInt)
                nearNumDiffer = (nearnum, bestNearNumDiffer)

        return min(
            len(str(nearNumDiffer[0])) + abs(nearNumDiffer[0] - targetInt),
            abs(INIT_CHANNEL - targetInt),
        )

    # 1~8개가 안 눌리는 리모컨
    oneBiggerNum, sameNum, oneLessNum = "", "", ""
    for targetIndex in range(len(target)):
        targetIndexNumInt = int(target[targetIndex])
        tmpWorkingList = sorted(workingNumList + [targetIndexNumInt])

        # biggerNum, lessNum = None, None
        # if tmpWorkingList[-1] != targetIndexNumInt:
        #     biggerNum = tmpWorkingList[tmpWorkingList.index(targetIndex) + 1]
        # if tmpWorkingList[0] != targetIndexNumInt:
        #     lessNum

        if targetIndexNumInt + 1 in workingNumList:
            oneBiggerNum += targetIndexNumInt + 1
            for _ in range(len(target) - (targetIndex + 1)):
                oneBiggerNum += workingNumList[0]
        if targetIndexNumInt in workingNumList:
            sameNum += targetIndexNumInt
        if targetIndexNumInt - 1 in workingNumList:
            oneLessNum += targetIndexNumInt - 1
            for _ in range(len(target) - (targetIndex + 1)):
                oneBiggerNum += workingNumList[-1]

        if oneBiggerNum != "":
            nearNumList.append(oneBiggerNum)
        if oneLessNum != "":
            nearNumList.append(oneLessNum)

        if sameNum == "":
            break

        oneBiggerNum = sameNum
        oneLessNum = sameNum


targetChannel = input().rstrip()
notwWorkingNums = int(input().rstrip())

# 안 고장난 리모컨
if notwWorkingNums == 0:
    print(min(len(targetChannel), abs(INIT_CHANNEL - int(targetChannel))))
    exit()

notWorkingList = set(map(int, input().split()))
print(getMinimumTouch(targetChannel, notwWorkingNums, notWorkingList))
