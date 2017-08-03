def isCryptSolution(crypt, solution):
    cryptNum = []
    for el in crypt:
        word = ""
        for i in el:
            for x in solution:
                if i in x:
                    word += solution[solution.index(x)][1]
        cryptNum.append(word)
    a = cryptNum[0]
    b = cryptNum[1]
    c = cryptNum[2]
    lengtha = len(a)
    lengthb = len(b)
    if a[0] == '0' and b[0] == '0' and lengtha > 1 and lengthb > 1 or lengtha > 1 and a[0] == '0' or lengthb > 1 and b[0] == '0' or int(a) + int(b) != int(c):
        return False
    else:
        return


crypt = ["SEND", "MORE", "MONEY"]

solution = [["O", "0"],
            ["M", "1"],
            ["Y", "2"],
            ["E", "5"],
            ["N", "6"],
            ["D", "7"],
            ["R", "8"],
            ["S", "9"]]

crypt2 = ["TEN", "TWO", "ONE"]

solution2 = [["O", "1"],
             ["T", "0"],
             ["W", "9"],
             ["E", "5"],
             ["N", "4"]]

crypt3 = ["AA", "BB", "AA"]
solution3 = [["A", "1"],
             ["B", "0"]]

isCryptSolution(crypt3, solution3)
