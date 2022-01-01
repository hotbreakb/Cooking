## UCPC는 무엇의 약자일까?

#### 입력

문자열을 입력받되, 대문자 알파벳인 것만 추려내어 리스트로 저장한다.

```python
uppercase_list = list(filter(lambda x: 65 <= ord(x) <= 90, read().rstrip()))
```

- 예시 입력
  ```
  Union of Computer Programming Contest club contest
  ```

#### 알고리즘

UCPC가 순서대로 만들어 지는지를 확인하면 된다.

- 물론 UCPC 사이에 다른 대문자 알파벳이 들어가도 상관없다.
  > 문자열이 주어지면 이 문자열을 적절히 축약해서 "UCPC"로 만들 수 있는지 확인하는 프로그램을 만들어보자.

```python
ucpc = "UCPC"
    index = 0
    for char in uppercase_list:
        if ucpc[index] == char:
            index += 1
        if index == 4:
            print("I love UCPC")
            break
    else:
        print("I hate UCPC")
```
