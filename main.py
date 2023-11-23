import random
import datetime

current_time = datetime.datetime.now()
print_time = current_time.strftime("%Y년 %m월 %d일 - %H:%M")

n = random.randint(1, 30)
rand_nums = [random.randint(1, 100) for _ in range(n)]

print("현재 시각: ", print_time)
print()

print("정렬 전: ", rand_nums)

sorted_nums = sorted(rand_nums)

print("정렬 후: ", sorted_nums)