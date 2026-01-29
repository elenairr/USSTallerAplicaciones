import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
from ucimlrepo import fetch_ucirepo

# Sklearn imports
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve

# Imblearn
from imblearn.over_sampling import SMOTE

# Configuration
OUTPUT_DIR = "streamlit_app"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
MODEL_PATH = os.path.join(OUTPUT_DIR, "model.joblib")
PREPROCESSOR_PATH = os.path.join(OUTPUT_DIR, "preprocessor.joblib")
FEATURES_PATH = os.path.join(OUTPUT_DIR, "features.joblib")

if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

print("--- 1. Loading Data ---")
# Fetch dataset from UCI
try:
    bank_marketing = fetch_ucirepo(id=222) 
    X = bank_marketing.data.features 
    y = bank_marketing.data.targets['y']
except Exception as e:
    print(f"Error fetching data: {e}")
    # Fallback if fetch fails (assuming local data might exist, but for now we rely on fetch)
    exit(1)

print(f"Data loaded: {X.shape}")

# Clean duplicates
df = pd.concat([X, y], axis=1).drop_duplicates()
X = df.drop('y', axis=1)
y = df['y'].apply(lambda x: 1 if x == 'yes' else 0)

print(f"Data after cleaning: {X.shape}")

# Split Train/Test
X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print("--- 2. Preprocessing ---")
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Fit and Transform Train
X_train = preprocessor.fit_transform(X_train_raw)
X_test = preprocessor.transform(X_test_raw)

# Get feature names
feature_names = (numeric_features + 
                 preprocessor.named_transformers_['cat']
                 .named_steps['onehot']
                 .get_feature_names_out(categorical_features).tolist())

print("--- 3. Handling Imbalance (SMOTE) ---")
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

print(f"Train shape after SMOTE: {X_train_smote.shape}")

print("--- 4. Training Model (Random Forest) ---")
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train_smote, y_train_smote)

print("--- 5. Evaluation ---")
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, y_prob)
print(f"AUC: {auc:.4f}")
print(classification_report(y_test, y_pred))

# Save Confusion Matrix
plt.figure(figsize=(6, 5))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix - Random Forest (App)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig(os.path.join(IMAGES_DIR, 'confusion_matrix.png'))
plt.close()

# Save ROC Curve
plt.figure(figsize=(8, 6))
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr, label=f"Random Forest (AUC = {auc:.3f})")
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig(os.path.join(IMAGES_DIR, 'roc_curve.png'))
plt.close()

print("--- 6. Serialization ---")
# Save Model
joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")

# Save Preprocessor
joblib.dump(preprocessor, PREPROCESSOR_PATH)
print(f"Preprocessor saved to {PREPROCESSOR_PATH}")

# Save Feature Names & Metadata
metadata = {
    "feature_names": feature_names,
    "numeric_features": numeric_features,
    "categorical_features": categorical_features,
    "auc": auc
}
joblib.dump(metadata, FEATURES_PATH)
print(f"Metadata saved to {FEATURES_PATH}")

print("Done.")
