n = int(input())
points = [[int(x) for x in input().split()] for _ in range(n)]
# 長方形の座標
xs, xt = [int(x) for x in input().split()]
ys, yt = [int(x) for x in input().split()]

answer = 0

for xi, yi in points:
    # 長方形の水平方向座標に含まれならhorizontalに代入
    horizontal = xs <= xi <= xt
    # 長方形の垂直方向座標に含まれるならverticalに代入
    vertical = ys <= yi <= yt
    # 2つの条件をみたす場合のみanswerをインクリメントする
    if horizontal and vertical:
        answer += 1

print(answer)