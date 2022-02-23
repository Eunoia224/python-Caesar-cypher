import string
chars = ''.join(chr(i) for i in range(128))
chars_list = []
for char in chars:
    chars_list += char


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for char in start_text:
      if char in chars_list:
        position = chars_list.index(char)
        new_position = position + shift_amount
        end_text += chars_list[new_position]
      else:
          end_text += char
  print(f"Here's the {direction}d result: {end_text}")


go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    request_to_go_again = input(
        "Type 'Yes' if you want to go again and 'No' if you want to exist\n").lower()
    if request_to_go_again == "no":
        go_again = False
        print("Ciao")
    elif request_to_go_again == "yes":
        go_again = True
        print("here we go again")
    else:
        print("Wrong input, Exiting......")
        go_again = False
