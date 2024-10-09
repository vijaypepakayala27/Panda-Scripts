import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
    'Age': [25, np.nan, 30, 40, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', np.nan, 'Miami']
}

df = pd.DataFrame(data)

print("Original DataFrame with missing values:")
print(df)

# Method 1: Filling missing values with a placeholder
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'City': 'Unknown'})
print("\nDataFrame after filling missing values:")
print(df_filled)

# Method 2: Dropping rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)
