if 10 < 5:
    print('10 is less than 5')
elif 5 < 10:
    print('5 is less than 10')
else:
    print('test')

# for loops
# range(start,stop,step) start is inclusive, step is the amount of increment to take
# below is equivalent to for(int i = 0; i < 10; i++)
for i in range(1, 10):
    print(i)

# LIST (c++ equivalent to arrays)
# .append() add item to end list
# .pop() remove last item from list
# len(name_of_list) return the length of the list
# .sort()

list_var = ['start learning python', 'get comfortable with python lists']

for i in range(0, len(list_var)):
    print(list_var[i])

# OR
# for item in list_var:
#     print(item)


# DICTIONARY
a_dict = {
    "abc": "A string",
    "another": "Another string",
    "yetanother": "Another one",
}
print(a_dict)


# TUPLE
tup = ("abc", "def")
print(tup)


# FUNCTIONS
items = ["Mic", "Phone", 323.12, 3212.123, "Test", "Bag", "Cliff Bars", 1245]


def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items


print(parse_lists(items))


# CLASSES

class Animal:
    noise = "Grunt"
    size = "Large"
    color = "brown"
    hair = "Covers body"

    def get_color(self):
        return self.color

    def make_noise(self):
        return self.noise


# Dog in inheriting from Animal class
class Dog(Animal):
    name = 'Jon'


jon = Dog()
jon.color = 'white'
jon.name = 'jon snow'
jon.noise = 'WOOF'
print(jon.get_color())
print(jon.make_noise())


list_num = []
for i in range(10):
    list_num.append(i)

list_num_length = len(list_num)
print("list_num length", list_num_length)
print("list num val", list_num[len(list_num)-1])


matrix = [[]]
matrix = [[0 for i in range(2)] for i in range(2)]

print("matrix: ", matrix)