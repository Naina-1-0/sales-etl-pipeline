from logger import logger

def validate_data(df):
    """
    Validate the transformed dataset before loading it into the database.

    Checks:
    - Missing values
    - Duplicate rows
    - Negative sales
    - Negative quantities
    - Empty customer IDs

    Args:
        df (pd.DataFrame): Transformed dataset.

    Returns:
        bool: True if validation passes.

    Raises:
        ValueError: If critical validation checks fail.
    """

    validation_report = {
        "total_rows": len(df),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "negative_sales": int((df["sales"] < 0).sum()),
        "negative_quantity": int((df["quantity"] < 0).sum()),
        "empty_customer_ids": int((df["customer_id"] == "").sum())
    }

    logger.info("Validation Report")
    logger.info(validation_report)

    print("\nValidation Report")
    print("-" * 35)

    for key, value in validation_report.items():
        print(f"{key:<20}: {value}")

    # Fail validation if critical issues exist
    if (
        validation_report["missing_values"] > 0 or
        validation_report["duplicate_rows"] > 0 or
        validation_report["negative_sales"] > 0 or
        validation_report["negative_quantity"] > 0
    ):
        raise ValueError("❌ Data validation failed!")

    print("\n✅ Data validation passed.")

    logger.info("Data validation passed.")

    return True