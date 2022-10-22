from math import gcd
import pyperclip

max_n = 1114112

f = open("codes.txt", "r")
lines = f.readlines()[0]
lst = lines.split()
lst[0] = int(lst[0])
lst[1] = int(lst[1])

def encrypt(a, b, message):
    result = ""
    if gcd(a, max_n) != 1:
        raise Exception("ERROR: a and 1,114,112 must be coprime.")
    for letter in message:
        encr_letter = ( a*ord(letter) + b ) % max_n
        result += chr(encr_letter)
    return result

def decrypt(a, b, message):
    result = ""
    a_inv = pow(a, -1, max_n)
    for letter in message:
        decr_letter = ( a_inv * ( ord(letter) - b ) ) % max_n
        result += chr(decr_letter)
    return result

while True:
    inpt = str(input(">>> "))
    if inpt == 'e':
        msg = str(input("Enter a message to encrypt: "))
        encr_msg = encrypt(lst[0], lst[1], msg) 
        pyperclip.copy(encr_msg)
        print("Your message has been encrypted and copied to the clipboard. The encrypted message is shown below.")
        print(encr_msg)

    elif inpt == 'h':
        print("'e' --- encryption\n'd' --- decryption\n'h' --- help\n'q' --- quit")

    elif inpt == 'd':
        msg = str(input("Enter a message to decrypt: "))
        decr_msg = decrypt(lst[0], lst[1], msg)
        print("Your message has been decrypted and is shown below.")
        print(decr_msg)
    elif inpt == 'q':
        print("Application closed.")
        break
    else:
        print("Unrecognised command " + "'" + inpt + "'. " + "Type 'h' for a list of commands.")
