#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import data
ncaa_df = pd.read_csv("data/ncaa_df.csv")

#set fig size
plt.rcParams['figure.figsize'] = [15, 10]

#Bonus EDA

#Among schools that had an APR in both 2004 and 2019, took average APR
ncaa_2 = ncaa_df.dropna(subset = ["APR_RATE_2004_1000","APR_RATE_2019_1000"])
ncaa_2["APR_change"] = ncaa_2["APR_RATE_2019_1000"] - ncaa_2["APR_RATE_2004_1000"]
ncaa_2.sort_values(by="APR_change", ascending = False)
APR_change_top = ncaa_2.groupby("SCL_NAME")["APR_change"].mean().sort_values(ascending = False)[0:5]
APR_change_bottom = ncaa_2.groupby("SCL_NAME")["APR_change"].mean().sort_values(ascending = False)[-5:]
APR_change_top_bottom = pd.concat([APR_change_top, APR_change_bottom], axis = 0)

#Schools with largest positive and negative changes in average APR among all sports (2004-2019)
colors = ['green' if (x > 0) else 'red' for x in APR_change_top_bottom.values]
plt.figure()
sns.barplot(y = APR_change_top_bottom.index, x = APR_change_top_bottom.values, palette=colors).set(
    title='Schools with largest positive and negative changes in average APR among all sports (2004-2019)',
    xlabel = "change in average APR between 2004 and 2019",
    ylabel = "")
plt.savefig("figs/mean_APR_change.jpg")