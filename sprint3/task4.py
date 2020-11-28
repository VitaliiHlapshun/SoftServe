def prime_factors(N):
    for x in range(1, N+1):
        if N % x == 0:
            yield x
    while True:
        yield None
