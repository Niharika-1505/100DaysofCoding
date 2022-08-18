import sys
import re

std = sys.stdin

line = std.readline().strip()
print(
    re.match("^[1-9][0-9]{5}$", line) is not None and [ord(line[i]) - ord(line[i + 2]) for i in range(4)].count(0) <= 1)
