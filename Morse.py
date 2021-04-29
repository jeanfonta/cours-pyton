def trad_to_morse(phrase):
    morse = " "
    for c in phrase:
        for k, value in dico_morse.items():
            if k == c:
                morse = morse + value    # ici que j'ai changé pour que ca imprime les uns a la suite des autres
    return morse


def phrase_autorisee(phrase): 
    for c in phrase:
        if c in dico_morse.keys():
            return True
    return False


dico_morse = {"A": ".-", "B": "– • • •", "C": "– • – •", "D": "– • •", "E": "•", "F": "• • – •", "G": "– – •",
              "H": "• • • •", "I": "• •", "J": "• – – –", "K": "– • –", "L": "• – • •", "M": "– –",
              "N": "– •", "O": "– – –", "P": "• – – •", "Q": "– – • –", "R": "• – •", "S": "• • •", "T": "–",
              "U": "• • –", "V": "• • • –", "W": "• – –", "X": "– • • –", "Y": "– • – –", "Z": "– – • •",
              ".": "• – • – • –", "?": "• • – – • •", "!": "– • – • – –", "@": "• – – • – •", "0": "– – – – –",
              "1": "• – – – –", "2": "• • – – –", "3": "• • • – –", "4": "• • • • –", "5": "• • • • •",
              "6": "– • • • •", "7": "– – • • •", "8": "– – – • •", "9": "– – – – •"}

phrase = input("Entrez une phrase: ").upper()

while not phrase_autorisee(phrase):
    phrase = input("Caractère(s) incorrect(s), veuillez encoder une nouvelle phrase: ").upper()
print(trad_to_morse(phrase))





