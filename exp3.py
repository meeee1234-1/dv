import seaborn as sns
from wordcloud import WordCloud
a=pd.read_csv('Customers (1).csv')
print(a)

plt.figure(figsize=(8, 6))
a['Genre'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Area by No. of house')
plt.xlabel('Area')
plt.ylabel('No of house')
plt.show()


plt.figure(figsize=(8, 6))
df['stories'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('No of stories')
plt.ylabel('')
plt.show()


d=pd.read_csv('shop.csv')
print(d)


wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(d['product']))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud of Platforms')
plt.show()