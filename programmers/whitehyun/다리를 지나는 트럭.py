#
#  다리를 지나는 트럭
#  https://programmers.co.kr/learn/courses/30/lessons/42583
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/12.
#

from collections import deque


def solution(bridge_length, weight, truck_weights):

    # == 변수 선언 ==
    """
    bridge_weight: 현재 다리에 놓인 트럭의 총 무게
    time: 지나온 시간 - 정답 변수
    queue: 트럭이 들어갈 다리(큐)
    truck_queue: 다리에 지나가기 위해 기다리고 있는 트럭 큐
    """
    bridge_weight = 0
    time = 0
    queue = deque()
    truck_queue = deque(truck_weights)

    # == 초기 세팅 ==
    """
    queue element:
        list:
            index 0: truck weight
            index 1: move distance
    """
    queue.append([truck_queue.popleft(), 1])
    bridge_weight += queue[0][0]
    time += 1

    while queue:  # 다리에 트럭이 존재하지 않을 때 까지
        if not truck_queue:  # 다리를 지나가기 위해 기다리는 트럭은 없는 경우
            # 가장 끝의 트럭이 다리를 지나올 때까지의 시간을 구하면 완료됨
            truck_weight, move_distance = queue.pop()
            time_passed = bridge_length - move_distance + 1
            time += time_passed
            break
        # 기다리는 트럭이 있지만 이미 다리가 버티는 데 포화상태인 경우
        elif bridge_weight + truck_queue[0] > weight:
            # 앞의 트럭이 다 지나올 시간까지를 구하고, 다른 트럭들의 시간도 그만큼 합산
            done_truck_weight, move_distance = queue.popleft()
            bridge_weight -= done_truck_weight  # 다리를 지났기 때문에 다리에 있는 트럭의 무게에서 뺌
            time_passed = bridge_length - move_distance + 1
            time += time_passed
            for i in range(len(queue)):
                queue[i][1] += time_passed

            # 그래도 포화상태라면 다시 반복문 실행..
            if bridge_weight + truck_queue[0] > weight:
                continue

        # 기다리는 트럭이 있고 다리도 트럭을 수용할 수 있는 상태인 경우
        else:
            # 다리에 있는 트럭은 한 칸씩 이동
            for i in range(len(queue)):
                queue[i][1] += 1
            # 앞의 트럭이 다리를 지났다면 다리의 총 무게에서 트럭 무게를 뺌
            if queue[0][1] > bridge_length:
                done_truck_weight = queue.popleft()[0]
                bridge_weight -= done_truck_weight
            time += 1  # 시간도 1 추가

        # 트럭이 들어올 수 있으므로 다리에 트럭을 놓자!
        truck_weight = truck_queue.popleft()
        bridge_weight += truck_weight
        queue.append([truck_weight, 1])

    return time


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
