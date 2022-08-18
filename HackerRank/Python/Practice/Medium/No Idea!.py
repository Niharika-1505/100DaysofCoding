n, m = list(map(int, input().split()))
n_array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
res = 0
for x in n_array:
    if x in A:
        res += 1
    elif x in B:
        res -= 1
print(res)