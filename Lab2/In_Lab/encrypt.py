import os

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def encrypt(plaintext, distance):
    encrypted_text = ""
    for x in range(len(plaintext)):
        char = plaintext[x]
        if char.isupper():
            encrypted_text += chr((ord(char) + distance - 65) % 26 + 65)
        else:
            encrypted_text += chr((ord(char) + distance - 97) % 26 + 97)
    return encrypted_text
    
if __name__ == "__main__":
    clean()

    plaintext = input("Enter a word: ")
    try:
        distance = int(input("Enter an integer for its distance: "))
    except ValueError:
        print("Invalid input")
        exit(1)
    print("Encrypted text: ", encrypt(plaintext, distance))