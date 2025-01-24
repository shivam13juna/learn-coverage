def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    x = 10
    y = 5

    print(f"Addition of {x} and {y} is: {add(x, y)}")
    print(f"Subtraction of {x} and {y} is: {sub(x, y)}")
    print(f"Multiplication of {x} and {y} is: {mul(x, y)}")
    print(f"Division of {x} and {y} is: {div(x, y)}")