from data import laptops
import pandas as pd


# Converts a dictionary into a dataframe and downloads an Excel file
# with a table containing all laptops and additional information about them


df = pd.DataFrame(laptops)

df.to_excel('laptops.xlsx', index=False)
