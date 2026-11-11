
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, balanced_accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Loading data
data = pd.read_csv("creditcard.csv")

features = data.drop("Class", axis=1)
labels = data["Class"]

# Separating training data from test data
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.2, stratify=labels, random_state=1
)

# Standard scaling
scaler = StandardScaler()

train_features_scaled = train_features.copy()
test_features_scaled = test_features.copy()

# Scaling only Time and Amount
train_features_scaled[["Time", "Amount"]] = scaler.fit_transform(
    train_features[["Time", "Amount"]]
)

test_features_scaled[["Time", "Amount"]] = scaler.transform(
    test_features[["Time", "Amount"]]
)

# Model without class weights
print("Model without class weights")

baseline_model = LogisticRegression(max_iter=1000, random_state=1)
baseline_model.fit(train_features_scaled, train_labels)

baseline_predictions = baseline_model.predict(test_features_scaled)

print("Accuracy:", round(100 * accuracy_score(test_labels, baseline_predictions), 2), "%")
print("Recall:", round(100 * recall_score(test_labels, baseline_predictions), 2), "%")
print("Balanced accuracy:", round(100 * balanced_accuracy_score(test_labels, baseline_predictions), 2), "%")

# Model with balanced class weights
print("\nModel with balanced class weights")

balanced_model = LogisticRegression(
    class_weight="balanced", max_iter=1000, random_state=42
)

balanced_model.fit(train_features_scaled, train_labels)

balanced_predictions = balanced_model.predict(test_features_scaled)

print("Accuracy:", round(100 * accuracy_score(test_labels, balanced_predictions), 2), "%")
print("Recall:", round(100 * recall_score(test_labels, balanced_predictions), 2), "%")
print("Balanced accuracy:", round(100 * balanced_accuracy_score(test_labels, balanced_predictions), 2), "%")
