#Ceasar Cipher

'''Nothing but Encrypting and Decrypting the Word that user enters with the use of shift value from the user input
eg: ask user encode or decode - if encode then ask following
plain_text = "hello"
    shift = 5
    cipher_text = "mjqqt"
    print output: "The encoded text is mjqqt
    
    if decode 
    plain_text = "mjqqt"
    shift = 5
    cipher_text = "hello"
    print output: "The decoded text is hello
    
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛'''

'''direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))'''

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
def encode(text,shift):
    encoded_text=""
    for texts in text:
        text_val=ord(texts)+shift
        if text_val>ord("z"):
            text_val=(ord("a")-1)+(text_val-ord("z"))
        encoded_text+=chr(text_val)
    return encoded_text

def decode(text,shift):
    decoded_text=""
    for texts in text:
        text_val=ord(texts)-shift
        if text_val<ord("a"):
            text_val=(ord("z")+1)-(ord("a")-text_val)
        decoded_text+=chr(text_val)
    return decoded_text


while True:
    if direction=="encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(f"your encoded text is '{encode(text,shift)}'")
        value=input("Do you want to continue, Type Yes or No:\n").lower()
        if value=="yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        else:
            break
    elif direction=="decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(f"your decoded text is '{decode(text,shift)}'")
        value=input("Do you want to continue, Type Yes or No:\n").lower()
        if value=="yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        else:
            break
    else:
        print("You entered something else, plese type the following")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()




#another method
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)