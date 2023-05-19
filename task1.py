def main():
    keys_and_values = {
        'x': 'a',
        'z': 'b',
        'n': 'c',
        'l': 'd',
        'w': 'e',
        'e': 'f',
        'b': 'g',
        'g': 'h',
        'j': 'i',
        'h': 'j',
        'q': 'k',
        'd': 'l',
        'y': 'm',
        'v': 'n',
        't': 'o',
        'k': 'p',
        'f': 'q',
        'u': 'r',
        'o': 's',
        'm': 't',
        'p': 'u',
        'c': 'v',
        'i': 'w',
        'a': 'x',
        's': 'y',
        'r': 'z',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }

    def Menu():
        while True:
            print("MENU")
            print("E: Encrypting function")
            print("D: Decrypting function")
            print("EX: Exit")
            user_choice = input("Choose an option: ").upper()
            if user_choice == "E":
                encrypt_value = input("Enter the message: ").lower()
                if encrypt_value == "":
                    print("The input message should be a non-empty string")
                else:
                    output_ciphertext = Encrypting(encrypt_value)
                    print(''.join(output_ciphertext))
            elif user_choice == "D":
                decrypt_value = input("Enter the message: ").lower()
                if decrypt_value == "":
                    print("The input message should be a non-empty string")
                else:
                    output_plaintext = Decrypting(decrypt_value)
                    print(''.join(output_plaintext))
            elif user_choice == "EX":
                break
            else:
                print("Invalid choice. Please try again.")

    def Encrypting(encrypt_value):
        cipher_text = []
        for i in encrypt_value:
            if i in keys_and_values:
                cipher_text.append(keys_and_values[i])
            else:
                cipher_text.append(i)
        return cipher_text

    def Decrypting(decrypt_value):
        plain_text = []
        for i in decrypt_value:
            for key, val in keys_and_values.items():
                if val == i:
                    plain_text.append(key)
                    break
            else:
                plain_text.append(i)
        return plain_text

    Menu()


if __name__ == "__main__":
    main()
