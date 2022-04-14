def fibonacci(n):

    try:
        n = int(n)
    except ValueError:
        return False

    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b

    for i in range(n - 2):
        a, b = b, a + b
    return b
