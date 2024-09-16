numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_primes = []
for number in numbers:
    if number == 1:
        continue
    for i in range ( 2, number // 2 +1 ):
        if number % i == 0:
            not_primes.append(number)
            break
    else:
        prime. append(number)
print(f"{'Primes:'}", prime)
print(f"{'Not Primes:'}",  not_primes)

