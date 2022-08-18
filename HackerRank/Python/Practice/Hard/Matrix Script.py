import sys
import re

std = sys.stdin

n, m = map(int, std.readline().split())
s = [" "] * (n * m)
for i in range(n):
    line = std.readline().rstrip()
    for j in range(len(line)):
        s[j * n + i] = line[j]
s = "".join(s)

print(re.sub("(?<=\w)\W+(?=\w)", " ", s))
