# Caesar Cipher

This program implements the Caesar Cipher algorithm to encrypt and decrypt text.

## Overview

The Caesar Cipher is a simple encryption algorithm that works by shifting the letters in the plaintext by a certain number of positions. For example, if the shift number is 3, then the letter 'A' in the plaintext becomes 'D' in the ciphertext. The shift number can be any integer between 0 and 25.


## Getting Started

To use the Caesar Cipher program, follow these steps:

1. Clone the repository or download the files.

```
git clone https://github.com/luckyklyist/Caesar-Cipher
```
2. Open the terminal or command prompt and navigate to the directory containing the files.
3. Run the command `python caesar.py` to start the program.
```
python caesar.py
```


## Functions

The program is divided into several functions, each with a specific purpose:

### welcome()

Displays a welcome message to the user.
```
def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
```


### `encrypt(store_value)`

Encrypts the given message using the Caesar Cipher and writes the result to a file.

```
def encrypt(store_value):
    message, shift = store_value[1:]

    encrypt_message = ""

    for msg in message:
        encrypt_message += chr(ord(msg) + shift)

    write_message(encrypt_message)
    print("Encrypted message:", encrypt_message)
```
### `decrypt(store_value)`

Decrypts the given message using the Caesar Cipher and writes the result to a file.

```
def decrypt(store_value):
    message, shift = store_value[1:]

    decrypt_message = ""

    for msg in message:
        decrypt_message += chr(ord(msg) - shift)

    write_message(decrypt_message)
    print("Decrypted message:", decrypt_message)
```

### `process_file(filename, mode, shift)`

Reads the message from the given file and either encrypts or decrypts it, depending on the mode.

```
def process_file(filename, mode, shift):
    try:
        with open(filename, 'r') as f:
            msg = f.read()

        if mode == "e":
            encrypt_message = ""
            for m in msg:
                encrypt_message += chr(ord(m) + shift)
            write_message(encrypt_message)
            print("Encrypted message:", encrypt_message)
        elif mode == "d":
            decrypt_message = ""
            for m in msg:
                decrypt_message += chr(ord(m) - shift)
            write_message(decrypt_message)
            print("Decrypted message:", decrypt_message)

    except FileNotFoundError:
        print("File not found:", filename)
```
### `is_file(filename)`

Checks if the given file exists.

```
def is_file(filename):
    return os.path.isfile(filename)
```

### `write_message(msg)`

Writes the given message to a file named "result.txt".

```
def write_message(msg):
    with open("result.txt", 'w') as f:
        f.write(msg)
```

### `message_or_file()`

Prompts the user to choose whether to read the message from a file or the console, and whether to encrypt or decrypt the message.

```
def message_or_file():
    welcome()

    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

        if mode not in ('e', 'd'):
            print("Invalid mode.")
            continue

        

        while True:
            reading_mode = input("Would you like to read from a file (f) or the console (c)? ").lower()

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
                process_file(filename,mode,shift)
                break

            elif reading_mode == 'c':
                message = input("What message would you like to {}: ".format(mode))
                store_value = (mode, message, shift)
                if mode == "e":
                    encrypt(store_value)
                elif mode == "d":
                    decrypt(store_value)
                break
        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message == "n":
            break
```

### `main()`

Runs the program.

```
if __name__ == "__main__":
    message_or_file()
```

## Conclusion

The Caesar Cipher is a simple but effective encryption algorithm that can be used to secure messages. This implementation of the Caesar Cipher demonstrates how the algorithm can be used to encrypt and decrypt messages using Python.

## Contribution Guide

Thank you for considering contributing to our project! We welcome any contributions, big or small, including bug fixes, new features, and improvements to the documentation.

### Getting Started

1. Fork the project repository.
2. Clone the forked repository to your local machine.
3. Install any necessary dependencies.
4. Create a new branch for your changes.
5. Make your changes and commit them with clear and descriptive commit messages.
6. Push your changes to your forked repository.
7. Open a pull request to merge your changes into the main repository.

### Style Guide

Please follow these guidelines when making contributions:

- Use clear and concise commit messages.
- Follow the code style and formatting conventions used in the project.
- Write clear and concise documentation.
- Include tests for any new functionality.

### Code of Conduct

Please note that we have a Code of Conduct in place to ensure a welcoming and inclusive community. By contributing to this project, you are expected to abide by its terms.

### Reporting Bugs

If you encounter a bug or issue, please open a new issue in the project's issue tracker. Please include a clear and concise description of the issue, as well as any relevant code or steps to reproduce the issue.

### Contact

If you have any questions or concerns about contributing, please contact us at anupam.aclc.chauhan@gmail.com or https://anupamac.me. We appreciate your interest in the project and look forward to your contributions!
