from exercise_python_koni.chapter_5.c5_4_sources import c5_4_daily,c5_4_weekly

print("Daily forecast:", c5_4_daily.forecast())
print("Weekly forecast:", c5_4_weekly.forecast())
for number, outlook in enumerate(c5_4_weekly.forecast(),1):
    print(number, outlook)