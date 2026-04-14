# Exercise 31: scikit-learn Basics

## Concept

scikit-learn is the standard library for classical ML in Python. It provides consistent APIs for training, prediction, and pipelines.

### Key Concepts

1. **train_test_split**: Divide data into training and test sets
2. **fit/predict**: Standard model interface
3. **Pipelines**: Chain preprocessing and models
4. **StandardScaler**: Normalize features

## AI/ML Application

- Building ML models for classification and regression
- Preprocessing and feature engineering
- Model evaluation and selection

## Code Examples

### Splitting data with `train_test_split`

```python
from sklearn.model_selection import train_test_split

X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
y = [0, 0, 1, 1, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print(f"Train: {len(X_train)}, Test: {len(X_test)}")  # Train: 4, Test: 2
```

### Training a model with the fit/predict pattern

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

X_train = np.array([[1, 2], [2, 3], [3, 1], [4, 3]])
y_train = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(X_train, y_train)              # Train the model

X_new = np.array([[2, 2], [3, 3]])
predictions = model.predict(X_new)       # Make predictions
print(predictions)                        # e.g., [0, 1]
```

### Building a pipeline with `StandardScaler` and a model

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Chain preprocessing and model into one object
pipeline = Pipeline([
    ("scaler", StandardScaler()),          # Step 1: normalize features
    ("classifier", LogisticRegression()),  # Step 2: classify
])

# Use the pipeline like a single model
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_new)
```

### Evaluating model accuracy

```python
from sklearn.metrics import accuracy_score

y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]
print(accuracy_score(y_true, y_pred))  # 0.8 (4 out of 5 correct)
```

## Your Task

1. `split_data(X, y, test_size, random_state)` - Split data using train_test_split
2. `train_logistic_regression(X_train, y_train)` - Train and return a LogisticRegression model
3. `make_predictions(model, X_test)` - Return predictions from model
4. `create_pipeline()` - Create pipeline with StandardScaler and LogisticRegression
5. `train_pipeline(pipeline, X_train, y_train)` - Fit pipeline and return it

## Testing
```bash
pytest exercises/31_sklearn_basics/test_sklearn.py -v
```
