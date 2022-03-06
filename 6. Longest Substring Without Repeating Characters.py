from typing import Set


def lengthOfLongestSubstring(s: str) -> int:
    characterSet = set()    # type: Set[str]
    l_pointer, r_pointer, result = 0, 0, 0

    while r_pointer < len(s):
        if not s[r_pointer] in characterSet:
            characterSet.add(s[r_pointer])
            r_pointer += 1
            result = max(r_pointer - l_pointer, result)
        else:
            characterSet.remove(s[l_pointer])
            l_pointer += 1

    return result
