n = int(input())
a = [int(x) for x in input().split()]
# 入力される最大値が1,000,000,000とわかっているので
maximum = 1000000001
# 2回繰り返すことで2番めに大きい数字がmaximumに代入される
for i in range(2):
    next_maximum = -1000000001
    for val in a:
        if val < maximum:
            next_maximum = max(next_maximum, val)
    maximum = next_maximum

print(maximum)