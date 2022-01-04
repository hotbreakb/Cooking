## 약수의 합 2

이건 아무리 봐도 시간 초과가 나와서 다른 사람의 코드를 보고 풀었다.
100번 생각해봐도 못 풀었을 거 같다.

### 맞았습니다

9까지 약수의 합을 구할 때, [1은 9번(9//1), 2는 4번(9//2), 3은 3번(9//3), 4는 2번(9//4), ..., 9는 9번(9//1)] 나온다.
그래서 이것들을 더해주면 된다. [1x9, 2x4, 3x3, 4x2, ..., 9x1]

### 시간 초과

약수 찾는 과정이 O(N<sub>3/2</sub>)가 나와서 시간 초과가 뜬다. 제출하면 그냥 탈락😄

```
def getDivisorSum(num):
    divisorList = []

    for i in range(1, int((num) ** (1 / 2)) + 1):
        if num % i == 0:
            divisorList.append(i)
            if i ** 2 != num:
                divisorList.append(num // i)

    return sum(divisorList)
```
