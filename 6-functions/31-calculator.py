def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exp(a, b):
    total = 1
    for _ in range(0,b):
        total *= a
    return total

print(add(3, 4))
print(subtract(10, 5))
print(multiply(7, 6))
print(divide(1, 2))
print(exp(2, 3))