n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
b = [int(x) for x in input().split()]
for i in range(q):
    print(a[b[i]-1])