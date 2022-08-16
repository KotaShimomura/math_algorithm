n = int(int(input()))
s = []
sn = int(n**0.5)

for i in range(2, sn+1):
    while True:
        if n % i == 0:
            s.append(i)
            n //= i
        else:
            break

if n != 1:
    s.append(n)

print(*s)