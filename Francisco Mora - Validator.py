import csv

def valid_card_number(num: str):
    if len(num) != 16:
        return False
    last_digit = int(num[15])
    other_nums = num[0:15]
    print(other_nums)


print(valid_card_number("4556737586899855"))

# with open("Book1.csv") as old_csv:
#         with open("MyNewFile.csv", 'w', newline='') as new_csv:
#             reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#
#         for row in reader:
#             # old_number = int(row[0]) + 1
#             old_number = row[0]
#             if valid_card_number(old_number):
#                 writer.writerow(row)
