import random
import time
times = time.perf_counter()
unlock_level = True
beat_level = True
end_time = 100
target_score = 10000
score = 800000
times2 = time.perf_counter()
times = times2 - times
if score < target_score or not beat_level or times > end_time/10 or not unlock_level:
    print("You still have some goals to make")
else:
    print("Goals met")

if score > target_score*10 and times < end_time/10:
    print("wha", times, score)

