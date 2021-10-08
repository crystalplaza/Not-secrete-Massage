
import math
from decimal import *
import datetime

def encrypt():
    #Get the inputs
    plain = input("Enter the plain text: ")
    key = int(input("Enter the public key: "))
    exponent = int(input("Enter the public exponent: "))

    #plain text to ASCII bytes
    ascii_bytes = bytes(plain,"UTF-8")

    data = 0
    for byte in ascii_bytes:
        data = str(data) + str (byte)  # append each byte to data
        data = int(data)

    # (data power exponent) mod key
    cipher = pow(data,exponent,key)
    print("\n Cipher text : ", cipher)


def decrypt():
    #Get the inputs
    cipher_text = int(input("Enter the Cipher text: "))
    pub_key = int(input("Enter the public key: "))
    private_exponent = int(input("Enter the private exponent d: "))

    # C power d mod N
    plain_text = pow(cipher_text,private_exponent,pub_key)

    list_char = []
    #Convert to the ascii 
    while plain_text !=0:
        r = plain_text % 1000
        list_char.insert(0,r)
        plain_text = plain_text // 1000
	
    print("\nPlain text : ", bytes(list_char).decode())

while True:
    def main():
        print("-------CryptoSystem-------")
        try:
            input_num = int(input("Enter your choice:  1.Encrypt: 2.Decrypt: 3. Exit -- "))
            if input_num == 1:
                encrypt()
            elif input_num == 2:
                decrypt()
            elif input_num == 3:
                quit()
            else:
                print("Input should be numeric, either 1, 2 or 3")
                pass
        except Exception as e:
            print("Invalid Input, try again")
    if __name__ == "__main__":
        main()
