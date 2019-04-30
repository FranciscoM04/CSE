import csv

def validate(num: str):
    if not all_16_digits(num):
        return False
    if divisible_by_2(num) and divisible_by _3(num):
        return True
    return False

def divisible_by _3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False

def divisible_by _2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def all_16_digits(num: str):
    if not all_16_digits(num):


# with open("Book1.csv") as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#     reader = csv.reader(old_csv)
#     writer = csv.writer(new_csv)
#     print("Processing...")
#
#     for row in reader:
#         # old_number = int(row[0]) + 1
#         old_number = row[0]
#         first_num = int(old_number)
#         if first_num % 2 == 0:
#              writer.writerow(row)
# print("Done")

def reverse(string):
    print(string[::-1])

reverse_it("Hello World")

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

with open("Book1.csv") as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
    writer = csv.writer(new_csv)
    print("Processing...")

    for row in reader:
        # old_number = int(row[0]) + 1
        old_number = row[0]
        if validate(old_number):
            writer.writerow(row)
print("Done")

def valid_card_number(num: str):

print(valid_card_number("9988951394582520"))

list_num = list(number)
for index in ranmge(len(number)):
    list_num[index] = int(list_num[index])
