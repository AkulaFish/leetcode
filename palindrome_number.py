def is_palindrome(self, x: int) -> bool:
    reverse = ""
    for i in reversed(str(x)):
        reverse += i
    return reverse == str(x)
