"""
Implement strStr().
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters.
"""


def solution(haystack: str, needle: str) -> int:
    i = 0
    j = 0
    m = len(needle)
    n = len(haystack)
    if m == 0:
        return 0
    while i < n and n - i + 1 >= m:
        if haystack[i] == needle[j]:
            temp = i
            while j < m and i < n and needle[j] == haystack[i]:
                i += 1
                j += 1
            if j == m:
                return temp
            i = temp + 1
            j = 0
        else:
            i += 1
    return -1
