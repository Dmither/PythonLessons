def write_table(lst):
    file = open("./data/index.txt", "w")
    for i in range(len(lst)):
        file.writelines([str(lst[i][0]), "\t", "|", "\t"])
        file.writelines([str(lst[i][1]), "\t", "|", "\t"])
        file.writelines([str(lst[i][2]), "\n"])
    file.close()


def read_table():
    lst = []
    file = open("./data/index.txt", "r")
    for i in file:
        item = i[:-1].split('\t|\t')
        lst.append(item)
    file.close()
    return lst


lst = [
    ["bread", 13.8, 12],
    ["chocolate", 28.5, 5],
    ["potato", 8, 5.5],
]


# ---------------------------------------------------------------

try:
    5 / 0
    print('success')
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Zerro division")
else:
    print("else")
finally:
    print("finally")