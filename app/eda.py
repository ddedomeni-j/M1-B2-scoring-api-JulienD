import pandas as pd

# Columns
NUMERIC_FEATURES: list[str] = [
    "loan_amnt",
    "int_rate",
    "installment",
    "annual_inc",
    "dti",
    "delinq_2yrs",
    "fico_range_low",
    "revol_util",
]

CATEGORICAL_FEATURES: list[str] = [
    "term",
    "grade",
    "home_ownership",
    "verification_status",
    "purpose",
    "emp_length",
]

def search_variables_range(df: pd.DataFrame):
    for col in NUMERIC_FEATURES:
        # Get the range of the variable
        min_value = df[col].min()
        max_value = df[col].max()
        print(f"range of {col}: {min_value} - {max_value}")

    return min_value, max_value

# Load the dataset
df1 = pd.read_csv("../../M1-B1-scoring-JulienD/M1-B1-scoring-JulienD/data/lending_club_holdout.csv")
df2 = pd.read_csv("../../M1-B1-scoring-JulienD/M1-B1-scoring-JulienD/data/lending_club_train.csv")

df = pd.concat([df1, df2], ignore_index=True)

search_variables_range(df)