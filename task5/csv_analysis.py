import pandas as pd
import io
import matplotlib.pyplot as plt

# 1. CREATE & LOAD DATA
# Sample data (replace with pd.read_csv('your_file.csv') for a real file)
df = pd.read_csv('csv_data.csv')

# Display the first few rows of the DataFrame
print("--- Sales Data ---")
print(df.head())
print("\n" + "="*30 + "\n")


# 2. ANALYZE DATA
# Use groupby() to find the total sales for each product category
print("--- Analysis: Total Sales by Category ---")
sales_by_category = df.groupby('Category')['Sales'].sum()
print(sales_by_category)
print("\n" + "="*30 + "\n")


# 3. VISUALIZE RESULTS
print("--- Generating Chart ---")
# Create a bar chart to visualize the sales by category
sales_by_category.plot(
    kind='bar',
    title='Total Sales by Product Category',
    xlabel='Category',
    ylabel='Total Sales ($)',
    color=['skyblue', 'salmon', 'lightgreen'],
    rot=0, # Keeps category names horizontal
    figsize=(8, 5)
)

# Display the plot
plt.tight_layout()
plt.show()