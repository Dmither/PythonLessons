file1 = open("./text.txt", "a")
file1.write("\nAdd some more text")
file1.close()

file1 = open("./text.txt", "r")
print(file1.read())
file1.close()
