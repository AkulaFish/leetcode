"""
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
"""


def longest_common_prefix(strs: list[str]) -> str:
    max_word = max(strs)
    for i in range(len(max_word) + 1):
        if_starts = [w.startswith(max_word[:i]) for w in strs]
        if not all(if_starts):
            return max_word[:i-1]

    return max_word
