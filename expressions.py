def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

def and_func(x, y):
    return x and y

def or_func(x, y):
    return x or y

def not_func(x):
    return not x

def main():

    # Defining the variables because otherwise the functions don't work
    a = 1
    b = 2
    c = 3
    e = 0
    d = 5
    f = 3.2
    g = 10

    # Expression number 1
    expected = a + b * c - e / d + f or g
    actual = or_func(add(add(a, (subtract(multiply(b, c), divide(e, d)))), f), g)
    print(expected, actual)

    # Expression number 2
    expected = a * b * d + c and f and g
    actual = and_func(and_func(add(multiply(multiply(a,b), d), c), f), g)
    print(expected, actual)

    # Expression number 3
    expected = a and b or c and (e + d + f + g)
    actual = or_func(and_func(a, b), and_func(c, add(add(add(e, d), f), g)))
    print(expected, actual)

main()