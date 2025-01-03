import duckdb as duck
import pandas as pd
con = duck.connect()
con.sql("SELECT 42").show()
results = con.sql("SELECT 42").pd.df()
print(results)
