import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load your data 
df = pd.read_csv('average_happiness_rank.csv')

print(df.columns)


# Calculate weight so lower ranks appear larger
max_rank = df['Rank'].max()
df['Weight'] = max_rank + 1 - df['Rank']

#Create {Country: Weight} dictionary
rank_dict = dict(zip(df['Country'], df['Weight']))

#Generate the word cloud
wordcloud = WordCloud(
    width=1000,
    height=600,
    background_color='white',
    colormap='plasma'  
).generate_from_frequencies(rank_dict)

#Save the word cloud image
wordcloud.to_file("happiness_wordcloud.png")

# Show the word cloud
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
