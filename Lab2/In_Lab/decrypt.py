""" 
  Fundamentals of Python: First Programs Chapter 04
  Programming Exercises
  
  Write a script in the file decrypt.py that inputs a line of encrypted text and a distance value and outputs plaintext using a Caesar cipher. 
  The script should work for any printable characters. (LO: 4.1, 4.2)
"""
import os

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def decrypt(encrypted_text, distance):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char == " ":
            decrypted_text += " "
        elif char.isupper():
            decrypted_text += chr((ord(char) - distance - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - distance - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    clean()

    encrypted_text = input("Enter the encrypted text: ")
    try:
        distance = int(input("Enter the distance: "))
    except ValueError:
        print("Invalid input")
        exit(1)
    print("Decrypted text: ", decrypt(encrypted_text, distance))
