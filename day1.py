
def part1():
    number = 50
    count1 = 0
    # part 1
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

                number = number % 100
                if number == 0:
                    count1 += 1

    except FileNotFoundError:
        print("File not Found")


    print(count1)

part1()


def part2():
    # part 2

    number = 50
    count = 0

    try:
        with open("day1.txt", "r", encoding='utf-8') as d:
            for zeile in d:
                if zeile[0] == "L":
                    try:
                        x = int(zeile[1:].strip())
                        for i in range(x):
                            number -= 1
                            number = number % 100
                            if number == 0:
                                count += 1
                            
                    except ValueError:
                        continue

                elif zeile[0] == "R":
                    try:
                        x = int(zeile[1:].strip())
                        for i in range(x):
                            number += 1
                            number = number % 100
                            if number == 0:
                                count += 1
                    except ValueError:
                        continue

                else:
                    continue


    except FileNotFoundError:
        print("File not Found")


    print(count)

part2()



