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
