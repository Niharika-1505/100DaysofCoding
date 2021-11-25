def add(*args):
    addition = 0
    print(args[0], type(args[1]))
    for n in args:
        addition += n
    return addition


def sub(*subtraction):  # the key word can be anything after *
    difference = 0
    print(subtraction[0], type(subtraction[1]))
    for n in subtraction:
        difference -= n
    return difference


print(f"1. Sum is {add(1, 2, 3)}")
print(f"2. Sum is {add(2, 2)}")
print(f"3. Sum is {add(3, 2, 3, 4, 5)}")
print(f"4. Sum is {add(4, 2, 3, 10, 100)}")
print(f"1. Diff is {sub(3, 2, 1)}")
print(f"2. Diff is {sub(2, 2)}")
print(f"3. Diff is {sub(3, 2, 3, 5, 4)}")
print(f"4. Diff is {sub(10, 100)}")
