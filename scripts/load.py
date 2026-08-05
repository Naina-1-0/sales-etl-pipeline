from sqlalchemy import create_engine
from logger import logger
from config import DATABASE_PATH, TABLE_NAME


def load_data(df):
    """
    Load the transformed data into the SQLite database.

    Args:
        df (pd.DataFrame): Cleaned sales dataset.

    Returns:
        None
    """

    engine = create_engine(f"sqlite:///{DATABASE_PATH}")

    df.to_sql(
        TABLE_NAME,
        con=engine,
        if_exists="replace",
        index=False
    )

    logger.info("Data loaded into SQLite database.")
    print("✅ Data loaded into SQLite database.")