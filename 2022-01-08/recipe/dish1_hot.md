## 사탕 게임

<img width="715" alt="image" src="https://user-images.githubusercontent.com/64337152/148648801-9d278828-3a98-4fdb-9657-59393bcbfb5e.png">

1. switchListValue()로 칸 좌우에 있는 값을 바꾼다.
2. getCountMaxChar()에서 전달받은 리스트와 [행과 열이 바뀐 리스트](https://m.blog.naver.com/cjh226/221328286730)를 findMaxChar()에 전달한다.
   - 행과 열이 바뀐 리스트르 구할 때는 `list(x) for x in zip(*board)]` 이렇게 작성한다. zip으로 나온 tuple을 list로 만들어준다.
4. 왼쪽부터 오른쪽으로 이동하면서 문자가 같은 가장 긴 길이를 구한다.
