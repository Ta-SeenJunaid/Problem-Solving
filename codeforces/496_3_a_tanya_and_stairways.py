n = int(input())
l = list(map(int, input().split()))

print(l.count(1))

length_l = len(l)
if length_l == 1:
    print("1")
else:
    for i in range(length_l):
        if i == (length_l-1):
            print(l[i])
            break
        if (l[i] + 1) != l[i+1]:
            print(l[i])


