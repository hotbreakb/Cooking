#
#  13305번: 주유소
#  https://www.acmicpc.net/problem/13305
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/01.
#

from sys import stdin

input = stdin.readline

def getMinPrice(dList, pList):
    # 총 가야 하는 거리
    sumOfDistance = sum(dList)
    # 저렴한 가격대로 정렬
    inexpensivePriceList = sorted(pList)
    # 구매한 기름 리터 수
    # 구매한 곳의 맨끝 위치
    perchasedOilLastIndex = len(pList) - 1
    # 저렴한 가격대부터 구매한다.
    indexOfInexpensivePriceList = 0
    # 구매한 가격
    sumOfOilPrice = 0

    while sumOfDistance > 0:
        # 가장 저렴한 곳의 기름 가격
        oilPrice = inexpensivePriceList[indexOfInexpensivePriceList]
        # 저렴한 기름이 있는 곳의 위치
        locationOfOil = pList.index(oilPrice)
        # 저렴한 곳에서 구매했음을 표기한다
        perchaseOilLiter = sum(dList[locationOfOil:perchasedOilLastIndex+1])
        sumOfOilPrice += perchaseOilLiter * oilPrice
        sumOfDistance -= perchaseOilLiter
        # print(oilPrice, perchasedOilLastIndex, perchaseOilLiter)
        
        perchasedOilLastIndex = min(locationOfOil-1, perchasedOilLastIndex)
        indexOfInexpensivePriceList += 1
    
    return sumOfOilPrice




# 사용자의 값 입력
_ = int(input().rstrip())
distanceList = list(map(int, input().split()))
priceList = list(map(int, input().split()))

print(getMinPrice(distanceList, priceList))