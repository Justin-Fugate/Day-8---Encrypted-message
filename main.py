from art import logo2

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    new_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            cipher_position = position + shift_amount
            new_text += alphabet[cipher_position]
        else:
            new_text += char
    print(f"\nThe {cipher_direction}d text is '{new_text.upper()}'\n")

print(logo2)

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift %= 26

        caesar(text, shift, direction)

        restart = input("Type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
        if restart == "no":
            should_end = True
            print("Goodbye")
    else:
        print("Please enter a proper command.")