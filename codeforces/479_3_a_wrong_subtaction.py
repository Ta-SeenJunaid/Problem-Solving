n,k = map(int,input().split())

for _ in range(k):
    if n%10:
        temp=n-1
        if temp<=0:
            break
        else:
            n=temp
    else:
        n=n//10

print(n)