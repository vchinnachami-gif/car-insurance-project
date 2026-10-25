import pandas as pd

from src.preprocessing import preprocess
from src.eda import perform_eda
from src.train import train_models
from src.evaluate import evaluate_model

DATA_PATH = "data/Car Insurance Claim Prediction - Project.csv"


def main():

    print("=" * 60)
    print("CAR INSURANCE CLAIM PREDICTION")
    print("=" * 60)

    df = pd.read_csv(DATA_PATH)

    perform_eda(df)

    X_train, X_test, y_train, y_test, encoders = preprocess(df)

    best_model = train_models(
        X_train,
        X_test,
        y_train,
        y_test
    )

    evaluate_model(
        best_model,
        X_test,
        y_test
    )

    print("\nProject Completed Successfully!")


if __name__ == "__main__":
    main()