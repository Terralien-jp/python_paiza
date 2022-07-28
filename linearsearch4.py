n = int(input())
results = [input().split() for _ in range(n)]
# 最低点をk最高点をlとする
k, l = [int(x) for x in input().split()]

for name, score in results:
    # k以上l以下の名前を合格者としてプリント
    if k <= int(score) <= l:
        print(name)