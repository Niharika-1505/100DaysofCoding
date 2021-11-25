class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


def calculate(**kwargs):
    print(kwargs, type(kwargs))
    print(f"Adding these values {kwargs['add']}")
    add = 0
    diff = 0
    mult = 1
    for (key, value) in kwargs.items():
        if key == "add":
            for values in value:
                add += values
            print(f"Sum is {add}")
        elif key == "subtract":
            for values in value:
                diff -= values
            print(f"Difference is {diff}")
        elif key == "divide":
            print(f"Division value is {value[0] / value[1]}")
        elif key == "multiply":
            for values in value:
                mult *= values
            print(f"Product is {mult}")


def example(n, **any_keyword):
    n += any_keyword["add"]
    n *= any_keyword["multiply"]
    print(f"n value is {n}")


calculate(add=(3, 2), subtract=(4, 2))
calculate(add=(3, 2), multiply=(4, 2), divide=(4, 2))
example(2, add=3, multiply=5)
my_car = Car(model="Chevrolet", color="Red", seats="5")
print(f"Car model is {my_car.model}")
