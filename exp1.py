import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('Housing.csv')
df=data.head(10)
# Display the dataset
print("Dataset:")
print(data)


#Bar Chart

data['stories'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Number of Houses by Number of Stories')
plt.xlabel('Stories')
plt.ylabel('Number of Houses')
plt.show()


#Line Chart

data.groupby('stories')['price'].mean().sort_index().plot(kind='line', color='green')
plt.title('Average House Price by Number of Stories')
plt.xlabel('Stories')
plt.ylabel('Average Price')
plt.show()

#Pie Chart

data['mainroad'].value_counts().plot(kind='pie', autopct='%1.1f%%',  colors=['skyblue','red'])
plt.title('Main Road Access Distribution')
plt.ylabel('')  # Hide y-label for pie chart
plt.show()

