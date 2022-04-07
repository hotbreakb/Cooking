n = 3000
isPrimeList = [False, False] + [True]*(n-1)


def solution(nums):
    makePrimeList()
    answer = 0

    odds, evens = [], []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    for o1 in range(len(odds)):
        for o2 in range(o1+1, len(odds)):
            for o3 in range(o2+1, len(odds)):
                if isPrimeList[odds[o1]+odds[o2]+odds[o3]]:
                    answer += 1
        for e1 in range(len(evens)):
            for e2 in range(e1+1, len(evens)):
                if isPrimeList[odds[o1]+evens[e1]+evens[e2]]:
                    answer += 1

    return answer


def makePrimeList():
    global isPrimeList
    primes = []

    for i in range(2, n+1):
        if not isPrimeList[i]:
            continue
        primes.append(i)
        for j in range(2*i, n+1, i):
            isPrimeList[j] = False


nums = [1, 2, 7, 6, 4]
print(solution(nums))
