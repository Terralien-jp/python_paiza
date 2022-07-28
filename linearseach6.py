n = int(input())
a = [int(x) for x in input().split()]
k = int(input())
# 入力される最大値が1,000,000,000とわかっているので
maximum = 1000000001
# k回繰り返すことでk番めに大きい数字がmaximumに代入される
for i in range(k):
    next_maximum = -1000000001
    for val in a:
        if val < maximum:
            next_maximum = max(next_maximum, val)
    maximum = next_maximum

print(maximum)