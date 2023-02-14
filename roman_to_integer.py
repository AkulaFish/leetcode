def roman_to_int(s: str):
    """My solution"""
    nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = nums.get(s[-1])
    for i in range(2, len(s) + 1):
        if nums.get(s[-i]) < nums.get(s[-i + 1]) and nums.get(s[-i]) != nums.get(s[-i + 1]):
            result -= nums.get(s[-i])
        else:
            result += nums.get(s[-i])
    return result


def roman_to_int_runtime(self, s: str) -> int:
    """Best runtime solution"""
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    for ind, num in enumerate(s[:-1], 1):
        res += romans[num]
        if romans[num] < romans[s[ind]]:
            res -= romans[num] * 2
    return res + romans[s[-1]]
