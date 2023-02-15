"""
    A self-dividing number is a number that is divisible by every digit it contains.

    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

    A self-dividing number is not allowed to contain the digit zero.

    Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
"""


def self_dividing_numbers(left: int, right: int):
    result = []
    for num in range(left, right + 1):
        if "0" in str(num):
            continue

        for i in str(num):
            if num % int(i) != 0:
                break
        else:
            result.append(num)
    return result
