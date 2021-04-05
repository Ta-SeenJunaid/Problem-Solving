n = int(input())
count = 0

string_list = []

for i in range(n):
    string_list.append(input())

string_list = sorted(string_list, key=len)
for i in range(len(string_list)-1):
    if string_list[i] in string_list[i+1]:
        count +=1
if count+1 == n:
    print('YES')
    for i in range(len(string_list)):
        print(string_list[i])
else:
    print('NO')
