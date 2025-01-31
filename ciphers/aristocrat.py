from cryptography_resources import ALPHABET, Cipher


class AristocratCipher(Cipher):
    def __init__(self, text: str):
        super().__init__(text)
        self.mapping = ""

    def encrypt(self, text=None):
        if text is None:
            text = self.text
        ciphertext = ""
        for c in text.upper():
            if c.isalpha():
                ciphertext += self.mapping[ALPHABET.index(c)]
            else:
                ciphertext += c
        return ciphertext

    def decrypt(self, text=None):
        if text is None:
            text = self.text
        plaintext = ""
        for c in text.upper():
            if c.isalpha():
                plaintext += ALPHABET[self.mapping.index(c)]
            else:
                plaintext += c
        return plaintext


if __name__ == '__main__':
    # Creating some basic plaintext and using a mapping to encode
    aristocrat = AristocratCipher("The quick brown fox jumps over the lazy dog")
    aristocrat.mapping = "QWERTYUIOPASDFGHJKLZXCVBNM"

    print("Plain Text:", aristocrat.text)
    ciphertext = aristocrat.encrypt()
    print("Cipher Text:", ciphertext)

    # Decoding and printing output
    print("Decoded Text:", aristocrat.decrypt(ciphertext))
