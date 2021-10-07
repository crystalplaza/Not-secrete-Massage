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


#def decrypt():


def main():
    print("-------CryptoSystem-------")
    input_num = int(input("Enter your choice 1.Encrypt: 2.Decrypt:"))
    if input_num == 1:
        encrypt()
    elif input_num == 2:
    #    decrypt()
        print("test")
    else:
        print("Input should be either 1 or 2")

if __name__ == "__main__":
    main()
