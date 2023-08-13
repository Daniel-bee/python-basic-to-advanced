alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q','r','s','t','u', 'v','w','x','y','z']

direction = input("Type 'encode' to encript, type 'decode' to decript:\n")

text = input("Type your message ").lower( )

shift = int(input("Type the shift number:\n"))

def caeser(text, shift, direction):
    cipher_text = ""
    for ch in text:
        index = alphabet.index(ch)
        if direction == 'encode':
            if index >= 25:
                index = 0
                cipher_text += alphabet[shift + index - 1]
            else:
                cipher_text += alphabet[shift + index]
        elif direction == 'decode':
            cipher_text += alphabet[index - shift]
        else:
            print("Invalid Direction")
            
    print(f" The encoded text is {cipher_text} ")

caeser(text, shift, direction)