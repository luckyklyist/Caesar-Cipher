import os


def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def encrypt(store_value):
    message, shift = store_value[1:]

    encrypt_message = ""

    for msg in message:
        if msg == " ":
            encrypt_message += msg
        else:
            encrypt_message += chr(ord(msg) + shift)

    write_message(encrypt_message)
    print("Encrypted message:", encrypt_message)


def decrypt(store_value):
    message, shift = store_value[1:]

    decrypt_message = ""

    for msg in message:
        if msg == " ":
            decrypt_message += msg
        else:
            decrypt_message += chr(ord(msg) - shift)

    write_message(decrypt_message)
    print("Decrypted message:", decrypt_message)


def process_file(filename, mode, shift):
    try:
        with open(filename, 'r') as f:
            msg = f.read()

        if mode == "e":
            encrypt_message = ""
            for m in msg:
                if m == " ":
                    encrypt_message += m
                else:
                    encrypt_message += chr(ord(m) + shift)
            write_message(encrypt_message)
            print("Encrypted message:", encrypt_message)
        elif mode == "d":
            decrypt_message = ""
            for m in msg:
                if m == " ":
                    decrypt_message += m
                else:
                    decrypt_message += chr(ord(m) - shift)
            write_message(decrypt_message)
            print("Decrypted message:", decrypt_message)

    except FileNotFoundError:
        print("File not found:", filename)


def is_file(filename):
    return os.path.isfile(filename)


def write_message(msg):
    with open("result.txt", 'w') as f:
        f.write(msg)


def message_or_file():
    welcome()

    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

        if mode not in ('e', 'd'):
            print("Invalid mode.")
            continue

        while True:
            reading_mode = input(
                "Would you like to read from a file (f) or the console (c)? "
            ).lower()

            if reading_mode not in ('f', 'c'):
                print("Invalid reading mode.")
                continue

            shift = input("What is the shift number: ")

            try:
                shift = int(shift)
            except ValueError:
                print("Invalid shift number.")
                continue

            if reading_mode == 'f':
                filename = input("Enter a filename: ")
                if not is_file(filename):
                    print("File not found:", filename)
                    continue
                process_file(filename, mode, shift)
                break

            elif reading_mode == 'c':
                message = input(
                    "What message would you like to {}: ".format(mode))
                store_value = (mode, message, shift)
                if mode == "e":
                    encrypt(store_value)
                elif mode == "d":
                    decrypt(store_value)
                break
        another_message = input(
            "Would you like to encrypt or decrypt another message? (y/n): "
        ).lower()
        if another_message == "n":
            break


if __name__ == "__main__":
    message_or_file()
