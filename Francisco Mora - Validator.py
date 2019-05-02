def valid_card_number(num: str):

print(valid_card_number("9988951394582520"))

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