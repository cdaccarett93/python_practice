import unittest


def firstDuplicate(a):
    if len(a) == 1:
        return -1
    data = dict()
    for index, val in enumerate(a):
        dup = data.get(val, None)
        if dup is not None:
            return val
        else:
            data[val] = index
    return -1


# Testing Function

test1 = [2, 3, 3, 1, 5, 2]
test2 = [2, 4, 3, 5, 1]
test3 = [1]
test4 = [2, 2]
test5 = [2, 1]
test6 = [2, 1, 3]
test7 = [2, 3, 3]
test8 = [3, 3, 3]
test9 = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
test10 = [10, 6, 8, 4, 9, 1, 7, 2, 5, 3]
test11 = [1, 1, 2, 2, 1]


class MyTest(unittest.TestCase):
    def test_firstDuplicate(self):
        self.assertEqual(firstDuplicate(test1), 3)
        self.assertEqual(firstDuplicate(test2), -1)
        self.assertEqual(firstDuplicate(test3), -1)
        self.assertEqual(firstDuplicate(test4), 2)
        self.assertEqual(firstDuplicate(test5), -1)
        self.assertEqual(firstDuplicate(test6), -1)
        self.assertEqual(firstDuplicate(test7), 3)
        self.assertEqual(firstDuplicate(test8), 3)
        self.assertEqual(firstDuplicate(test9), 6)
        self.assertEqual(firstDuplicate(test10), -1)
        self.assertEqual(firstDuplicate(test11), 1)


unittest.main()
