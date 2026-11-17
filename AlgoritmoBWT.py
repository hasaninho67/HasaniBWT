def trasformata_BWT(parola):
    

    parola = (parola+"$")

    trasformata = []
    for i in range(len(parola)):
        trasformata.append(parola[i:] + parola[:i])
    
    for i in range(len(trasformata)):
        for j in range(len(trasformata) - 1 - i):
            if trasformata[j] > trasformata[j + 1]:
                trasformata[j], trasformata[j + 1] = trasformata[j + 1], trasformata[j]

    BWT = ""
    for rotazione in trasformata:
        BWT += rotazione[-1]
    return BWT