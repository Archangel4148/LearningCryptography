from cryptography_resources import calculate_difference_from_english


def caesar_encode_decode(plaintext: str, offset: int, decoding=False):
    """Encode plaintext using a simple rotation (Caesar) cipher"""
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


def crack_caesar_shift(ciphertext: str):
    """Find the shift value that decodes a Caesar cipher to the "best" plaintext (most similar to English)"""
    scores = []
    for shift in range(26):
        decoded_text = caesar_encode_decode(ciphertext, shift, decoding=True)
        scores.append(calculate_difference_from_english(decoded_text))

    return scores.index(min(scores))


if __name__ == '__main__':
    # Encoding some sample plaintext
    plaintext = "The quick brown fox's mother is quite gray."
    shift = 9
    ciphertext = caesar_encode_decode(plaintext, int(shift))
    print("Plain Text:", plaintext)
    print("Cipher Text:", ciphertext)

    # Finding the most likely shift value to decrypt
    best_shift = crack_caesar_shift(ciphertext)
    print(f"\nPredicted Shift: {best_shift} (or {best_shift - 26})")
    print("Predicted Decryption:", caesar_encode_decode(ciphertext, best_shift, decoding=True))
