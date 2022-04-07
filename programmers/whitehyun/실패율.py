#
#  실패율
#  https://programmers.co.kr/learn/courses/30/lessons/42889
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/07.
#


def solution(N, stages):
    # stage_list: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
    # total_stage_list: 스테이지에 도달한 플레이어 수
    stage_list = [0] * (N + 1)
    total_stage_list = [0] * (N + 1)

    # stage별 빈도를 구함
    for stage in stages:
        if stage > N:
            continue
        stage_list[stage] += 1

    # 스테이지 누적합을 구함
    total_stage_list[1] = len(stages)
    for i in range(2, N + 1):
        total_stage_list[i] = total_stage_list[i - 1] - stage_list[i - 1]

    # key: stage, value: 실패율
    failure_rate_dict = {}
    for i in range(1, N + 1):
        if total_stage_list[i] == 0:
            failure_rate_dict[i] = 0
            continue
        failure_rate_dict[i] = stage_list[i] / total_stage_list[i]

    # 실패율이 가장 높은 값으로 튜플 값 정렬
    sorted_failure_rate_list = sorted(
        failure_rate_dict.items(), key=lambda items: -items[1]
    )
    # 정렬된 값에서 스테이지를 빼옴
    sorted_stage_list = list(map(lambda items: items[0], sorted_failure_rate_list))
    return sorted_stage_list


if __name__ == "__main__":
    N = [5, 4, 6]
    stages = [[2, 1, 2, 6, 2, 4, 3, 3], [4, 4, 4, 4, 4], [1, 2, 3, 4, 5]]
    for n, stage in zip(N, stages):
        print(solution(n, stage))
