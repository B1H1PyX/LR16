import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string
input_file_path = "C:/PhotoStory.txt"
output_file_path = "C:/PhotoStory2.txt"
with open(input_file_path, "r", encoding="utf-8") as file:
    text = file.read()
words = word_tokenize(text)
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
stemmed_words = [stemmer.stem(word) for word in words]
stop_words = set(stopwords.words("english"))
filtered_words = [word.lower() for word in lemmatized_words if word.isalpha() and word.lower() not in stop_words]
filtered_words = [word for word in filtered_words if word not in string.punctuation]
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(" ".join(filtered_words))
print('Success')