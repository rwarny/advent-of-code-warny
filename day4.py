def part1():
    # part 1
    ergebnis = 0

    try:
        with open("day4.txt", "r", encoding='utf-8') as d:
            zeilen = d.read().strip().split('\n')
            for y in range(len(zeilen)):
                for x in range(len(zeilen[y])):
                    if zeilen[y][x] == '@':
                        nachbarn = 0
                        if y > 0 and x > 0 and zeilen[y-1][x-1] == '@':
                            nachbarn += 1
                        if y > 0 and zeilen [y-1][x] == '@':
                            nachbarn += 1
                        if y > 0 and x + 1 < len(zeilen[y]) and zeilen [y-1][x+1] == '@':
                            nachbarn += 1
                        if x > 0 and zeilen [y][x-1] == '@':
                            nachbarn += 1
                        if x + 1 < len(zeilen[y]) and zeilen [y][x+1] == '@':
                            nachbarn += 1
                        if y + 1 < len(zeilen) and x > 0 and zeilen [y+1][x-1] == '@':
                            nachbarn += 1
                        if y + 1 < len(zeilen) and zeilen [y+1][x] == '@':
                            nachbarn += 1
                        if y + 1 < len(zeilen) and x + 1 < len(zeilen[y]) and zeilen [y+1][x+1] == '@':
                            nachbarn += 1
                        if nachbarn < 4:
                            ergebnis += 1

        
    except FileNotFoundError:
        print("File not Found")

    print(ergebnis)

part1()

def part2():
    # part 2
    ergebnis = 0
    entfernt = 1


    try:
        with open("day4.txt", "r", encoding='utf-8') as d:
            zeilen = d.read().strip().split('\n')
            zeilen = [list(zeile) for zeile in zeilen]
            while entfernt > 0:
                entfernt = 0

                for y in range(len(zeilen)):
                    for x in range(len(zeilen[y])):
                        if zeilen[y][x] == '@':
                            nachbarn = 0
                            if y > 0 and x > 0 and zeilen[y-1][x-1] == '@':
                                nachbarn += 1
                            if y > 0 and zeilen [y-1][x] == '@':
                                nachbarn += 1
                            if y > 0 and x + 1 < len(zeilen[y]) and zeilen [y-1][x+1] == '@':
                                nachbarn += 1
                            if x > 0 and zeilen [y][x-1] == '@':
                                nachbarn += 1
                            if x + 1 < len(zeilen[y]) and zeilen [y][x+1] == '@':
                                nachbarn += 1
                            if y + 1 < len(zeilen) and x > 0 and zeilen [y+1][x-1] == '@':
                                nachbarn += 1
                            if y + 1 < len(zeilen) and zeilen [y+1][x] == '@':
                                nachbarn += 1
                            if y + 1 < len(zeilen) and x + 1 < len(zeilen[y]) and zeilen [y+1][x+1] == '@':
                                nachbarn += 1
                            if nachbarn < 4:
                                ergebnis += 1
                                entfernt += 1
                                zeilen[y][x] = "X"
            
    except FileNotFoundError:
        print("File not Found")

    print(ergebnis)

part2()