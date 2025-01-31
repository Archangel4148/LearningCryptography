from sympy import mod_inverse

from cryptography_resources import ALPHABET, Cipher


class AffineCipher(Cipher):
    def __init__(self, text: str):
        super().__init__(text)
        self.key = [0, 0]

    def encrypt(self, text=None):
        if text is None:
            text = self.text
        values = [(ALPHABET.index(c) * self.key[0] + self.key[1]) % 26 for c in text.upper() if c.isalpha()]
        ciphertext = "".join([ALPHABET[v] for v in values])
        return ciphertext

    def decrypt(self, text=None):
        if text is None:
            text = self.text
        a_inv = mod_inverse(self.key[0], 26)
        values = [(a_inv * (ALPHABET.index(c) - self.key[1])) % 26 for c in text.upper()]
        plaintext = "".join([ALPHABET[v] for v in values])
        return plaintext


if __name__ == '__main__':
    # Creating some basic plaintext and using a mapping to encode
    affine = AffineCipher("The quick brown fox jumps over the lazy dog")
    affine.key = [3, 1]

    print("Plain Text:", affine.text)
    ciphertext = affine.encrypt()
    print("Cipher Text:", ciphertext)

    # Decoding and printing output
    print("Decoded Text:", affine.decrypt(ciphertext))
