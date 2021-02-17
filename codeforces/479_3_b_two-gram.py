n=int(input())
s=input()
l=[]

for i in range(n-1):
    l.append(s[i:i+2])

print(max(l, key=l.count))

