alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(encode_or_decode, original_text, shift_amount ):
   if encode_or_decode == 'encode':
       encrypt(original_text, shift_amount)
   elif encode_or_decode == 'decode':
       decrypt(original_text, shift_amount)


def decrypt(original_text, shift_amount):
   decrypted_text = ""
   for letter in original_text:
       if letter not in alphabet:
           encrypted_text += letter
       else:
           index_1 = alphabet.index(letter)
           index_2 = index_1 + shift_amount
           index_2 = index_2 % len(alphabet)
           shifted_letter = alphabet[index_2]
           decrypted_text += shifted_letter
   print(decrypted_text)




def encrypt(original_text, shift_amount):
   encrypted_text = ""
   for letter in original_text:
       if letter not in alphabet:
           encrypted_text += letter
       else:
           index_1 = alphabet.index(letter)
           index_2 = index_1 + shift_amount
           index_2 = index_2 % len(alphabet)
           shifted_letter = alphabet[index_2]
           encrypted_text += shifted_letter
   print(encrypted_text)


caesar(direction, text, shift)

