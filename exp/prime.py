n = int(int(input()))
s =[]
sn = int(n**0.5)

for i in range(1,sn+1):
    if n % i == 0:
        s.append(i)
        if n // i != i:
            s.append(n // i)

s.sort()
for i in s:
    print(i)