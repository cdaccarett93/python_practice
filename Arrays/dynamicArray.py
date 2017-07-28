import ctypes
import sys


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item <= self.n:
            return IndexError('Item is out of bounds!')
        else:
            return self.A[item]

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # double if capacity isn't enough

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_cap):
        b = self.make_array(new_cap)

        for item in range(self.n):
            b[item] = self.A[item]

        self.A = b
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def listinbytes(self, t):
        data = []
        for x in range(t):
            # number of elements
            ad = len(data)

            # Actual size in bytes
            bd = sys.getsizeof(data)

            print('Length: {0:3d}; Size in bytes: {1:4d} '.format(ad, bd))

            # Increase Length by one
            data.append(t)


arr = DynamicArray()

for i in range(500):
    arr.append(i)

arr_len = len(arr)

arr.listinbytes(arr_len)
