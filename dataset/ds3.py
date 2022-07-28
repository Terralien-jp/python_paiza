li = [int(x) for x in input().split()]

# ソートで並べ替え
li.sort()
# 配列にはいっている数値は3つなのでこのようにすると最大値、最小値の差が求められる
# 解き方として納得いかないのでmax/minを使用して解答した
print(li[2] - li[0])