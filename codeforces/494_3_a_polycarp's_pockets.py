import collections
n = int(input())
l = list(map(int, input().split()))
print(max(collections.Counter(l).values()))