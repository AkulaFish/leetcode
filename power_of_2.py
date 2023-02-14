def is_power_of_two(n):
    return n & n - 1 == 0

print(is_power_of_two(255))
