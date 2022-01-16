# solve fibonacci series using divide and conquer problem

def fibonacci(n):
    if n < 0:
        return 'Number canot be less than the 0'
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
