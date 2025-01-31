from cryptography_resources import ALPHABET


def aristocrat_encode_decode(plaintext: str, mapping: str, decoding=False):
    mapping = mapping.upper()
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha():
            if decoding:
                ciphertext += ALPHABET[mapping.index(c)]
            else:
                ciphertext += mapping[ALPHABET.index(c)]
        else:
            ciphertext += c
    return ciphertext


if __name__ == '__main__':
    # Creating some basic plaintext and using a mapping to encode
    plaintext = "The quick brown fox jumps over the lazy dog"
    mapping = "QWERTYUIOPASDFGHJKLZXCVBNM"
    ciphertext = aristocrat_encode_decode(plaintext, mapping)
    print("Plain Text:", plaintext)
    print("Cipher Text:", ciphertext)

    # Decoding and printing output
    print("Decoded Text:", aristocrat_encode_decode(ciphertext, mapping, True))
