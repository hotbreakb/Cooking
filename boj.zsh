#!/bin/zsh

# 새 백준 문제 풀이 파이썬 파일을 만들어주는 스크립트.
#
# 문제 번호를 제공하면,
# - 해당 문제의 이름과 링크를 주석으로 포함하고
# - 문제 번호를 이름으로 가지는
# 파이썬 파일을 생성함.
#
# 사용법: ./boj.zsh [문제 번호] [닉네임]

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

if [ "$#" -eq 0 ]; then
  echo -n "백준 문제 번호: "
  read -r problem_number
  echo -n "닉네임: "
  read -r nickname
elif [ "$#" -eq 2 ]; then
  problem_number="$1"
  nickname="$2"
else
  exit 1
fi

# problem_number must be a number.
if [ -n $problem_number ] && [ $problem_number -eq $problem_number ] 2>/dev/null; then
	# OK. It is a number.
else
	echo "problem_number must be a number."
	exit 1
fi

# install jq if not installed
pkg_check=`which jq >/dev/null; echo $?`
if [ $pkg_check -eq 0 ]; then
  # jq is installed
else
  while true; do
    read -p "스크립트를 사용하기위해 jq를 설치해야합니다. 설치하시겠습니까? [y/n]: " yn
    case $yn in
        [Yy]* ) brew install jq; break;;
        [Nn]* ) exit 1;;
        * ) echo "Please answer yes or no.";;
    esac
  done
fi

# 
# =============================================================================
# 

api_result=$(curl --request GET \
  --url "https://solved.ac/api/v3/search/problem?query=${problem_number}&page=1&sort=id&direction=asc" \
  --header 'Content-Type: application/json' | jq ".items | .[0]")

problem_name=$(echo "$api_result" | jq ".titleKo")
problem_name=${problem_name#\"}
problem_name=${problem_name%\"}
problem_name="${problem_number}번: $problem_name"

# make directory if not exist.
solution_folder="$DIR/boj/$nickname"
mkdir -p "$solution_folder"

solution_file="$solution_folder/$problem_number.py"



# python version
python_version=$(python3 --version)

# today's date
today=$(date "+%Y/%m/%d")

echo "#" >> "$solution_file"
echo "#  $problem_name" >> "$solution_file"
echo "#  https://www.acmicpc.net/problem/$problem_number" >> "$solution_file"
echo "#  Version: $python_version" >> "$solution_file"
echo "#" >> "$solution_file"
echo "#  Created by $nickname on $today." >> "$solution_file"
echo "#" >> "$solution_file"
echo -e "\n\nfrom sys import stdin\n\nread = stdin.readline\n\nif __name__ == \"__main__\":\n    pass" >> "$solution_file"


echo "$problem_name"
echo "$solution_file"
