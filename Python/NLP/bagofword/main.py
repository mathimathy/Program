from nh3 import clean
import numpy as np
import pandas as pd

data_imdb = pd.read_csv("imdb_labelled.txt", delimiter="\t", header=None)
data_imdb.columns = ["Review_text", "Review class"]

data_amazon = pd.read_csv("amazon_cells_labelled.txt", delimiter="\t", header=None)
data_amazon.columns = ["Review_text", "Review class"]

data_yelp = pd.read_csv("yelp_labelled.txt", delimiter="\t", header=None)
data_yelp.columns = ["Review_text", "Review class"]

data = pd.concat([data_imdb,data_amazon,data_yelp])
print(data)

import re
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def clean_text(df):
    all_reviews = list()
    lines = df['Review_text'].values.tolist()
    for text in lines:
        text = text.lower()
        pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|[?:%[0-9a-fA-F][0-9a-fA-F]])+')
        text = pattern.sub('', text)
        text = re.sub(r'[,."!@#$%^&*(){}?/;\'~:<>+=-]', "", text)
        tokens = word_tokenize(text)
        table = str.maketrans('','',string.punctuation)
        stripped=[w.translate(table) for w in tokens]
        words = [word for word in stripped if word.isalpha()]
        stop_word = set(stopwords.words("english"))
        stop_word.discard("not")
        PS = PorterStemmer()
        words = [PS.stem(w) for w in words if not w in stop_word]
        words = ' '.join(words)
        all_reviews.append(words)
    return all_reviews

all_reviews = clean_text(data)
print(all_reviews[0:20])

from sklearn.feature_extraction.text import CountVectorizer
CV = CountVectorizer(min_df=3)
x = CV.fit_transform(all_reviews).toarray()
y = data["Review class"].values
print(np.shape(x))
print(np.shape(y))

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score, f1_score, precision_score
print(accuracy_score(y_test,y_pred))
print(f1_score(y_test,y_pred))
print(precision_score(y_test,y_pred))