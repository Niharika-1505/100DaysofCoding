def prime_checker(number):
    flag = 0
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
                flag = 1
                break
        if flag == 0:
            return True


n = int(input("Check this number: "))
if prime_checker(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
