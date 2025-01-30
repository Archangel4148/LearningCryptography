from cryptography_resources import calculate_letter_frequency, calculate_difference_from_english


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


def crack_shift(ciphertext: str):
    scores = []
    for shift in range(26):
        decoded_text = caesar_encode_decode(ciphertext, shift, decoding=True)
        scores.append(calculate_difference_from_english(decoded_text))

    return scores.index(min(scores))


if __name__ == '__main__':
    plaintext = "The quick brown fox's mother is quite gray."
    shift = 9
    ciphertext = caesar_encode_decode(plaintext, int(shift))
    print("Plain Text:", plaintext)
    print("Cipher Text:", ciphertext)

    best_shift = crack_shift(ciphertext)
    print(f"\nPredicted Shift: {best_shift} (or {best_shift-26})")
    print("Predicted Decryption:", caesar_encode_decode(ciphertext, best_shift, decoding=True))
