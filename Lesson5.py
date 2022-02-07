import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

text = "Welcome! In this bit of code, we will describe tokenization. Depending on what we want to tokenize, we use different tokenizers."
print('sent', sent_tokenize(text))

from nltk.tokenize import word_tokenize
print('word', word_tokenize(text))

#We can import various tokenizers from the nltk.tokenize sub-package:

from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
s0 = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"
print('without params', tknzr.tokenize(s0))

#Examples using strip_handles and reduce_len parameters:

tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
s1 = '@remy: This is waaaaayyyy too much for you!!!!!!'
print('with params', tknzr.tokenize(s1))

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
word_list = ['Oh', 'I’m', 'not', 'too', 'sure', 'about', 'that']

#[word for word in word_list if word not in english_stops]
for word in word_list:
    if word not in english_stops:
        print(word)


from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()

print("bakeries :", lemmatizer.lemmatize("bakeries"))
print("expectations :", lemmatizer.lemmatize("expectations"))

#Some terms we need to specify how they are being used.

#Here ‘a’ denotes adjective in "pos"[ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v']

print("better :", lemmatizer.lemmatize("better", pos="a"))

#We can create frequency distributions of our words using FreqDist

text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood? If a woodchuck could chuck any amount of wood, how much wood would a woodchuck chuck?"
words = nltk.word_tokenize(text)
words = [word for word in words if word not in english_stops]

freq_dist = nltk.FreqDist(words)

freq_dist.most_common(3)

freq_dist.tabulate(3)

freq_dist['chuck']
lower_fd = nltk.FreqDist([w.lower() for w in freq_dist])

nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sia.polarity_scores("Wow, NLTK is really powerful!")

