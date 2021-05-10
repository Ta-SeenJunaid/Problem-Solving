a, b, x = map(int, input().split())

p = '01'
c = int(x/2)

if x%2 == 0:
    if a > b:
        print(p*c + p[1] * (b - c) + p[0] * (a - c))
    else:
        p = '10'
        print(p*c + p[1] * (a - c) + p[0] * (b - c))
else:
    if a > b:
        print(p*c + p[0] * (a - c) + p[1] * (b - c))
    else:
        p = '10'
        print(p*c + p[0] * (b - c) + p[1] * (a - c))