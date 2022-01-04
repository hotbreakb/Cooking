#!/bin/zsh

# 오늘의 메뉴를 만들어주는 스크립트.
#
# 사용법: ./today-menu.zsh [년] [월] [일]

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

if [ "$#" -eq 0 ]; then
  today=$(date "+%Y-%m-%d")
else
  today="$1-$2-$3"
fi
# today's date


# folder
today_folder="$DIR/$today"
dish_folder="$DIR/$today/dish"
recipe_folder="$DIR/$today/recipe"


# file
today_readme_file="$today_folder/README.md"
dish_readme_file="$dish_folder/README.md"
recipe_readme_file="$recipe_folder/README.md"


# mkdir folder
mkdir "$today_folder"
mkdir "$dish_folder"
mkdir "$recipe_folder"


# today README
echo "![header](https://capsule-render.vercel.app/api?type=waving&color=timeAuto&height=300&section=header&text=🥗오늘의%20메뉴🥘&fontSize=70&animation=fadeIn&fontAlignY=38&desc=미%20정&descAlignY=58&descAlign=50&descSize=30)" >> "$today_readme_file"
echo "\n### 📑 메뉴 상세페이지\n" >> "$today_readme_file"
echo "### [🍱 요리](./dish)\n" >> "$today_readme_file"
echo "### [📖 레시피](./recipe)" >> "$today_readme_file"

# dish README
echo "![header](https://capsule-render.vercel.app/api?type=waving&color=timeAuto&height=300&section=header&text=🍱%20요리&fontSize=70&animation=fadeIn&fontAlignY=38)\n" >> "$dish_readme_file"
echo "## 미정\n" >> "$dish_readme_file"
echo "|   Cook    |             Dishes             |" >> "$dish_readme_file"
echo "| :-------: | :----------------------------: |" >> "$dish_readme_file"
echo "| WhiteHyun | [✍️작성중✍️](./dish1_white.py) |" >> "$dish_readme_file"
echo "| hotbreakb |  [✍️작성중✍️](./dish1_hot.py)  |" >> "$dish_readme_file"

# recipe README
echo "![header](https://capsule-render.vercel.app/api?type=waving&color=timeAuto&height=300&section=header&text=📖%20레시피&fontSize=70&animation=fadeIn&fontAlignY=38)\n" >> "$recipe_readme_file"
echo "## 미정\n" >> "$recipe_readme_file"
echo "|   Cook    |             Recipe             |" >> "$recipe_readme_file"
echo "| :-------: | :----------------------------: |" >> "$recipe_readme_file"
echo "| WhiteHyun | [✍️작성중✍️](./dish1_white.md) |" >> "$recipe_readme_file"
echo "| hotbreakb |  [✍️작성중✍️](./dish1_hot.md)  |" >> "$recipe_readme_file"