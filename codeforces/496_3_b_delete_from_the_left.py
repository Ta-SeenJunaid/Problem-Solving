s = input()
t = input()
s = s[::-1]
t= t[::-1]
count = 0
# min = min(len(s), len(t))

for i in range(min(len(s), len(t))):
    if s[i]==t[i]:
        count +=1
    else:
        break
print(len(s) + len(t)- 2*count)