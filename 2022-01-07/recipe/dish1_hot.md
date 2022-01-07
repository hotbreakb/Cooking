## 시간초과가 50%에서 나는 이유는!

기존에 짰던 소수 판별 함수는 숫자가 들어갈 때마다 2부터 반복해서 확인하기 때문에 속도가 느리다.<br>
이를 해결하기 위해서는 '에라토스테네스의 체'를 사용해야 한다. <br>
<br>
최댓값까지 True로 배열을 만든 뒤에, 소수의 배수는 False로 바꾼다.

<img width="687" alt="image" src="https://user-images.githubusercontent.com/64337152/148563286-802db21b-58a4-4d90-b743-846e9e40bd46.png">


```
def isPrime(num) -> bool:
    if num % 2 == 0:
        return False

    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True
```

```
def makeSieveList():
    for num in range(2, MAX_NUM + 1):
        if sieve[num]: # 소수라면
            for notSieve in range(num * 2, MAX_NUM + 1, num): # 소수의 배수는 전부 False
                sieve[notSieve] = False
```
