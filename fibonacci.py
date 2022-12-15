def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

N = int(input('give the N value: ' ))
print(fib(N))

