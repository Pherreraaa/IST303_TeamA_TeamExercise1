def determine_primes(n: int):
    if not isinstance(n, int):
        raise Exception("Input must be an integer.")
    if n < 2:
        return ([], 0)

    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    iterations = 0

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * 2, n + 1, p):
                is_prime[multiple] = False
            iterations += 1

    return (primes, iterations)
