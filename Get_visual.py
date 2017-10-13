import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dir = "input"

#from subprocess import check_output
#print(check_output(["cd", dir]).decode("utf8"))

import glob


data = pd.DataFrame()

for f in glob.glob(dir+'\Indiegogo_2016-05-14.csv'):

    #print (f)

    data = pd.concat([data,pd.read_csv(f,low_memory=False)])

# all files in the directory that matchs the criteria.

# DATA CLEANING

useless_columns = ["id","url","category_url","igg_image_url","compressed_image_url","card_type",
                   "category_slug","partner_name","source_url","friend_team_members","friend_contributors"]
data = data.drop(useless_columns, axis = 1)

import re
def Remove_Non_Numeric (column) :
    return re.sub(r"\D","", column)

data.balance = data.balance.apply(lambda row : Remove_Non_Numeric(row))
data.collected_percentage = data.collected_percentage.apply (lambda row : Remove_Non_Numeric(row))



data.nearest_five_percent = data.nearest_five_percent.apply(lambda row : float(row)/100)
data.collected_percentage = data.collected_percentage.apply(lambda row : float(row)/100)



def Get_Days_Left(time):
    if  "hour" in time:
        return float(Remove_Non_Numeric(time))/24
    elif "day" in time:
        return float(Remove_Non_Numeric(time))
    else:
        return 0.0

data.amt_time_left = data.amt_time_left.apply(lambda row: Get_Days_Left(row))



def Clean_Funding(column):
    if  "true" in column.lower():
        return 1
    elif "false" in column.lower() :
        return -1
    else:
        return 0

data.in_forever_funding = data.in_forever_funding.apply(lambda row: Clean_Funding(str(row)))
data.in_forever_funding.unique()



# DATA VISUALIZATION

data.balance = data.balance.apply(lambda row: float(row))


def sb_BarPlot(data,label,measure):
    a4_dims = (11.0, 8.27)
    fig, ax = plt.subplots(figsize=a4_dims)
    plot = sns.barplot(y=label, x=measure,ax=ax, data=data,orient="vertical")

 sb_BarPlot(data,"category_name","balance")


print(data.head())
