#!/bin/zsh

# 새 백준 문제 풀이 파이썬 파일을 만들어주는 스크립트.
#
# 문제 번호를 제공하면,
# - 해당 문제의 이름과 링크를 주석으로 포함하고
# - 문제 번호를 이름으로 가지는
# 파이썬 파일을 생성함.
#
# 사용법: ./new-boj.zsh [문제 번호] [닉네임]

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

if [ "$#" -eq 0 ]; then
  echo -n "백준 문제 번호: "
  read -r problem_number
  echo -n "음식 번호: "
  read -r dish_number
  echo -n "닉네임(hot/white): "
  read -r nick_name
else
  problem_number="$1"
  dish_number="$2"
  nick_name="$3"
fi


problem_link="https://www.acmicpc.net/problem/$problem_number"

problem_name=$(curl -s -N "$problem_link" | sed -n "s/^.*<title>\(.*\)<\/title>.*$/\1/p")

# today's date
today=$(date "+%Y/%m/%d")
today_folder=$(date "+%Y-%m-%d")

solution_file="$DIR/$today_folder/dish/dish${dish_number}_${nick_name}.py"



# python version
python_version=$(python3 --version)


echo "#" >> "$solution_file"
echo "#  $problem_name" >> "$solution_file"
echo "#  $problem_link" >> "$solution_file"
echo "#  Version: $python_version" >> "$solution_file"
echo "#" >> "$solution_file"
echo "#  Created by $nick_name on $today." >> "$solution_file"
echo "#" >> "$solution_file"
echo -e "\n\nfrom sys import stdin\n\nread = stdin.readline\n\nif __name__ == \"__main__\":\n    pass" >> "$solution_file"


echo "$problem_name"
echo "$solution_file"
