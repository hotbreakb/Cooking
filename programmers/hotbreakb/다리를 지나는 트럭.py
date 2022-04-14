#
#  다리를 지나는 트럭
#  https://programmers.co.kr/learn/courses/30/lessons/42583
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/12.
#

from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 1
    doneTrucks = 0
    movingOnBridge = deque()
    movingOnBridgeWeights = 0
    truckIndex = 0

    while doneTrucks < len(truck_weights):
        for truckInfo in movingOnBridge:
            truckInfo[1] += 1
        if truckIndex < len(truck_weights) and truck_weights[truckIndex] + movingOnBridgeWeights <= weight:
            movingOnBridge.append([truck_weights[truckIndex], 1])
            movingOnBridgeWeights += truck_weights[truckIndex]
            truckIndex += 1
        if movingOnBridge[0][1] == bridge_length:
            movingOnBridgeWeights -= movingOnBridge.popleft()[0]
            doneTrucks += 1
        time += 1

    return time


bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(bridge_length, weight, truck_weights))
