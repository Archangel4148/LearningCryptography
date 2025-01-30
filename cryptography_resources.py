import pandas as pd

english_letter_frequency = {
    "E": 0.12702, "T": 0.09056, "A": 0.08167, "O": 0.07507, "I": 0.06966,
    "N": 0.06749, "S": 0.06327, "R": 0.06094, "H": 0.05987, "D": 0.04253,
    "L": 0.04025, "U": 0.02758, "C": 0.02702, "M": 0.02406, "F": 0.02228,
    "Y": 0.01994, "W": 0.01973, "G": 0.01586, "P": 0.01492, "B": 0.01492,
    "V": 0.00978, "K": 0.00772, "X": 0.00150, "Z": 0.00074, "J": 0.00153,
    "Q": 0.00095
}


class WordDataset:
    def __init__(self, csv_path: str):
        # Load the CSV file and extract the 'word' column as a list (in order of frequency)
        self.words = pd.read_csv(csv_path)['word'].tolist()

    def get_words(self):
        """Returns the list of words."""
        return self.words

    def get_word_count(self):
        """Returns the number of words in the dataset."""
        return len(self.words)
