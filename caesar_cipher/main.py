from cipher_alphabet import alphabet


def caesar(cipher_text, cipher_shift, cipher_direction):
    cipher = list(cipher_text)
    word = []
    if cipher_direction == "decode":
        cipher_shift *= -1
        adj = "decoded"
    elif cipher_direction == "encode":
        adj = "encoded"
    for m in range(len(cipher)):
        for n in range(len(alphabet)):
            if alphabet[n] == cipher[m]:
                word += alphabet[(n + cipher_shift) % 26]
        if cipher[m] not in alphabet:
            word += cipher[m]
    print(f"The {adj} text is: {''.join(word)}")


again = True
while again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    response = input(
        "Would you still like to use this program? Type 'yes' or 'no': "
    ).lower()
    if response == "no":
        again = False
        print("Goodbye")
