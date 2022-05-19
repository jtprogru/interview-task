"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321

Example 3:
    Input: x = 120
    Output: 21

Constraints:
- -2^31 <= x <= 2^31 - 1
"""


def solution(x: int) -> int:
    x = str(x)
    if x[0] == "-":
        a = int("-" + x[-1:0:-1])
        if -2147483648 <= a <= 2147483647:
            return a
        else:
            return 0
    else:
        a = int(x[::-1])
        if -2147483648 <= a <= 2147483647:
            return a
        else:
            return 0
