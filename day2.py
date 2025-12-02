
def part1():

    ranges = []
    invalids = 0
    try:
        with open("day2.txt", "r", encoding='utf-8') as d:
            ranges = d.read().split(',')

    except FileNotFoundError:
        print("File Not Found")

    for r in ranges:
        x, y = r.split("-")
        x = int(x)
        y = int(y)
        for number in range(x, y+1):
            n = str(number)
            l = len(n)
            if l % 2 == 0:
                h = l // 2
                f = n[0:h]
                b = n [h:]
                if f == b:
                    invalids += number

    print(invalids)

part1()

def part2():

    ranges = []
    invalids = 0
    try:
        with open("day2.txt", "r", encoding='utf-8') as d:
            ranges = d.read().split(',')

    except FileNotFoundError:
        print("File Not Found")

    for r in ranges:
        x, y = r.split("-")
        x = int(x)
        y = int(y)
        for number in range(x, y+1):
            n = str(number)
            l = len(n)
            for muster_laenge in range(1, l):
                if l % muster_laenge == 0:
                    h = l // muster_laenge
                    f = n[0:muster_laenge]
                    if f * h == n:
                        invalids += number
                        break

    print(invalids)

part2()
