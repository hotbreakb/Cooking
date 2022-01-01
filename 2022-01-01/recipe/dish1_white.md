## 주유소

전형적인 그리디 알고리즘 문제.
각 도시 사이에 거리가 있으며, 왼쪽부터 오른쪽까지 가는데 최소한의 금액으로 갈 수 있는 코드를 짜야한다.

#### 입력

```python
city_count = int(read()) # 도시의 수
distance_list = list(map(int, read().split())) # 각 도시 사이의 거리
gas_list = list(map(int, read().split())) # 도시의 기름 가격
```

- 예시 입력
  ```
  4
  2 3 1
  5 2 4 1
  ```
  ```
  4
  3 3 4
  1 1 1 1
  ```

#### 사용자 정의 변수

최소의 가격을 책정하기 위해 총 지불 가격을 저장할 변수와
가장 싼 기름의 가격을 저장할 변수를 아래와 같이 선언하였다.

```python
total_price = 0  # 총 지불한 가격
min_gas_price = gas_list[0]  # 기름 가격
```

#### 알고리즘

각 도시 사이의 거리 리스트를 for문으로 반복한다.

```python
for i in range(city_count - 1):  # O(n)
    # 만약 다음 도시의 기름이 더 쌀 경우
    if min_gas_price > gas_list[i]:
        min_gas_price = gas_list[i]
    total_price += min_gas_price * distance_list[i]
```

일일히 반복하며 거리와 기름값을 곱하여 계산하되, 다음 도시의 기름값이 전에 저장해놓은 최소기름가격보다 싼 경우에는 최소기름가격을 바꾼 뒤 다시 계산한다.
