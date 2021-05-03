n = int(input())
t = input()
for i in range(1, n+1):
    if n % i == 0:
        t = t[:i][::-1]+t[i:]

print(t)