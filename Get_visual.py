import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dir = 'E:\input\..'

#from subprocess import check_output
#print(check_output(["ls", dir]).decode("utf8"))

import glob

data = pd.DataFrame()
for f in glob.glob((dir+'*.csv')): # all files in the directory that matchs the criteria.
    data = pd.concat([data,pd.read_csv(f,low_memory=False)])

   # data.head()
