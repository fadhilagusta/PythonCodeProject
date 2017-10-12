import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob, re

data = pd.DataFrame()
for f in glob.glob('E:\input\Indiegogo_2016-05-14.csv'):
    data = pd.concat([data,pd.read_csv(f,low_memory=False)])

data['balance'] = data ['balance'].map(lambda x: float(re.sub('[a-z\$\?,]','',str(x))))
data = data.groupby(by=['category_name'],as_index=False)['balance'].sum().sort_values(['balance'], ascending=[False])[:30].plot(kind='barh', x='category_name', y='balance')




