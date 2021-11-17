# def greet_with_name(name, location = "Clovis"):
#     print(f'My name is {name}, what is it like in {location}')
#
# greet_with_name(location = "Taipei", name = "Cynthia")

# Day 8.1 Area Calc
# import math
# def paint_calc(height, width, cover):
#     number_cans = math.ceil((height*width)/coverage)
#     print(f'You\'ll need {number_cans} cans of paint.')
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Day 8.2 Prime Number Checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
# n = int(input("Check this number: "))
# prime_checker(number = n)

# Day-8 Final project: Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
direction = 'encode'
text = 'hello'
shift = 5
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    new_text = ""
    for letter in plain_text:
        shifted_index = alphabet.index(letter) + shift_amount
        new_text += alphabet[shifted_index]
    return new_text
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        shifted_index = alphabet.index(letter) - shift_amount
        decrypted_text += alphabet[shifted_index]
    return decrypted_text

def caesar(text, shift_amount, direction):
    new_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in text:
        shifted_index = alphabet.index(letter) + shift_amount
        new_text += alphabet[shifted_index]
    return new_text

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypted = encrypt(plain_text = text, shift_amount = shift)
# print(f'Encrypted text is {encrypted}')
# decrypted_text = decrypt(encrypted_text = encrypted, shift_amount = shift)
# print(f'Decrypted text is {decrypted_text}')
direction = 'encode'
encrypted_text = caesar(text, shift, direction)
direction = 'decode'
decrypted_text = caesar(encrypted_text, shift, direction)

print(f'Encrypted text is {encrypted_text} and decrypted text is {decrypted_text}')