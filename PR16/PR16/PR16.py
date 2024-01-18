import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
text_path = "C:/carroll-alice.txt"
with open(text_path, "r", encoding="utf-8") as file:
    text = file.read()
words = word_tokenize(text)
word_count = len(words)
print(f"Total number of words in the text: {word_count}")
stop_words = set(stopwords.words("english"))
filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
most_common_words = Counter(filtered_words).most_common(10)
print("10 most common words:", most_common_words)
words, counts = zip(*most_common_words)
plt.bar(words, counts)
plt.title("10 Most Common Words (after processing)")
plt.xlabel("Words")
plt.ylabel("Count")
plt.show()