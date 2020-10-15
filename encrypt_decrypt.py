# Encrypts/ decrypts given input string based on user preference

def encrypt_message(message: str) -> str:
    result = ''
    for ch in message:
        if ch.isalpha():
            result += ch.swapcase()
        elif ch.isnumeric():
            result += str(int(ch) + 1)
        else:
            result += ch
    return result


def decrypt_message(message: str) -> str:
    result = ''
    for ch in message:
        if ch.isalpha():
            result += ch.swapcase()
        elif ch.isnumeric():
            result += str(int(ch) - 1)
        else:
            result += ch
    return result


if __name__ == "__main__":
    # loop till user opts exit
    while(True):
        # ask for user preference
        pref = input("\n".join(['e - Encrypt message',
                                'd - Decrypt message',
                                'x - Exit program',
                                'Enter your preference (e/d/x):']))
        # user opted for exit
        if pref == 'x':
            break

        # get input string from user
        s = input('Please provide the string: ')

        if pref == 'e':  # invoke encryption algorithm
            print('Encrypted message: ', encrypt_message(s))
        elif pref == 'd':  # invoke decryption algorithm
            print('Decrypted message: ', decrypt_message(s))
        else:
            print('ERROR: invalid input!')
