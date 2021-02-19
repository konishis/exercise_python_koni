# from exercise_python_koni.chapter_5.c5_3_1_report import get_description
# description = get_description()
# print("Today's weather:",description)

# 別名にしてインポート
from exercise_python_koni.chapter_5.c5_3_1_report import get_description as hoge

description = hoge()
print("Today's weather:", description)
