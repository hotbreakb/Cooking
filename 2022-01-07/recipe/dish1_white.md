## 골드바흐의 추측

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있을까? 에서 시작된 문제이다.

### 문제의 요구사항

해당 문제에서 요구하는 시간은 1초이다.
테스트 케이스는 `1≤T≤100,000`이며, 짝수 정수 N의 범위는 `6≤N≤1,000,000`이다.
만약 약수를 정석대로 구현하게 된다면 최악의 케이스는 연산횟수가 `100,000,000,000`회이다.
연산횟수를 획기적으로 줄일 수 있는 방법을 마련해보자.

### 구현

#### 숫자 리스트

N+1의 크기를 가진 리스트를 `True`로 초기화 한다.

> N+1이 아닌 N으로 해도 상관 없으나 계산을 편하게 하기 위해 +1을 취했다.

2부터 N<sup>0.5</sup>+1 까지 반복하며 생기는 수를 **i**라 하면
**i**를 인덱스로 하였을 때 숫자 리스트의 값이 `True`라면,
그 수는 소수이며, 해당 숫자를 제외하고 그 수의 배수를 인덱스로 하여 값을 `False`로 바꾼다.
반복하면 `True`값인 인덱스는 전부 소수이다.

#### 소수 리스트

숫자 리스트에서 값이 True인 인덱스를 추린다.

#### 출력

0을 입력받을 때 까지 반복하며, 입력받은 수는 소수 리스트에서 값을 가져와 뺄셈한 수가 소수이면 출력한다.