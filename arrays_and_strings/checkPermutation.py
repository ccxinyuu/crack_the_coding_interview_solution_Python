import time
import unittest
from collections import defaultdict

def checkPermutation(s1, s2):
    checkMap = {}
    if len(s1) != len(s2):
        return False
    
    for c in s1:
        if c in checkMap:
            checkMap[c] += 1
        else:
            checkMap[c] = 1
    
    for c in s2:
        if c in checkMap:
            checkMap[c] -= 1
        else:
            return False
    
    for value in checkMap.values():
        if value != 0:
            return False 
    return True




class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        checkPermutation,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
