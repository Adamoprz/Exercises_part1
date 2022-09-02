text = "The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains all of the letters of the English alphabet"

#words = text.split(" ")
#lista przechowująca długości kolejnych wyrazów z pominięciem słowa “the”:

length_of_words = list(map(lambda x: len(x), filter(lambda x: x.lower() != 'the', text.split(" "))))

print(length_of_words)