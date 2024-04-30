def _encrypt_uppercase(char, s):
    return chr((ord(char) + s - 65) % 26 + 65)


def _encrypt_lowercase(char, s):
    return chr((ord(char) + s - 97) % 26 + 97)


def _decrypt_uppercase(char, s):
    return chr((ord(char) + (26 - s) - 65) % 26 + 65)


def _decrypt_lowercase(char, s):
    return chr((ord(char) + (26 - s) - 97) % 26 + 97)


def encode(text, offset=3):
    ans = ""
    # iterate over the given text
    for i in range(len(text)):
        char = text[i]

        # si hay espacios se concatenan
        if char == " ":
            ans += " "
        # caso mayusculas
        elif char.isupper():
            ans += _encrypt_uppercase(char,offset)
        # caso minusculas
        else:
            ans += _encrypt_lowercase(char,offset)

    return ans


def decode(text, offset=3):
    result = ""
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += _decrypt_uppercase(char, offset)
        # Encrypt lowercase characters
        else:
            result += _decrypt_lowercase(char, offset)
    return result
