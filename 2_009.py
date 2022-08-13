N, S = map(int, input().split())
A = list(map(int, input().split()))

answer = "No"
for i in range(0, 1 << N):
    print(i)
    partsum = 0
    for j in range(0, N):
        if (i & (1 << j)) != 0:
            partsum += A[j]
    if partsum == S:
        answer = "Yes"
        break

# 出力
print(answer)

