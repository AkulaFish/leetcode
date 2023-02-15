"""
    The array-form of an integer num is an array representing its digits in left to right order.
    For example, for num = 1321, the array form is [1,3,2,1].
    Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
"""


def add_to_array_form(num: list[int], k: int):
    """Best possible solution"""
    str_num = "".join(str(n) for n in num)
    result = int(str_num) + k
    return [int(d) for d in str(result)]
