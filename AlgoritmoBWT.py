stringa = input("inserisci una stringa: ")
print()
print(stringa)
print("1--> aggiunta del carattere dollaro come fine della stringaba")
stringa+="$"
print(stringa)
print("2--> riordinamento in senso antiorario")

rotazioni = []
for i in range(len(stringa)):
    rotazioni.append(stringa[i:] + stringa[:i])
print(rotazioni)