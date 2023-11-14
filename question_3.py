#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from question_2 import gender_split


#import data
ncaa_long = pd.read_csv("data/ncaa_long.csv")

#set fig size
plt.rcParams['figure.figsize'] = [15, 10]

#Question 3

ncaa_long['GENDER'] = ncaa_long['SPORT_NAME'].apply(gender_split)

#Academic Progress Rate Distributions for Men's Sports
plt.figure()
men_df = ncaa_long[ncaa_long["GENDER"] == "Men"]
sns.boxplot(y = men_df["SPORT_NAME"], x = men_df["APR_rate"]).set(
    title="Academic Progress Rate Distributions for Men's Sports",
    ylabel = "",
    xlabel = "APR")
plt.savefig("figs/men_sports.jpg")

#Academic Progress Rate Distributions for Women's Sports
plt.figure()
women_df = ncaa_long[ncaa_long["GENDER"] == "Women"]
sns.boxplot(y = women_df["SPORT_NAME"], x = women_df["APR_rate"]).set(
    title="Academic Progress Rate Distributions for Women's Sports",
    ylabel = "",
    xlabel = "APR")
plt.savefig("figs/women_sports.jpg")