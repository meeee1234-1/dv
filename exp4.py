import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(data.head())  # First 5 rows
print(data.info())  # Data types and non-null values
print(data.describe())  # Statistical summary for numerical columns
# Check for missing values
print(data.isnull().sum())
# Fill or drop missing values
data = data.fillna(0)  # Example: Filling NaN with 0
# data = data.dropna()  # Alternatively, drop rows with NaN
print(f"Number of duplicate rows: {data.duplicated().sum()}")
data = data.drop_duplicates()

sns.histplot(data['area'], kde=True)
plt.title(f'Distribution of {'area'}')
plt.show()


plt.figure(figsize=(8, 6))
plt.bar(df['parking'], df['stories'], color=['blue', 'orange'])
plt.title('Parking vs stories')
plt.xlabel('Parking')
plt.ylabel('Stories')
plt.show()


plt.figure(figsize=(8, 6))
plt.pie(df['parking'], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('parking')

plt.show()

s=a.head(10)
plt.figure(figsize=(8, 6))
plt.plot(s['Age'], s['Annual Income (k$)'],  color='green')
plt.title('House Price vs Number of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price')

plt.show()
