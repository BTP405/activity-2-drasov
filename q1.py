def getPrimeNumbers(n):
    return [x for x in range(2, n+1) if checkPrime(x)]


def checkPrime(numbers):
    if numbers < 2:
        return False
    for i in range(2, int(numbers**0.5) + 1):
        if numbers % i == 0:
            return False
    return True

n = 50
prime_numbers = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {prime_numbers}")
