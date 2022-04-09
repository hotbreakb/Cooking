from collections import Counter


def solution(participant, completion):
    completionCounter = Counter(completion)

    for key, value in Counter(participant).items():
        if key not in completionCounter.keys() or completionCounter[key] != value:
            return key


print(solution(["marina", "josipa", "nikola", "marina", "filipa"], [
      "josipa", "filipa", "marina", "nikola"]))
