import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def encrypt(text, shift):
  cipher = ""
  for letter in text:
    if letter in alphabet:
      pos = alphabet.index(letter)
      newpos = (pos + shift) % len(alphabet)
      cipher += alphabet[newpos]
    else:
      cipher += letter

  print(f"The encoded text is {cipher} .")

def decrypt(text, shift):
  message = ""
  for letter in text:
    if letter in alphabet:
      pos = alphabet.index(letter)
      newpos = pos - shift
      if newpos < 0:
        newpos += 26
      message += alphabet[newpos]
    else:
      message += letter

  print(f"The decoded text is {message}")

def caesar(direction, text, shift ):
  if direction.lower() == "encode":
    encrypt(text, shift)
  elif direction.lower() == "decode":
    decrypt(text, shift)

flag = True
while flag:
  direction = input("Type 'encode' to encrypt, type 'decode' to     decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction, text, shift)
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if again.lower() == "no":
    flag = False