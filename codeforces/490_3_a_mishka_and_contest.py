n, k = map(int, input().split())
l = list(map(int, input().split()))

c = 0
c1 = 0

for i in range(len(l)):
    if l[i] <= k:
        c += 1
    else:
        break

for i in range(c):
    l.pop(0)

l.reverse()
for i in range(len(l)):
    if l[i] <= k:
        c1 += 1
    else:
        break

print(c+c1)