def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        x = factorial_recursive(n - 1)
        print( n, "*", x, "=", n * x )
        return n * x

print(factorial_recursive(7))

