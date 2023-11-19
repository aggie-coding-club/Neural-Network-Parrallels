print("Hello World")
print("Hi there friends")
#embedding code below
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample text data
corpus = [
    "This is the first sample text.",
    "This document is the second sample.",
    "And this is the third one.",
    "etc.",
]

# Create a TfidfVectorizer instance
vectorizer = TfidfVectorizer()

# Fit and transform the corpus to obtain TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(corpus)

# Convert the TF-IDF matrix to a dense array
tfidf_vectors = tfidf_matrix.toarray()

# Get the feature (word) names corresponding to the columns
feature_names = vectorizer.get_feature_names_out()

# Create a DataFrame for readability (not needed)
import pandas as pd
tfidf_df = pd.DataFrame(data=tfidf_vectors, columns=feature_names)

# Display the TF-IDF vectors
print(tfidf_df)
