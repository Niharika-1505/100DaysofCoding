# Write your code below this row 👇
add = 0
for n in range(0, 100, 2):
    add += n
print("Sum of numbers divisible by 2 is:", add)
add1 = 0
for n in range(1, 100):
    if n % 3 == 0:
        add1 += n
print("Sum of numbers divisible by 3 is:", add1)
