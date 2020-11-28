def prime_factors(N):
   # while True:
    try:
        for x in range(1, N+1):
            if (N % x == 0):
                yield x
    except StopIteration:
        return ?
