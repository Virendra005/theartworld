# 9.1''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords')
# print(stopwords.words('english'))
# import these modules


# 9.2'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize

# ps = PorterStemmer()

# # choose some words to be stemmed
# words = ["program", "programs", "programmer", "programming", "programmers"]

# for w in words:
# 	print(w, " : ", ps.stem(w))
# 9.3'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# from nltk import pos_tag
# from nltk import RegexpParser
# text ="learn php from guru99 and make study easy".split()
# print("After Split:",text)
# tokens_tag = pos_tag(text)
# print("After Token:",tokens_tag)
# patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
# chunker = RegexpParser(patterns)
# print("After Regex:",chunker)
# output = chunker.parse(tokens_tag)
# print("After Chunking",output)

# 10.1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# import nltk
# from nltk.stem import PorterStemmer
# nltk.download("punkt")

# ps = PorterStemmer()

# example_words = ["program","programming","programer","programs","programmed"]

# print("{0:20}{1:20}".format("--Word--","--Stem--"))
# for word in example_words:
#    print ("{0:20}{1:20}".format(word, ps.stem(word)))
#10.2''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Define sample texts and corresponding categories (modify as needed)
sentences = [
    ("I love this movie!", "positive"),
    ("The service was terrible.", "negative"),
    ("This product is highly recommended.", "positive"),
    ("I'm not feeling well today.", "negative"),
    ("This article is very informative.", "neutral"),
]

def preprocess_text(text):
    """Preprocesses text for classification."""
    # Tokenize
    words = nltk.word_tokenize(text.lower())
    # Remove stopwords
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]
    # Lemmatize
    lemma = nltk.WordNetLemmatizer()
    words = [lemma.lemmatize(word) for word in words]
    return words

# Extract features and labels
features = [(preprocess_text(sentence), label) for sentence, label in sentences]

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(features)

# Get user input sentence
user_sentence = input("Enter a sentence: ")

# Classify the sentence
predicted_label, probability = classifier.classify_prob(preprocess_text(user_sentence))

# Print the prediction with confidence score
print(f"The sentence is classified as: {predicted_label} (Confidence: {probability:.2f})")





