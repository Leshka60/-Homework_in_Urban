def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        if num > 1:
            for i in range(2, (num // 2) + 1):
                if (num % i) == 0:
                    print("Составное")
                    return num
            else:
                print("Простое")
                return num
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
