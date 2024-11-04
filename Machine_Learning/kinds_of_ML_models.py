from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def logistic_regression(X_train, X_val, y_train, y_val):
    # Initialize and fit the model
    logreg = LogisticRegression(max_iter=10000, random_state=42)
    logreg.fit(X_train, y_train)

    # Predict on the validation set
    y_pred = logreg.predict(X_val)

    # Evaluate the model
    accuracy = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)

    print("Logistic Regression Classification Report:\n", report)

    return logreg, accuracy

def svm_model(X_train, X_val, y_train, y_val):
    # Initialize and fit the SVM model
    svm = SVC(random_state=42)
    svm.fit(X_train, y_train)

    # Predict on the validation set
    y_pred = svm.predict(X_val)

    # Evaluate the model
    accuracy = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)

    print("SVM Classification Report:\n", report)

    return svm, accuracy

def random_forest_model(X_train, X_val, y_train, y_val):
    # Initialize and fit the Random Forest model
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)

    # Predict on the validation set
    y_pred = rf.predict(X_val)

    # Evaluate the model
    accuracy = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)

    print("Random Forest Classification Report:\n", report)

    return rf, accuracy

def naive_bayes_model(X_train, X_val, y_train, y_val):
    # Initialize the Naive Bayes model
    gnb = GaussianNB()

    # Fit the model on the training data
    gnb.fit(X_train, y_train)

    # Predict on the validation set
    y_pred = gnb.predict(X_val)

    # Evaluate the model
    accuracy = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)

    print("Naive Bayes Classification Report:\n", report)

    return gnb, accuracy

def return_model(model_name):
    if model_name == "logistic_regression":
        return logistic_regression
    elif model_name == "svm_model":
        return svm_model
    elif model_name == "random_forest_model":
        return random_forest_model
    elif model_name == "naive_bayes_model":
        return naive_bayes_model
    else:
        return