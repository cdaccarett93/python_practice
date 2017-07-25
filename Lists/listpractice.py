import sys


def listinbytes(n):
    data = []
    for i in range(n):
        # number of elements
        a = len(data)

        # Actual size in bytes
        b = sys.getsizeof(data)

        print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a, b))

        # Increase Length by one
        data.append(n)

listinbytes(50)

# The length at the beginning is 0 and size in bytes is 64 and then 96 bytes for
# 1 to 4. There is a pattern, Python increases the size in bytes in chunks this is to not have
# to constantly be take memory for every element being appended. It grabs enough memory for future
# elements and does this again once it detects that it will probably need more memory for more future elements.




