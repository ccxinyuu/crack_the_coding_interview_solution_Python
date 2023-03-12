# O(N)
import string
import unittest
from collections import Counter


def palindromePermutation(s):
    checkPalindromeMap = [0 for _ in range(ord("z") - ord("a") +1)]
    count_odd = 0
    
    for c in s:
        new_c = changeCharacter(c)
        if new_c != -1:
            checkPalindromeMap[new_c] += 1
    
    for i in checkPalindromeMap:
        if i %2 == 1:
            count_odd += 1
    
    return count_odd <= 1
    
def changeCharacter(c):
    a = ord("a")
    z = ord("z")
    upper_a = ord("A")
    upper_z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a

    if upper_a <= val <= upper_z:
        return val - upper_a
    return -1

class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        palindromePermutation,
    ]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()