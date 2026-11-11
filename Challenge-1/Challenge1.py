# Model regresji logistycznej bez wag klas osiagnie wysokie accuracy lecz niski recall class_weight='balanced' powinno podniesc recall
# kaggle.com/datasets/mlg-ulb/creditcardfraud 


# biblioteki
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import balanced_accuracy_score


#
# wczytywanie danych
df = pd.read_csv("creditcard.csv")
X = df.drop("Class", axis=1)
y = df["Class"]

# podzial na zbior treninigowy i testowy
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=1
)
#print(f"\nwiersze treningowe = {len(X_train)}")
#print(f"wiersze testowe = {len(X_test)}")

# skalujemy dane
scaler = StandardScaler()

X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

# Dajemy scaler tylko na zbiorze treningowym
X_train_scaled[["Time", "Amount"]] = scaler.fit_transform(
    X_train[["Time", "Amount"]]
)
# samo transform na tescie
X_test_scaled[["Time", "Amount"]] = scaler.transform(X_test[["Time", "Amount"]])

#
#
print("test 1 model bez wag")

model_baseline = LogisticRegression(max_iter=1000, random_state=1)
model_baseline.fit(X_train_scaled, y_train)

y_pred_baseline = model_baseline.predict(X_test_scaled)
print(classification_report(y_test, y_pred_baseline, digits=4))
print(
    "Balanced Accuracy:", balanced_accuracy_score(y_test, y_pred_baseline)
)  # dla testu 1


print("test 2 model z class_weight='balanced'")


model_balanced = LogisticRegression(
    class_weight="balanced", max_iter=1000, random_state=42
)
model_balanced.fit(X_train_scaled, y_train)


y_pred_balanced = model_balanced.predict(X_test_scaled)
print(classification_report(y_test, y_pred_balanced, digits=4))
print(
    "Balanced Accuracy:", balanced_accuracy_score(y_test, y_pred_balanced)
)  # dla testu 2
