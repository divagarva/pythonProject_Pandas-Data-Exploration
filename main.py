import pandas as pd
import numpy as np

# Sample data for demonstration
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'James', 'Laura'],
    'Age': [28, 22, 35, 32, 30, 27],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance'],
    'Salary': [50000, 60000, 55000, 52000, 61000, 58000],
    'Years of Experience': [3, 2, 7, 6, 5, 4]
}

# Creating a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


# 1. Filtering data
def filter_data(df):
    print("\nFiltering employees with salary greater than 55000:")
    filtered_df = df[df['Salary'] > 55000]
    print(filtered_df)


# 2. Grouping and Aggregating
def group_and_aggregate(df):
    print("\nGrouping by Department and aggregating by mean Salary and Years of Experience:")
    grouped_df = df.groupby('Department').agg({
        'Salary': 'mean',
        'Years of Experience': 'mean'
    }).reset_index()
    print(grouped_df)


# 3. Handling Missing Values
def handle_missing_values():
    print("\nHandling missing values in dataset:")
    # Adding some missing values
    df_with_nan = df.copy()
    df_with_nan.loc[2, 'Salary'] = np.nan
    print("DataFrame with missing values:\n", df_with_nan)

    # Fill missing values with mean of Salary
    df_filled = df_with_nan.fillna(df_with_nan['Salary'].mean())
    print("\nDataFrame after filling missing Salary with mean:\n", df_filled)


# 4. Descriptive Statistics
def descriptive_statistics(df):
    print("\nDescriptive statistics for numeric columns:")
    stats = df.describe()
    print(stats)


# Main Function
if __name__ == "__main__":
    # Filtering
    filter_data(df)

    # Grouping and Aggregating
    group_and_aggregate(df)

    # Handling Missing Values
    handle_missing_values()

    # Descriptive Statistics
    descriptive_statistics(df)
