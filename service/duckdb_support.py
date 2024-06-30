from typing import IO

import duckdb
import pandas as pd
from loguru import logger as log
class DuckDBSupport:
    def upload_csv(self, db_name: str, table_name: str, input_csv: IO):
        db_path = f"{db_name}.duckdb"
        df = pd.read_csv(input_csv)
        conn = duckdb.connect(db_path)
        conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
        conn.close()
        log.info("Upload csv success.")