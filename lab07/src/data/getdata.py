import pandas as pd

f=pd.read_csv("./bgg_dataset.csv", delimiter=';')
keep_col = ['Name', 'Year Published', 'Users Rated', 'Rating Average']
new_f = f[keep_col]
new_f['Year Published'] = pd.to_numeric(new_f['Year Published'],
                              errors='coerce').fillna(-1000000).astype('int')
new_f['Rating Average'] = new_f['Rating Average'].str.replace(',',
                              '.').astype('float')
new_f.to_csv("./games.csv", index=False)
