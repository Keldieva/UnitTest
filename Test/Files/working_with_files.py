income_file4 = open("income of DouglasCounty families.csv", "a")
income_file4.write("\n Zarrina, Zarrina, 0000")

income_file4.close()

income_file4 = open("income of DouglasCounty families.csv", "r")
print(income_file4())

# import os
#
# file5 = open('text5.txt', 'w')
#
# file5.write('\n Hello everyone, it"s my first try')
#
# file5.close()
#
# file5 = open('text5.txt', 'r')
#
# print(file5.read())
#
# file5.close()
#
# os.remove('text5.txt')