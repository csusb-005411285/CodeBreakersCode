# tc: o(n), sc: o(n)
def caesarCipherEncryptor(string, key):
    encrypted_str = ''

    for char in string:
        char_ord = ord(char)
        new_char_ord = char_ord + key

        while new_char_ord > 122:
            new_char_ord = 96 + (new_char_ord % 122)

        char_from_ord = chr(new_char_ord)
        encrypted_str += char_from_ord
    
    return encrypted_str
