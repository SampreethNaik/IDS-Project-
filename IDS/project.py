import pandas as pd
import numpy as np

youtube = pd.read_excel('dataScience.xlsx')

category = youtube.select_dtypes('object')
cdf = pd.DataFrame(category)

df = pd.DataFrame(youtube)

#numeric=youtube.select_dtypes(np.number).head()


mlikes = df["likes"].mean()
mdislikes = df["dislikes"].mean()
mcomments = df["comment_total"].mean()
mcategory = df["category_id"].mean()
mviews = df["views"].mean()

values = {'likes': mlikes, 'views': mviews, 'dislikes' : mdislikes, 'category_id' : mcategory, 'comment_total' : mcomments}
df.fillna(value = values, inplace= True)

#print(df.loc[:20, ['likes', 'dislikes', 'views', 'comment_total', 'category_id']])
#print(df.dislikes)
#print(df.comment_total)
#print(df.views)
#print(df.category_id)

cdf.fillna(method='ffill', inplace=True)
print(cdf)



