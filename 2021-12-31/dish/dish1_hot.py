import sys

input = sys.stdin.readline


def findBaByShark():
    global babySharkPosX, babySharkPosY
    

    for _ in range(spaceWidth):
        newLine = list(map(int,input().rsplit()))
        if 9 in newLine:
            babySharkPosY = newLine.index(9)
            return

        babySharkPosX += 1

def eatSomeFishes():
    


def dfs(x, y):
    if x < 0 or y < 0 or x > spaceWidth - 1 or y > spaceWidth - 1:
        return False

    # 최단 거리에 있는 걸 기록하는 법을 모르겠다. 원래는 1이나 0을 표시하면서 갔었는데 이건 어떻게 해야 하지?
    if ground[x][y] == 1:
        ground[x][y] = 0

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

spaceWidth = int(input().rstrip())
space = []
babySharkSize = 2 # 아기 상어의 처음 크기
babySharkGazy = 0 # 아기 상어의 크기와 같아지면 상어의 크기가 +1
babySharkPosX, babySharkPosY = 0,0
findBaByShark()


print(babySharkPosX, babySharkPosY)