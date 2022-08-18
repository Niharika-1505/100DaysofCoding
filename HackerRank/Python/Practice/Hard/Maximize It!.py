data = input().split()
k = int(data[0])
m = int(data[1])
val = [0]
for i in range(0,k):
    newval=[]
    data=input().split()
    for j in data[1:]:
        d = int(j)
        for k in val:
            newtot = (d*d + k) % m
            if not(newtot in newval):
                newval.append(newtot)
    val = newval
print(max(val))