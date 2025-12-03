
def part1():
    # part 1
    ergebnis = 0

    try:
        with open("day3.txt", "r", encoding='utf-8') as d:
            for zeile in d:
                zeile = zeile.strip()
                zehner = max(zeile[:-1])
                index = zeile.index(zehner)
                einer = max(zeile[index+1:])
                z = zehner + einer
                zahl = int(z)
                ergebnis += zahl

    
    except FileNotFoundError:
        print("File not Found")

    print(ergebnis)

part1()

def part2():
    ergebnis = 0

    try:
        with open("day3.txt", "r", encoding='utf-8') as d:
            for zeile in d:
                n = ""
                zeile = zeile.strip()
                for i in range(12):
                    laenge = len(zeile)
                    suchbereich = laenge - (11 - i)
                    ziffer = max(zeile[0:suchbereich])
                    index = zeile.index(ziffer)
                    n += ziffer
                    zeile = zeile[index+1:]
                
                zahl = int(n)
                ergebnis += zahl

    except FileNotFoundError:
        print("File not Found")

    print(ergebnis)

part2()
    