#!/usr/bin/env python3
"""
Download the Cleveland Heart Disease dataset from UCI ML Repository.
Saves as heart.csv with proper column headers and NaN for missing values.

No authentication required — UCI hosts this file publicly.

Source: UCI Machine Learning Repository, dataset ID 45
URL: https://archive.ics.uci.edu/dataset/45/heart+disease
Reference: Detrano R. et al. (1989). International application of a new
           probability algorithm for the diagnosis of coronary artery disease.
           American Journal of Cardiology 64:304-310.

Dataset: 303 patients from Cleveland Clinic Foundation
Features: 13 clinical features (age, sex, chest pain type, resting BP, etc.)
Target:   0 = no disease, 1-4 = disease present (severity)
Missing:  ca (4 values), thal (2 values) — marked as '?' in source, saved as NaN
"""

import sys
from io import StringIO
from pathlib import Path

import pandas as pd
import requests

# Public UCI data URL — no login or API key required
UCI_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "heart-disease/processed.cleveland.data"
)

COLUMNS = [
    "age",       # age in years
    "sex",       # 1 = male, 0 = female
    "cp",        # chest pain type (1-4)
    "trestbps",  # resting blood pressure (mm Hg)
    "chol",      # serum cholesterol (mg/dl)
    "fbs",       # fasting blood sugar > 120 mg/dl (1 = true)
    "restecg",   # resting ECG results (0-2)
    "thalach",   # maximum heart rate achieved
    "exang",     # exercise-induced angina (1 = yes)
    "oldpeak",   # ST depression induced by exercise
    "slope",     # slope of peak exercise ST segment (1-3)
    "ca",        # number of major vessels colored by fluoroscopy (0-3)
    "thal",      # thalassemia type (3=normal, 6=fixed defect, 7=reversable defect)
    "target",    # diagnosis: 0 = no disease, 1-4 = disease present
]

OUTPUT = Path(__file__).parent / "heart.csv"


def main():
    print("Downloading Cleveland Heart Disease dataset from UCI ML Repository...")
    print(f"Source: {UCI_URL}\n")

    try:
        resp = requests.get(UCI_URL, timeout=30)
        resp.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to UCI ML Repository.")
        print("Check your internet connection and try again.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"ERROR: HTTP {e.response.status_code} from UCI server.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("ERROR: Request timed out. Try again.")
        sys.exit(1)

    # Parse: comma-separated, '?' represents missing values
    df = pd.read_csv(
        StringIO(resp.text),
        header=None,
        names=COLUMNS,
        na_values="?",
    )

    df.to_csv(OUTPUT, index=False)

    print(f"Saved {len(df)} rows × {len(df.columns)} columns → {OUTPUT.resolve()}")
    print()
    print("Missing values:")
    missing = df.isnull().sum()
    for col, n in missing[missing > 0].items():
        print(f"  {col}: {n} missing")
    if missing.sum() == 0:
        print("  None")
    print()
    print("Target distribution:")
    for val, count in df["target"].value_counts().sort_index().items():
        label = "no disease" if val == 0 else f"disease (severity {val})"
        print(f"  {val} ({label}): {count} patients")
    print()
    print("For binary classification: target > 0 → disease present")
    print("  df['target'] = (df['target'] > 0).astype(int)")


if __name__ == "__main__":
    main()
