number = 50
count = 0

try:
    with open("day1.txt", "r", encoding='utf-8') as d:
        for zeile in d:
            if zeile[0] == "L":
                try:
                    x = int(zeile[1:].strip())
                    number -= x
                except ValueError:
                    continue

            elif zeile[0] == "R":
                try:
                    x = int(zeile[1:].strip())
                    number += x
                except ValueError:
                    continue

            else:
                continue

            zahl = number % 100
            if number == 0:
                count += 1

except FileNotFoundError:
    print("File not Found")


print(count)
