#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import data
ncaa_long = pd.read_csv("data/ncaa_long.csv")

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