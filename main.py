alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
run = True

def ceaser(plain_text, shift_amount,cipher_direction):
  if shift_amount >26:
    shift_amount %=26
    round(shift_amount)

  cipher_text = ""
  if cipher_direction =="decode":
      shift_amount *= -1
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    else:
      cipher_text +=letter
  print(f"The {cipher_direction}d text is {cipher_text}")
   
  
while run == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceaser(plain_text = text, shift_amount = shift,cipher_direction = direction)
  ask = input("Would you like to run again? Type 'yes' to run again and 'no' to exit\n").lower()
  if ask =="yes":
    run=True
  elif ask == "no":
    run = False  
