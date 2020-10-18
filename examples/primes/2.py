from random import randint

def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generate_big_prime(a, b):
    found_prime = False
    while not found_prime:
        p = randint(2**a, 2**b)
        if is_prime(p, 1000):
            return p