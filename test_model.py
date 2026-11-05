import joblib
import numpy as np
import pytest

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


@pytest.fixture
def trained_model():
    iris = load_iris()

    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "iris_model.pkl")

    return model, X_test, y_test


def test_model_loading(trained_model):
    joblib.dump(trained_model[0], "iris_model.pkl")

    loaded_model = joblib.load("iris_model.pkl")

    assert loaded_model is not None


def test_model_accuracy(trained_model):
    model, X_test, y_test = trained_model

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    assert accuracy >= 0.90


def test_prediction_output(trained_model):
    model, _, _ = trained_model

    sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])

    prediction = model.predict(sample_input)

    assert len(prediction) == 1
    assert prediction[0] in [0, 1, 2]


def test_prediction_probability(trained_model):
    model, _, _ = trained_model

    sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])

    probabilities = model.predict_proba(sample_input)

    assert probabilities.shape == (1, 3)
    assert np.all(probabilities >= 0)
    assert np.all(probabilities <= 1)
    assert np.isclose(probabilities.sum(), 1.0)