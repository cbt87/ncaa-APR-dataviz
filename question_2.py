#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import data
ncaa_long = pd.read_csv("data/ncaa_long.csv")

#set fig size
plt.rcParams['figure.figsize'] = [15, 10]

#Question 2

#create a new column that splits sports into gender category
ncaa_long[["SPORT_NAME","SPORT_CODE"]].value_counts()

def gender_split(sport):
    if "Men" in sport:
        result = "Men"
    elif "Women" in sport:
        result = "Women"
    elif sport in ["Baseball","Football"]:
        result = "Men"
    elif "Mixed" in sport:
        result = "mixed"
    return result

ncaa_long['GENDER'] = ncaa_long['SPORT_NAME'].apply(gender_split)

#Academic Progress Rate for Men and Women's Sports Over Time
plt.figure()
sns.boxplot(x = ncaa_long["year"], y = ncaa_long["APR_rate"], hue = ncaa_long["GENDER"]).set(
    title="Academic Progress Rate for Men and Women's Sports Over Time",
    ylabel = "APR",
    xlabel = "")
plt.savefig("figs/gender_agg_overtime.jpg")
