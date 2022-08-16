n = int(input())

s = 'Yes'
sn = int(n**0.5)

for i in range(2,sn):
    if n % i == 0:
        s = 'No'
        break


print(s)