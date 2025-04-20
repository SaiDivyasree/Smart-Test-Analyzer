import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

dataset_path = os.path.join("dataset", "errors_dataset.csv")
data = pd.read_csv(dataset_path)

X = data['error_log_text']
y = data['root_cause']

pipe = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('model', MultinomialNB())
])

pipe.fit(X, y)
joblib.dump(pipe, "failure_classifier.pkl")
print("✅ Model trained and saved successfully.")
