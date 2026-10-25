import pandas as pd


def generate_risk_report(model, X_test):

    probabilities = model.predict_proba(X_test)[:,1]

    report = X_test.copy()

    report["Risk Score"] = probabilities

    report["Risk Level"] = pd.cut(

        report["Risk Score"],

        bins=[0,0.33,0.66,1],

        labels=["Low","Medium","High"]

    )

    report.to_csv(

        "outputs/risk_scoring_report.csv",

        index=False

    )

    print("\nRisk scoring report saved.")