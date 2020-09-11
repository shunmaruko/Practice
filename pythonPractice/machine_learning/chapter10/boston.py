from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

boston = load_boston()
print(boston.feature_names)
df = pd.DataFrame(boston.data, columns=boston.feature_names)
cols = ['LSTAT', 'INDUS', 'NOX', 'RM']
print(df.head())
print(df['LSTAT'])
print(df[cols].values.T)
sns.pairplot(df[cols], height=1.5)
plt.tight_layout()
plt.show()
plt.clf()

cm = np.corrcoef(df[cols].values.T)
hm = sns.heatmap(cm,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size':15},
                 yticklabels=cols,
                 xticklabels=cols)
plt.show()

