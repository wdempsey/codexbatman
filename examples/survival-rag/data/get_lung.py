#!/usr/bin/env python3
"""
Download the NCCTG lung cancer dataset and save as lung.csv.

Source: Rdatasets mirror of the R survival::lung dataset
Reference: Loprinzi CL. et al. (1994) NCCTG Lung Cancer Study.
           Journal of Clinical Oncology 12:601-607.

Dataset: 228 advanced lung cancer patients, NCCTG study 1994
Outcome: Overall survival (time in days, status 1=censored 2=dead)
"""

import sys
from pathlib import Path

import pandas as pd
import requests


RDATASETS_URL = (
    "https://raw.githubusercontent.com/vincentarelbundock/"
    "Rdatasets/master/csv/survival/lung.csv"
)

OUTPUT_PATH = Path(__file__).parent / "lung.csv"


def download_lung():
    print("Downloading NCCTG lung cancer dataset from Rdatasets...")
    try:
        resp = requests.get(RDATASETS_URL, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Download failed: {e}")
        print("Try downloading manually from:")
        print(f"  {RDATASETS_URL}")
        sys.exit(1)

    df = pd.read_csv(pd.io.common.StringIO(resp.text))

    # Drop the unnamed row-index column R exports by default
    if df.columns[0] in ("", "Unnamed: 0", "rownames"):
        df = df.drop(columns=df.columns[0])

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} rows to {OUTPUT_PATH}")
    print(f"Columns: {list(df.columns)}")
    print(f"Missing values:\n{df.isnull().sum().to_string()}")


if __name__ == "__main__":
    download_lung()
