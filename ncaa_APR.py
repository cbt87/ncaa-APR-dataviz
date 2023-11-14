#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read in data
ncaa_df = pd.read_csv("https://ncaaorg.s3.amazonaws.com/research/academics/2020RES_APR2019PubDataShare.csv")

#reshape the dataset from wide to long so each row includes an academic progress rate
#for each year for each sport at every school

APR_rate = [col for col in ncaa_df.columns if "APR_RATE" in col]
ncaa_long = ncaa_df.melt(id_vars=ncaa_df.loc[:,"SCL_UNITID":"DATA_TAB_ANNUALRATE"],
                         value_vars=APR_rate,
                         var_name="year", 
                         value_name = "APR_rate")

#relabel year column
year_list = ncaa_long["year"].unique()
years = [2019, 2018, 2017,2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004]
ncaa_long['year'].replace(year_list, years, inplace = True)

#set fig size
plt.rcParams['figure.figsize'] = [15, 10]

#Question 1

#Academic Progress Rate Distribution Over Time
plt.figure()
sns.boxplot(y = ncaa_long["APR_rate"], x = ncaa_long["year"]).set(
    title="Academic Progress Rate Distribution Over Time",
    ylabel = "APR",
    xlabel = "")
plt.savefig("figs/APR_over_time.jpg")

#Academic Progress Rate Distribution (Southern University, Baton Rouge removed)
plt.figure()
SUBR_removed = ncaa_long[ncaa_long["SCL_NAME"]!= "Southern University, Baton Rouge"]  
sns.boxplot(y = SUBR_removed["APR_rate"], x = SUBR_removed["year"]).set(
    title="Academic Progress Rate Distribution (Southern University, Baton Rouge removed)",
    ylabel = "APR",
    xlabel = "")
plt.savefig("figs/APR_no_SUBR.jpg")

#Comparison for APR distributions for HBCUs and non HBCUs
plt.figure()
sns.boxplot(y = ncaa_long["APR_rate"], x = ncaa_long["year"], hue = ncaa_long["SCL_HBCU"]).set(
    title="Historically Black Colleges and University - Academic Progress Rate Distributions",
    ylabel = "APR",
    xlabel = "")
plt.legend(loc='upper left', labels=['HBCU', 'Non_HBCU'])
plt.savefig("figs/HBCU_boxplot.jpg")

#Mean Academic Progress Rate for Public and Private Schools Over Time
plt.figure()
ncaa_means = ncaa_long.groupby(["year","SCL_PRIVATE"]).mean()
sns.lineplot(data = ncaa_means, x = "year", y = "APR_rate",hue="SCL_PRIVATE").set(
    title="Mean Academic Progress Rate for Public and Private Schools Over Time",
    ylabel = "APR",
    xlabel = "")
plt.ylim(800, 1000)
plt.legend(loc='upper left', labels=['Public', 'Private'])
plt.savefig("figs/PVT_mean_APR.jpg")


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


#Question 3

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