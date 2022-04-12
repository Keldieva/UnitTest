import os

#file1 = open("2.txt", "a")
#file1.write("\n my fourth line")
#file1.close()
file1 = open("2.txt", "r")

print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())

os.remove("2.txt")
