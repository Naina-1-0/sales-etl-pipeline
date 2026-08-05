import pandas as pd
from logger import logger
from config import RAW_DATA


def extract_data():
    """
    Read the raw sales CSV file and return it as a pandas DataFrame.

    Returns:
        pd.DataFrame | None:
            The extracted sales data if successful, otherwise None.
    """
    try:
        df = pd.read_csv(RAW_DATA, encoding="latin1")  #Adjust encoding if necessary

        logger.info("Data extracted successfully.")
        print("✅ Data extracted successfully!")

        return df

    except FileNotFoundError:
        logger.error(f"File not found: {RAW_DATA}")
        print(f"❌ File not found: {RAW_DATA}")
        return None

    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        print(f"❌ Error: {e}")
        return None