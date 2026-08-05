import pandas as pd
from logger import logger

def transform_data(df):
    """
    Clean and transform the extracted sales data.

    Operations performed:
    - Rename columns to snake_case
    - Convert date columns to datetime
    - Remove duplicate rows
    - Create the profit_margin column

    Args:
        df (pd.DataFrame): Raw sales dataset.

    Returns:
        pd.DataFrame: Transformed dataset.
    """
    # Creating a copy to avoid modifying the original DataFrame
    df = df.copy()

    # 1. Rename columns
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # 2. Convert dates
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    # 3. Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    logger.info(f"Removed {before-after} duplicate rows.")
    print(f"Removed {before - after} duplicate rows.")

    # 4. Create a new column
    df["profit_margin"] = (df["profit"] / df["sales"]) * 100

    # 5. Round values
    df["profit_margin"] = df["profit_margin"].round(2)

    
    logger.info("Transformation completed.")
    print("✅ Transformation completed!")

    
    return df