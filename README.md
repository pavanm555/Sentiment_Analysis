## Sentiment_Analysis
Dataset: https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset
<br>
Download the required dataset from the above link
### Summary:
The given code performs sentiment analysis on a dataset of tweets. The goal is to classify tweets as either positive or negative based on their sentiment.

The first step is to import the necessary libraries such as numpy, pandas, matplotlib, seaborn, and nltk. The dataset is then imported using pandas read_csv function. The dataset contains 6 columns: sentiment, id, date, query, username, and text. The sentiment column contains the sentiment of the tweet (0 for negative and 4 for positive).

After importing the dataset, the code checks for any null values in the dataset using the isnull() function. Since there are no null values, the code renames the columns to a more readable format and drops the query column since it is not necessary for sentiment analysis.

The code then calculates the length of each tweet and visualizes the distribution of tweet lengths using a barplot and histogram. The mean length of tweets is calculated and a vertical line is drawn at the mean length in the histogram. The code also removes stopwords and punctuations from the tweets using the NLTK library.

The cleaned dataset is split into two dataframes: data_cleaned and data_eda. The data_cleaned dataframe contains the cleaned tweets and their corresponding sentiments. The data_eda dataframe contains the cleaned tweets split into individual words and their corresponding sentiments.

The code then generates word clouds for positive and negative tweets using the cleaned dataset. A word cloud is a visualization that shows the most frequent words in a dataset. The word clouds help to give an idea of the most common words in positive and negative tweets.

The cleaned dataset is then transformed using the TfidfVectorizer function from the sklearn library. The TfidfVectorizer function converts a collection of raw documents into a matrix of TF-IDF features. The transformed dataset is then split into a training set and a testing set using the train_test_split function.

Finally, the code trains a logistic regression model using the training set and predicts the sentiment of tweets in the testing set. The accuracy of the model is calculated using the accuracy_score function from the sklearn library.

