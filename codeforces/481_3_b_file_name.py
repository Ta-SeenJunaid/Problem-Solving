n=int(input())
s=input()
c=int(0)

while "xxx" in s:
    c=+1
    n = s.find("xxx", 0, len(s) - 1)
    s = s[:n] + s[n + 1:]

print(c)