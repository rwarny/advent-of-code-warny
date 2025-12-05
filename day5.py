from clearscreen import clearscreen
def part1():
    # part 1
    ergebnis = 0

    try:
        with open("day5.txt", "r", encoding='utf-8') as d:
            bereiche, zahlen = d.read().strip().split('\n\n')
    
    except FileNotFoundError:
        print("File Not Found")

    bereiche = bereiche.split("\n")
    zahlen = zahlen.split("\n")

    for zahl in zahlen:
        zahl = int(zahl)
        gefunden = False
        for r in bereiche:
            x, y = r.split("-")
            x = int(x)
            y = int(y)
            if x <= zahl <= y:
                ergebnis += 1
                gefunden = True
                break

    print(ergebnis)

part1()

def part2():
    clearscreen()
    # part 2

    try:
        with open("day5.txt", "r", encoding='utf-8') as d:
            bereiche, zahlen = d.read().strip().split('\n\n')
    
    except FileNotFoundError:
        print("File Not Found")

    # bereiche sammeln und sortieren
    bereiche = bereiche.split("\n")
    bereiche_liste = []
    for r in bereiche:
        x, y = r.split("-")
        bereiche_liste.append((int(x), int(y)))

    bereiche_liste.sort()

    # Bereiche miteinander vergleichen, startend bei ersten bereich
    start, ende = bereiche_liste[0]
    ergebnis = 0

    # Durch die anderen bereiche gehen
    for i in range(1, len(bereiche_liste)):
        neuer_start, neues_ende = bereiche_liste[i]

        if neuer_start <= ende + 1:
            # Bereiche Überlappen sich, also verschmelzen
            ende = max(ende, neues_ende)
        else:
            # Bereiche überlappen sich nicht, alter bereich wird gezählt
            ergebnis += ende - start +1
            # starte neu, mit dem neuen bereich
            start = neuer_start
            ende = neues_ende
    #letzten bereich noch zählen
    ergebnis += ende - start + 1

    print(ergebnis)

part2()


