from datetime import date

todoList = []
doneList = []


def markitemcomplete():
    ditem = int(input("Type item key to mark as complete: "))
    doneList.append(todoList[ditem])
    todoList.pop(ditem)


def print_todo_list():
    num = 0
    for dates, item in todoList:
        print("key: " + str(num), "Finish by: " + dates, "Item Description: " + item)
        num += 1


def print_done_list():
    for dates, item in doneList:
        print("Item Description: " + item)


def additem():
    itemname = input("Todo item: ")
    month, day, year = input("Due Date, format date Month/Day/Year ").split('/')
    whatday = date(int(year), int(month), int(day)).strftime('%A')
    date_string = month + '/' + day + '/' + year
    a = date_string + ' ' + whatday
    tup = (a, itemname)
    todoList.append(tup)


def removeitem():
    ritem = input("Type item key to remove: ")
    todoList.pop(int(ritem))


def print_instructions():
    print("Press 1 to add an item, 2 to remove an item")
    print("3 to mark item as complete, 4 to print todo list")
    print("5 to print done list, Type exit to exit")
    var1 = input("Please enter item: ")
    print("\n")
    if var1 == '1':
        additem()
        print("\n")
        print_instructions()
    elif var1 == '2':
        removeitem()
        print("\n")
        print_instructions()
    elif var1 == '3':
        markitemcomplete()
        print("\n")
        print_instructions()
    elif var1 == '4':
        print_todo_list()
        print("\n")
        print_instructions()
    elif var1 == '5':
        print_done_list()
        print("\n")
        print_instructions()
    elif var1 == 'exit':
        pass
    else:
        print_instructions()


print_instructions()
