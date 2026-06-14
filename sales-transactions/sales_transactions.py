import pandas as pd

# reading csv file 
df = pd.read_csv("sales_transactions.csv")

# display data
pd.set_option("display.max_columns", None)
print(df.head())

# understanding the data statistics.
print("\nInformation: ")
df.info()
print(df.describe())
print(f"\nTotal no. of null values: \n{df.isnull().sum()}")

# checking the exact column names
print("column names: ")
print(df.columns.to_list())

# converting date column to datetime
df["date"] = pd.to_datetime(df["date"])

# inserting quater and month column
df.insert(1, "quarter", df["date"].dt.quarter)
df.insert(2, "month", df["date"].dt.month)

# total Revenue by Category
print("\nRevenue by category: ")
print(df.groupby("category")["total_amount"].sum())

# total revenue per product
print("\nTotal revenue per product: ")
print(df.groupby("product")["total_amount"].sum().sort_values(ascending=False))

# total quantity sold per region
print("\nTotal quantity sold per region: ")
print(df.groupby("region")["quantity"].sum())

# top sales person by total revenue
print("\nTop sales person by total revenue: ")
print(df.groupby("salesperson")["total_amount"].sum().sort_values(ascending=False))

# Top Salesperson by Quantity
print("\nTop sales person by total quantity: ")
print(df.groupby("salesperson")["quantity"].sum().sort_values(ascending=False))

# Average Order Value
print(f"Average order value: {df["total_amount"].mean()}")

# Monthly Revenue Trend
print(f"Monthly revenue trend: ")
print(df.groupby("month")["total_amount"].sum())

# best selling month using groupby on month
print("\nbest selling month: ")
print(df.groupby("month")["total_amount"].sum().sort_values(ascending=False))

# Filter only Electronics category and find its % of total revenue
total_revenue = df["total_amount"].sum()
electronics_revenue = df.loc[df["category"] == "Electronics","total_amount"].sum()
electronics_revenue_percent = ( electronics_revenue / total_revenue ) * 100
print(f"\nFilter only Electronics category and find its % of total revenue: {electronics_revenue_percent.round(2)}")