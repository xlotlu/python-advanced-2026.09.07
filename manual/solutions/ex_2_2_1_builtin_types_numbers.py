# Write a function is_prime that checks whether a given number is prime.


def is_prime(nr):
    if nr <= 1:
        return False
    if nr == 2 or nr == 3:
        return True
    if nr % 2 == 0:
        return False
    for i in range(3, int(nr ** 0.5) + 1, 2):
        if nr % i == 0:
            return False
    return True


print(is_prime(100))
print(is_prime(17))
print(is_prime(57))
print(is_prime(97))
print(is_prime(8))
