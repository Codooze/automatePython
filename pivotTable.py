#? Project #3 - Automate Excel Report - Create a Pivot Table with Python
import pandas as pd


df = pd.read_excel("supermarket_sales.xlsx")

df = df[["Gender","Product line", "Total"]]
print(df.head())

pivot_table = df.pivot_table(index="Gender", columns="Product line", values="Total", aggfunc="sum").to_excel("pivot.xlsx")

#? Automate Excel Report - Add a Bar Chart