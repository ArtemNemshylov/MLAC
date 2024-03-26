import pandas as pd

df = pd.read_csv('datasets/banknote+authentication.zip', header=None)
df.columns = ['variance', 'skewness', 'curtosis', 'entropy', 'target']
X, y = df.iloc[:, :4], df['target']