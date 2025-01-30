from cryptography_resources import WordDataset

word_dataset = WordDataset("word_freq.csv")

for i, word in enumerate(word_dataset.words[:100]):
    print(f"{i+1}. {word}")