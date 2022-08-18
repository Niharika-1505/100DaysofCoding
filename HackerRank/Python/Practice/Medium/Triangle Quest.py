for i in range(1, int(input())):
    print(i * int(bin((2 ** i) - 1)[2:]))
