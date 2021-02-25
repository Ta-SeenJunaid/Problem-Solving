n= int(input())
a = input().split()[::-1]

print(len(set(a)))
print(*sorted(set(a), key=a.index, reverse=True))