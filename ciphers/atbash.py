from cryptography_resources import ALPHABET


def atbash_encode_decode(plaintext: str, decoding=False):
    reverse_alphabet = ALPHABET[::-1]
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha():
            ciphertext += reverse_alphabet[ord(c) - ord("A")]
        else:
            ciphertext += c
    return ciphertext


if __name__ == '__main__':
    # Creating some basic plaintext to encode
    plaintext = "Hello, my name is Jeff!"
    ciphertext = atbash_encode_decode(plaintext)
    print("Plain Text:", plaintext)
    print("Cipher Text:", ciphertext)
