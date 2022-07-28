n = int(input())
points = [[int(x) for x in input().split()] for _ in range(n)]
k = int(input())

# 配列の最後尾を指定
xn, yn = points[-1]
answer = 0

# 配列から座標を読み出して最後尾との差を求める
for xi, yi in points:
    if abs(xi - xn) + abs(yi - yn) <= k:
        answer += 1

print(answer)