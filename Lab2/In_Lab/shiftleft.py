""" 
  Fundamentals of Python: First Programs 3rd Edition Chapter 4

  Define two scripts, shiftleft.py and shiftright.py, that expect a bit string as an input. 
  The script shiftLeft shifts the bits in its input one place to the wrapping the leftmost bit 
  to the rightmost position. The script shiftRight performs the inverse operation. Each script 
  prints the resulting string.

"""

import os

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def shiftleft(bitstring):
    if len(bitstring) == 0:
        return bitstring
    # Wraps the leftmost bit to the right
    return bitstring[1:] + bitstring[0]

def main():
    bitstring = input("Enter your bit string: ").strip()
    if not all(bit in '01' for bit in bitstring):
        print("Error: Should only be a valid bit string that contain 0s and 1s.")
        return
    shifted = shiftleft(bitstring)
    print(f"Shifted left: {shifted}")

if __name__ == "__main__":
    main()