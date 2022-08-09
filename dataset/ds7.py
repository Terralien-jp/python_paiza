H, W, r, c = map(int, input().split())
maze = [input() for _ in range(H)]

# リストのインデックスははからなのでr, cから１を引き、壁（#）であった場合Yes、そうでない場合Noを返す
if maze[r-1][c-1] == "#":
    print("Yes")
else:
    print("No")