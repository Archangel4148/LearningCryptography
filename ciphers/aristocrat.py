from cryptography_resources import ALPHABET


def encode_aristocrat(plaintext: str, mapping: str):
    mapping = mapping.upper()
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha():
            ciphertext += mapping[ALPHABET.index(c)]
        else:
            ciphertext += c
    return ciphertext


if __name__ == '__main__':
    # Creating some basic plaintext to encode
    plaintext = "The quick brown fox jumped over the lazy dog"
    mapping = "QWERTYUIOPASDFGHJKLZXCVBNM"
    ciphertext = encode_aristocrat(plaintext, mapping)
    print("Plain Text:", plaintext)
    print("Cipher Text:", ciphertext)
