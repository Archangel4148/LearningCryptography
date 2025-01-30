def caesar_encode_decode(plaintext: str, offset: int, decoding=False):
    ciphertext = ""
    offset = -offset if decoding else offset
    if offset < 0:
        offset = (offset + 26) % 26
    for character in plaintext.upper():
        if character.isalpha():
            relative_ord = (ord(character) - ord("A") + offset) % 26
            ciphertext += chr(ord("A") + relative_ord)
        else:
            ciphertext += character
    return ciphertext


if __name__ == '__main__':
    plaintext = "The quick brown fox's mother is quite gray."
    shift = 1
    ciphertext = caesar_encode_decode(plaintext, int(shift))
    print("Plain text:", plaintext)
    print("Cipher text:", ciphertext)
    print("Decoded text:", caesar_encode_decode(ciphertext, int(shift), decoding=True))
