def fib(n):
    fib1 = fib2 = 3

    for i in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


fibonacci_iterator = fib(300)

for num in fibonacci_iterator:
    print(num)