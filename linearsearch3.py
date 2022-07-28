n = int(input())
results = [input().split() for _ in range(n)]
k = int(input())

resultsの中身それぞれをnameとscoreに代入しスコアを合格点（k）と比較
for name, score in results:
    if int(score) >= k:
        print(name)