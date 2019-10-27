"""
Tung Hoang - 10/17/19
This programs takes in a keyword and use the Vingere cipher to translate a
plaintext into the correspond ciphertext according to the keyword
"""

# Constant
ASCII_a = 97
ASCII_z = 122
ASCII_A = 65
ASCII_Z = 90
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function helps cipher the text base on the letter case and keyword
def cipher(case, i):
    global count
    i = (ord(i) - case + correspondNum[count]) % 26
    i = chr(i + case)
    if count == len(keyword) - 1:
        count = 0
    else:
        count += 1
    return i

# Variable
cipherText = ""
correspondNum = []
count = 0
keyword = input ("Keyword: ")

# Error check to see if keyword is valid
if keyword.isdigit() or keyword == "" or (' ' in keyword):
    print ("Bad keyword")

else:
    # Finding the sequence of number that the keyword corresponds
    keyword = keyword.lower()
    for i in keyword:
        i = ord(i) - ASCII_a
        correspondNum.append(i)

    # Finding the cipher text    
    plainText = input("Plaintext: ")
    for i in plainText:
        # When it is not a letter
        if not(i in ALPHABET):
            i = i

        # When the letter is upper case
        elif ASCII_A <= ord(i) <= ASCII_Z:
            i = cipher(ASCII_A, i)

        # When the letter is lower case   
        elif ASCII_a <= ord(i) <= ASCII_z:
            i = cipher(ASCII_a, i)
            
        cipherText += i

    print ("Ciphertext: " + cipherText)
