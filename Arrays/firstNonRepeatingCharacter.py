import unittest


def firstNotRepeatingCharacter(s):
    dups = []
    non_dups = []
    for i in s:
        if i in non_dups:
            non_dups.remove(i)
            dups.append(i)
        elif i in dups:
            pass
        else:
            non_dups.append(i)
    if not non_dups:
        return '_'
    else:
        return non_dups[0]


# Testing

test1 = "abacabad"
test2 = "abacabaabacaba"
test3 = "z"
test4 = "bcb"
test5 = "bcccccccb"
test6 = "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"
test7 = "zzz"
test8 = "bcccccccccccccyb"
test9 = "xdnxxlvupzuwgigeqjggosgljuhliybkjpibyatofcjbfxwtalc"
test10 = "ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof"

class MyTest(unittest.TestCase):
    def test_firstNonRepeatingChar(self):
        self.assertEqual(firstNotRepeatingCharacter(test1), "c")
        self.assertEqual(firstNotRepeatingCharacter(test2), "_")
        self.assertEqual(firstNotRepeatingCharacter(test3), "z")
        self.assertEqual(firstNotRepeatingCharacter(test4), "c")
        self.assertEqual(firstNotRepeatingCharacter(test5), "_")
        self.assertEqual(firstNotRepeatingCharacter(test6), "d")
        self.assertEqual(firstNotRepeatingCharacter(test7), "_")
        self.assertEqual(firstNotRepeatingCharacter(test8), "y")
        self.assertEqual(firstNotRepeatingCharacter(test9), "d")
        self.assertEqual(firstNotRepeatingCharacter(test10), "g")


unittest.main()
