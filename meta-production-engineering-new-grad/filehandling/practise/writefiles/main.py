
# f = open('test.txt', 'r')

# print(f.read())

# f.close()

# with will wrap a block of code with context manager 
# so i dont have to close it .



# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line, end='')



import json
import csv

csvemp = [["Name", "Age", "job"],
          ["ram", "30", "cook"],
          ["pat","22","sand"]]

jsonemp = {
    "name": "ram",
    "age": "20",
    "prof": "cook"
}

text = 'this is a must'
employees = ["rav", "mar", "neel"]


filepath="employees.csv"

try:     
    with open(filepath, 'w') as f:
        writer= csv.writer(f)
        for row in csvemp:
            writer.writerow(row)
        print(f"json file '{filepath}' was created")
except FileExistsError:
    print("that file already exists")
        
    





