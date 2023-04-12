# -*- coding: utf-8 -*-
"""Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AIHYOGkquUzdmUFpw7a5wZkF0-QZ09Qm

# Sentiment Analysis
By: M PAVAN SAI RAMAKRISHNA REDDY
> pavansaim555@gmail.com

##Summary:
The given code performs sentiment analysis on a dataset of tweets. The goal is to classify tweets as either positive or negative based on their sentiment.

The first step is to import the necessary libraries such as numpy, pandas, matplotlib, seaborn, and nltk. The dataset is then imported using pandas read_csv function. The dataset contains 6 columns: sentiment, id, date, query, username, and text. The sentiment column contains the sentiment of the tweet (0 for negative and 4 for positive).

After importing the dataset, the code checks for any null values in the dataset using the isnull() function. Since there are no null values, the code renames the columns to a more readable format and drops the query column since it is not necessary for sentiment analysis.

The code then calculates the length of each tweet and visualizes the distribution of tweet lengths using a barplot and histogram. The mean length of tweets is calculated and a vertical line is drawn at the mean length in the histogram. The code also removes stopwords and punctuations from the tweets using the NLTK library.

The cleaned dataset is split into two dataframes: data_cleaned and data_eda. The data_cleaned dataframe contains the cleaned tweets and their corresponding sentiments. The data_eda dataframe contains the cleaned tweets split into individual words and their corresponding sentiments.

The code then generates word clouds for positive and negative tweets using the cleaned dataset. A word cloud is a visualization that shows the most frequent words in a dataset. The word clouds help to give an idea of the most common words in positive and negative tweets.

The cleaned dataset is then transformed using the TfidfVectorizer function from the sklearn library. The TfidfVectorizer function converts a collection of raw documents into a matrix of TF-IDF features. The transformed dataset is then split into a training set and a testing set using the train_test_split function.

Finally, the code trains a logistic regression model using the training set and predicts the sentiment of tweets in the testing set. The accuracy of the model is calculated using the accuracy_score function from the sklearn library.
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

"""# Index
* Importing Libraries
* Reading csv file
* Simplify the data
* analysis
* dropping unnecessary columns
* EDA
* Word cloud positive data
* Word cloud negative data
* TFIDF for sentiment analysis
* Train Test Split
* LogisticRegression
* Accuracy Score: 85%

# Importing Libraries
"""

import matplotlib.pyplot as plt
import seaborn as sns
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
import warnings
warnings.filterwarnings('ignore')

"""# Reading csv file"""

df = pd.read_csv('/content/training.1600000.processed.noemoticon.csv',delimiter=',', encoding='ISO-8859-1')

df.head()

df.info()

df.isnull().sum()

"""# Simplify the data"""

df.columns=['sentiment','id','date','query','username','text']

df.head()

df.shape

"""# Analysis"""

df['sentiment'].value_counts()

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['sentiment'],kde=True)

sns.countplot(df['sentiment'])

df['query'].value_counts()

"""# dropping unnecessary columns"""

df=df.drop(columns=['query'])

df.head()

texts = df['text']

text_lens = [len(t.split()) for t in texts.values]
len_mean = np.mean(text_lens)

"""# EDA"""

fig, axes = plt.subplots(2,1, figsize=(10, 8))
axes[0].set_title('Distribution of tweets')
sns.barplot(text_lens, ax=axes[0])
sns.histplot(text_lens,bins=100, kde=True, ax=axes[1],color='blue')
axes[1].vlines(len_mean, 0, 5000, color = 'g')
plt.annotate("mean", xy=(len_mean, 5000), xytext=(len_mean-2, 5050),color='r')
plt.show()

import nltk
nltk.download('stopwords')
stuff_to_be_removed = list(stopwords.words('english'))+list(punctuation)
stemmer = LancasterStemmer()
corpus = df['text'].tolist()
print(len(corpus))
print(corpus[0])

import nltk
nltk.download('wordnet')
final_corpus = []
final_corpus_joined = []
for i in df.index:
    text = re.sub('[^a-zA-Z]', ' ', df['text'][i])
    text = text.lower()
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    text=re.sub("(\\d|\\W)+"," ",text)
    text = text.split()
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in text  if not word in stuff_to_be_removed] 
    text1 = " ".join(text)
    final_corpus.append(text)
    final_corpus_joined.append(text1)

data_cleaned = pd.DataFrame()
data_cleaned["text"] = final_corpus_joined
data_cleaned["sentiment"] = df["sentiment"].values

data_eda = pd.DataFrame()
data_eda['text'] = final_corpus
data_eda['sentiment'] = df['sentiment'].values
data_eda.head()

positive = data_eda[data_eda['sentiment'] == 4]
positive_list = positive['text'].tolist()
negative = data_eda[data_eda['sentiment'] == 0]
negative_list = negative['text'].tolist()

positive_all = " ".join([word for sent in positive_list for word in sent ])
negative_all = " ".join([word for sent in negative_list for word in sent ])

"""# Word cloud positive data"""

from wordcloud import WordCloud
WordCloud()
wordcloud = WordCloud(width=1000,
                      height=500,
                      background_color='skyblue',
                      max_words = 90).generate(positive_all)

plt.figure(figsize=(30,20))
plt.imshow(wordcloud)
plt.title("Positive")
plt.show()

"""# Word cloud negative data"""

from wordcloud import WordCloud
WordCloud()
wordcloud = WordCloud(width=1000,
                      height=500,
                      background_color='skyblue',
                      max_words = 90).generate(negative_all)

plt.figure(figsize=(30,20))
plt.imshow(wordcloud)
plt.title("negative")
plt.show()

"""# TFIDF for sentiment analysis"""

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
xt = tfidf.fit_transform(data_cleaned['text'])
y = data_cleaned['sentiment']

"""# Train Test Split"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(xt, 
                                                    y, 
                                                    test_size=0.33, 
                                                    random_state=42,
                                                    stratify = y)

"""# LogisticRegression"""

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train,y_train)

"""# Accuracy Score: 85% """

y_train_pred = lr.predict(X_train)
y_test_pred = lr.predict(X_test)
accuracy_score(y_train,y_train_pred)*100

"""                               
                                                           <-- THE END -->


"""