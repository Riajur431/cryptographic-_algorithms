# -*- coding: utf-8 -*-
"""Hill_Cipher.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15WU5gi6csVPyU8kcv8p6RuXzQlbWOXTz
"""

import sys
import numpy as np

def Key_input():

  print("Please enter your key in a single line and separated by a space: ")

  # User will give the key in a single line
  elements = list(map(int, input().split()))

  matrixx = np.array(elements).reshape(2, 2)

  return matrixx


def cipher_encryption():
  plaintext = input("Enter Plain text: ").lower()
  plaintext = plaintext.replace(" ", "")
  result=""
  key=Key_input()

  i=0
  while i < len(plaintext):
      a = ord (plaintext[i]) -97
      b = ord(plaintext[i+1]) - 97
      #c = ord(plaintext[i+2]) - 97
      matrix = np.array([[a],
                       [b]])
      cipher = np.dot(key, matrix ) %26      # matrix multiplication
      list = cipher.flatten().tolist()       #convert matrix into list
      for j in range(2):
          result += chr(list[j]+97)
      i=i+2

  print("plaintext is: ",plaintext)
  print("Key is: \n",key)
  print("Ciphertext is: ", result)

def cipher_decryption():
    ciphertext = input("Enter Plain text: ").lower()
    ciphertext = ciphertext.replace(" ", "")

    key=Key_input()
    modulus=26
    det = int(np.round(np.linalg.det(key)))  # Step 1)
    r1=26
    r2 =det
    t1=0
    t2=1

    while r2 > 0:
      d= r1//r2
      R= r1%r2
      t=t1-(t2*d)
      r1=r2
      r2=R
      t1=t2
      t2=t
    print(t1)
    matrix_modulus_inv = (t1 * np.round(det * np.linalg.inv(key)).astype(int) % modulus)
    result=""
    i=0
    while i < len(ciphertext):
        a = ord(ciphertext[i]) -97
        b = ord(ciphertext[i+1]) - 97
        matrix = np.array([[a],
                       [b]])
        cipher = np.dot(matrix_modulus_inv, matrix)%26      # matrix multiplication
        list = cipher.flatten().tolist()                    # convert matrix into list
        for j in range(2):
            result += chr(list[j]+97)
        i = i+2

    print("Ciphertext is: ",ciphertext)
    print("Key is:\n",key)
    print("plaintext is: ",result)





def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("---Encryption---")
        cipher_encryption()
    elif choice == 2:
        print("---Decryption---")
        cipher_decryption()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()