#Histogram
plt.figure(figsize=(8,6))
plt.hist(data['price'], bins=20, color='orange', edgecolor='black')
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Number of Houses')
plt.show()

# Scatter Plot
plt.figure(figsize=(8,6))
plt.scatter(data['parking'], data['price'], color='purple')
plt.title('Price vs Parking')
plt.xlabel('Parking')
plt.ylabel('Price')
plt.show()

import seaborn as sns


# Correlation Heatmap
plt.figure(figsize=(8,6))
corr = data[['price', 'stories', 'bedrooms', 'bathrooms']].corr()  # use correct column names
sns.heatmap(corr, annot=True, cmap='coolwarm', )
plt.title('Correlation Heatmap')
plt.show()


# 4. Box Plot: Engagement Rate by Platform
plt.figure(figsize=(8, 6))
sns.boxplot(x='stories', y='parking', data=df)
plt.title('Stories VS Parking')
plt.xlabel('Stories')
plt.ylabel('Parking')
plt.show()
