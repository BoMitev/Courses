def morse(txt):

    d = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
         'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
         'Z': '--..', ' ': '.....'}

    message = ""
    encrypt = dict([(v, k) for k, v in d.items()])
    txt = txt.split()
    for char in txt:
        if char == "|":
            message += " "
        else:
            message += encrypt.get(char)
    return message.strip()


print(morse(input()))