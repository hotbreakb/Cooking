![algorithm](algorithm.png)

# Study

코딩테스트 마스터를 위한 알고리즘 스터디. 취뽀할 때 까지 가자!

## ⚖️ 조건 및 방법

### 조건

1. 파이썬을 사용할 줄 아는가?
2. 꾸준히 실천할 수 있는가?
3. git과 github를 사용할 줄 아는가?

> 위에 하나라도 포함이 안된다면 참여 ❌

### 참여 방법

1. 레포지토리를 `fork`한다.
2. [폴더 구조](#📁-폴더-구조-및-파일-규칙)에 맞게 파일을 만든다.
3. 자신이 푼 문제의 소스코드를 업로드한다.
4. [commit convention](#git-컨벤션)에 맞춰 커밋을 작성한다.
5. `Pull Request`를 보낸다.
6. 다른 사람들의 소스코드를 분석하며 자유롭게 코드리뷰를 진행한다.

## 📁 폴더 구조 및 파일 규칙

```
 📁 Cooking
 ┣ 📂 boj
 ┃ ┗ 📂 (users)
 ┃   ┃ 📝 (problem_number).py
 ┃   ┗ 📝 ...
 ┃
 ┣ 📂 programmers
 ┃ ┗ 📂 (users)
 ┃   ┗ 📂 (level) - optional
 ┃     ┃ 📝 (problem_name).py
 ┃     ┗ 📝 ...
 ...
```

### 스크립트 파일

되도록 `pgs.zsh`, `boj.zsh`와 같은 소스코드 자동화 스크립트를 사용한다.

> boj.zsh는 jq를 사용하기 때문에, 없는 경우 설치할지 물어보게 됩니다. 당황하지 마시고 설치해주시면 됩니다.

#### 예시 ⤵️

- boj

  ```
  ./boj.zsh 12953 WhiteHyun
  ./boj.zsh 1001 hotbreakb
  ```

- programmers
  ```
  ./pgs.zsh 49938 hotbreakb
  ./pgs.zsh https://programmers.co.kr/learn/courses/30/lessons/49994 WhiteHyun
  ```
  - pgs.zsh는 (문제주소) (닉네임) 또는, (문제번호) (닉네임)과 같이 주소나 번호 아무거나 넣어서 활용할 수 있습니다.

## 🤞 Convention

### git 컨벤션

푼 문제를 커밋할 때는 **반드시** 다음과 같이 작성하도록 한다.

```
git commit -m "[플랫폼] 문제명" -m "문제주소"
```

- 플랫폼별 양식 통일

  - 백준: [BOJ]
  - 프로그래머스: [PGS]
  - 코드포스: [CFS]
  - 리트코드: [LCE]
  - 그 외: [ETC]

#### 예시 ⤵️

```
git commit -m "[BOJ] A+B" -m "https://www.acmicpc.net/problem/1000"
```

### PR 규칙

- 제목은 commit과 유사하게 작성하되, 끝에 `/ (닉네임)`을 작성한다.
  - ex) [BOJ] A+B / WhiteHyun
- 여러 문제를 풀었을 경우 쉼표(`,`)를 기준으로 나누어 작성한다.
  - ex) [PGS] 나누어 떨어지는 숫자 배열, 신고 결과 받기 / WhiteHyun
- 문제를 어떻게 풀었는지 아이디어를 설명한다.
- 문제에 대한 회고를 작성한다. (`optional`)

이해가 되지 않아도 `template`이 있으므로 각 항목에 맞게 작성하면 된다!

## 📔 References

1. [배너 디자인 아이디어 - Avocado34님](https://github.com/Avocado34)
2. [💯 알고리즘 및 코딩 테스트 문제 풀이 챌린지 100 📝](https://github.com/ellynhan/challenge100-codingtest-study/blob/master/README.md)
