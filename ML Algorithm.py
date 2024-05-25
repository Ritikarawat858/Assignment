import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/apple/Desktop/kepler_data.csv', skiprows=52)  # Skip first 52 rows

df_numeric = df.select_dtypes(include=['int', 'float'])

label_encoder = LabelEncoder()
df_numeric['koi_disposition'] = label_encoder.fit_transform(df['koi_disposition'])

label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))

# Separate features X and target variable y
X = df_numeric.drop(columns=['koi_disposition'])
y = df_numeric['koi_disposition']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = XGBClassifier()

# Train the model
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#  classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

#  confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, xticklabels=label_mapping.keys(), yticklabels=label_mapping.keys())
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

print("Numerical Label -> Categorical Value Mapping:")
for numerical_label, categorical_value in label_mapping.items():
    print(f"{numerical_label} -> {categorical_value}")
