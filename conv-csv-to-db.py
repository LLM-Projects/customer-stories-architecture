import sqlite3
import pandas as pd

data = pd.read_csv('./output.csv')

# Join the elements of the list when splitting the column names
data.columns = data.columns.str.split().map(lambda x: '_'.join(x))

connection = sqlite3.connect("output.db")

# Write the DataFrame to the SQLite database
data.to_sql("scraped_data", connection, if_exists="replace", index=False)
