def atbash_encode_decode(plaintext: str, decoding=False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1]
    ciphertext = ""
    for c in plaintext.upper():
        if ord("A") <= ord(c) <= ord("Z"):
            ciphertext += alphabet[ord(c) - ord("A")]
        else:
            ciphertext += c
    return ciphertext


if __name__ == '__main__':
    # Creating some basic plaintext to encode
    plaintext = "Hello, my name is Jeff!"
    ciphertext = atbash_encode_decode(plaintext)
    print("Plain Text:", plaintext)
    print("Cipher Text:", ciphertext)
