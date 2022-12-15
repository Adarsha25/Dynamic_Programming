def fib_memeorization(n, cache={}):
    if n < 2:
        return n

    if n in cache:
        return cache[n]

    else:
        cache[n] = fib_memeorization(n-1, cache) + fib_memeorization(n-2, cache)
        return cache[n]


N = int(input('give the N value: ' ))
print(fib_memeorization(N))