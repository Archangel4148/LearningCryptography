from cryptography_resources import ALPHABET, Cipher


class AtbashCipher(Cipher):
    def __init__(self, text: str):
        super().__init__(text)
        self.reverse_alphabet = ALPHABET[::-1]

    def encrypt(self, text=None):
        ciphertext = ""
        if text is None:
            text = self.text
        for c in text.upper():
            if c.isalpha():
                ciphertext += self.reverse_alphabet[ord(c) - ord("A")]
            else:
                ciphertext += c
        return ciphertext

    def decrypt(self, text=None):
        if text is None:
            return self.encrypt(self.text)
        else:
            return self.encrypt(text)


if __name__ == '__main__':
    # Creating some basic plaintext to encode
    atbash = AtbashCipher("Hello, my name is Jeff!")
    print("Plain Text:", atbash.text)
    print("Cipher Text:", atbash.encrypt())
