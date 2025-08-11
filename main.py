# Welcome message

print(
   '''
   Welcome to MCT.
   Type 'help' for a list of commands.
   ''' 
)

help = ('''
        1 - English to Morse code
        2 - Morse code to English
        help - shows list of commands
        exit - exit the mode or program 
        ''')

# Morse dictionary

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# English dictionary

english_dict = {v: k for k, v in morse_dict.items()}

# Logic


while True:

    # User input

    mode = input("$ ").strip()
    if mode.lower() == "exit":
        break

    # English to Morse mode

    if mode == '1' or mode == '1.':
        print("You are currently using English to Morse.")
        while True:
            line = input("$ ").strip()
            if line.lower() == "exit":
                break
            result = []
            for char in line:
                result.append(morse_dict.get(char.upper(), "?"))
            print(" ".join(result))

    # Morse to English mode

    elif mode == '2' or mode == '2.':
        print("You are currently using Morse to English.")
        while True:
            line = input("$ ").strip()
            if line.lower() == "exit":
                break
            result = []
            codes = line.split()
            for code in codes:
                result.append(english_dict.get(code, "?"))
            print("".join(result))

    # Help 

    elif mode.lower() == 'help':
        print(help)

    else:
        print("Invalid input. Type 'help' for list of commands. ")
