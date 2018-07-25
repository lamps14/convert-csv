#!/usr/bin/python3


file_to_write = open('converted_csv.txt', 'w+')
file_to_convert = open('test-csv.csv', 'r')
data = ''


with file_to_convert as myfile:
    data = myfile.read()

data = data.replace("\n", ",")
data1 = data[0:239].lower()
data2 = data[240:479].lower()
data3 = data[480:719].lower()
data4 = data[720:-1].lower()


print(len(data1))
print(len(data2))
print(len(data3))
print(len(data4))

formatted_string = data1 + '\n' + data2 + '\n' + data3 + '\n' + data4

file_to_write.write(formatted_string)
