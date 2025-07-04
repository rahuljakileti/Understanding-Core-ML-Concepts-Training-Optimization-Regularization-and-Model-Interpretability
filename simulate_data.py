import pandas as pd
import numpy as np

def create_loan_dataset():
    np.random.seed(42)

    n = 200
    df = pd.DataFrame({
        'age': np.random.randint(21, 60, n),
        'annual_income': np.random.randint(25000, 120000, n),
        'loan_amount': np.random.randint(1000, 25000, n),
        'loan_term_months': np.random.choice([12, 24, 36, 60], n),
        'credit_score': np.random.randint(300, 850, n),
        'employment_type': np.random.choice(['salaried', 'self-employed', 'unemployed'], n),
        'owns_house': np.random.choice([0, 1], n),
        'defaulted': np.random.choice([0, 1], n, p=[0.8, 0.2])  # assume 20% default rate
    })

    df.to_csv('uploads/loan_data.csv', index=False)
    print("✅ Loan dataset saved to /uploads/loan_data.csv")

create_loan_dataset()
