from cryptography_resources import calculate_difference_from_english, Cipher


class CaesarCipher(Cipher):
    def __init__(self, text: str):
        super().__init__(text)
        self.offset = 0

    def encrypt(self, text=None):
        text = text if text else self.text
        ciphertext = ""
        if self.offset < 0:
            self.offset = (self.offset + 26) % 26
        for character in text.upper():
            if character.isalpha():
                relative_ord = (ord(character) - ord("A") + self.offset) % 26
                ciphertext += chr(ord("A") + relative_ord)
            else:
                ciphertext += character
        return ciphertext

    def decrypt(self, text=None):
        text = text if text else self.text
        ciphertext = ""
        self.offset = -self.offset
        if self.offset < 0:
            self.offset = (self.offset + 26) % 26
        for character in text.upper():
            if character.isalpha():
                relative_ord = (ord(character) - ord("A") + self.offset) % 26
                ciphertext += chr(ord("A") + relative_ord)
            else:
                ciphertext += character
        return ciphertext


def crack_caesar_shift(ciphertext: str):
    """Find the shift value that decodes a Caesar cipher to the "best" plaintext (most similar to English)"""
    decryption = CaesarCipher(ciphertext)
    scores = []
    for shift in range(26):
        decryption.offset = shift
        decoded_text = decryption.decrypt()
        scores.append(calculate_difference_from_english(decoded_text))

    return scores.index(min(scores))


if __name__ == '__main__':
    # Encoding some sample plaintext
    caesar = CaesarCipher("The quick brown fox's mother is quite gray.")
    caesar.offset = 9

    ciphertext = caesar.encrypt()
    print("Plain Text:", caesar.text)
    print("Cipher Text:", ciphertext)

    # Finding the most likely shift value to decrypt
    best_shift = crack_caesar_shift(ciphertext)
    decryption = CaesarCipher(ciphertext)
    decryption.offset = best_shift
    print(f"\nPredicted Shift: {best_shift} (or {best_shift - 26})")
    print("Predicted Decryption:", decryption.decrypt())
