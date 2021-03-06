import numpy as np
import pandas as pd
from textblob import TextBlob

# Read in dataset
# df = pd.read_csv('tweet_data/model_test_data.csv')
df = pd.read_csv('merged_data.csv',
    dtype={'text': 'str'})
print(df.dtypes)
print(df.columns)
#print(df.shape)

# Define empty lists to append to
polarity = []
subjectivity = []
for i in range(0, df.shape[0]):
    blob = TextBlob(df.iloc[i, 5])
    polarity.append(blob.sentiment.polarity)
    subjectivity.append(blob.sentiment.subjectivity)

# Insert polarity and subjectivity as columns 
# Might have to adjust 11 and 12 (I did that since model_test_data had 11 columns)
# df.insert(6, 'Polarity', polarity)
# df.insert(7, 'Subjectivity', subjectivity)
df['Polarity'] = polarity
df['Subjectivity'] = subjectivity
#print(df.shape)

# Write to a csv
df.to_csv('merged_data_with_sentiment.csv',index=False)


