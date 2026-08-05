from extract import extract_data
from transform import transform_data
from load import load_data
from validator import validate_data
from visualize import generate_visualizations
from logger import logger

def main():
    """
    Run the complete ETL pipeline.

    Workflow:
    1. Extract data
    2. Transform data
    3. Validate data
    4. Load data into SQLite
    5. Generate visualizations
    """
    # Extract
    df = extract_data()

    if df is None:
        return

    # Transform
    transformed_df = transform_data(df)

    # validate data
    validate_data(transformed_df)

    # Save the transformed data to a CSV file for record-keeping
    transformed_df.to_csv(
    "data/processed/cleaned_sales.csv",
    index=False
    )

    # Load
    load_data(transformed_df)

    # Visualize
    generate_visualizations()

    logger.info("ETL pipeline completed successfully.")
    print("\n🎉 ETL Pipeline completed successfully!")



if __name__ == "__main__":
    main()