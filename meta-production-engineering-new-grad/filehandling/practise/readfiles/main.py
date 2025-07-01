
import json 

file_path = "input.txt"

try:
    with open(file_path,"r") as file:
        content= file.read()
        print(content)
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you dont have persmission to read that file")



# For JSON
import json
with open("file.json") as f:
    data = json.load(f)

# For CSV
import csv
with open("file.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["likes"])

# Reading large log files
with open("access.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            print(line)
