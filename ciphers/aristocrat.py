from cryptography_resources import ALPHABET, Cipher, english_letter_frequency


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


def crack_mapping(ciphertext: str):
    ciphertext = ''.join([c.upper() for c in ciphertext if c.isalpha()])
    # Count the frequency of characters in the ciphertext
    cipher_counts = Counter(ciphertext)

    # Sort the characters by frequency
    cipher_frequency = ''.join([item[0] for item in cipher_counts.most_common()])

    # Create a mapping based on frequency
    mapping = {cipher_frequency[i]: list(english_letter_frequency)[i] for i in range(len(cipher_frequency))}

    # Now we use this mapping to decrypt the ciphertext
    decrypted_text = ''.join([mapping.get(c, c) for c in ciphertext])

    # Return the mapping and the decoded text (for testing purposes)
    return decrypted_text, mapping


if __name__ == '__main__':
    # Creating some basic plaintext and using a mapping to encode
    aristocrat = AristocratCipher("The quick brown fox jumps over the lazy dog")
    aristocrat.mapping = "QWERTYUIOPASDFGHJKLZXCVBNM"

    print("Plain Text:", aristocrat.text)
    ciphertext = aristocrat.encrypt()
    print("Cipher Text:", ciphertext)

    decryption, mapping = crack_mapping(ciphertext)
    # Printing cracked output
    print(mapping, "\n", decryption)

    # Decoding and printing output
    # print("Decoded Text:", aristocrat.decrypt(ciphertext))
