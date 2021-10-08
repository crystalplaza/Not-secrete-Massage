import math
from decimal import *
import datetime

###########################################################################################
####################### Crack the challenge ###################################################
###########################################################################################

## using newton's method to find the square root of a number, the time complexity to compute 
#is O(logn)
def isqrt(num):
    x = num
    y = (x + 1) // 2

    while y < x:
        x = y
        y = (x + num // x) // 2

    return x

# calculate the d, which is multiplicative inverse for e mod n
# Uses extended Euclidean algorithm ex + ny = 1, solve for x
## time complexity O(e)
def private_key(e, n):
    n_initial = n
    x = 1
    y = 0

    while e > 1:
        q = e // n
        t = n
        n = e % n
        e = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + n_initial

    return x

## check if a number if perfect square
def check_perfect_square(n):
    last_digit = n % 10
    prev_digit = (n // 10) % 10
  
    # If a numeber is a perfect square, last digit must be 0, 1, 4, 5, 6, or 9
    ## source from wiki
    if last_digit not in (0, 1, 4, 5, 6, 9):
        return False
    if (last_digit in (1, 4, 9) and prev_digit % 2 != 0):
        return False
    if last_digit == 0 and prev_digit != 0:
        return False
    if last_digit == 5 and prev_digit != 2:
        return False
    if last_digit == 6 and prev_digit % 2 != 1:
        return False
    r = isqrt(n)
    if n - r * r != 0:
        return False
    return True


# Fermat factorization to factor N into p, q, here p = x-y, q = x+y, time complexity O(n)
def fermat_factorization(n):
    x = isqrt(n)
    y_square = x * x - n
    while check_perfect_square(y_square) == False:
        x = x + 1
        y_square = x * x - n
    y = isqrt(y_square)
    return ((x-y), (x+y))

## decrypt cryphertext using m = c^d mod n
def decrypt_cipher_text(ct,d,N):
        plaintext= pow(ct,d,N)
        return plaintext

#Converts binary data to ASCII string
def binary_to_ASCII(bin_data):
    step =8
    data_len = len(bin_data)
    ASCIIResult = bytes(int(bin_data[start:start+step],2) for start in range(0,data_len,step))
    return ASCIIResult.decode()

## compute the time to crack the cypher, private key d
def decrypt():
    start_time = datetime.datetime.now()
    ## enter the cipher_text, n , and e
    cipher_text = int(input("Enter the cipher text : "))
    key = int(input("n : "))
    e = int(input("e: "))

    print("Breaking the key...")
    p, q = fermat_factorization(key)
    N = p*q
    if(N == key):
        print("\n====RSA private key cracked!======")
        totient=(p-1)*(q-1)

        #Private Key calcuation and Decryption
        d= private_key(e,totient)
        padded_plain_text=decrypt_cipher_text(cipher_text,d,N)

        #Padding data strip and ascii conversion
        bin_plain_text = bin(padded_plain_text)[-200:]
        plain_text = binary_to_ASCII(bin_plain_text)

        time_taken = datetime.datetime.now() - start_time
    
        print("\nKey Summary:\nP : ",p,"\nQ : ",q,"\nPrivate key d : ",d)
        print("\nPlain Text : ", plain_text)
        print("\nIt takes:" ,time_taken.seconds, " seconds to break the RSA! ")
    else:
        print("Failed")

def main():
    print("-------Cryptanalysis-------")
    decrypt()

if __name__ == "__main__":
    main()
