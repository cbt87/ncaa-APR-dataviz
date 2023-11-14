#import packages
import pandas as pd


#read in data
ncaa_df = pd.read_csv("https://ncaaorg.s3.amazonaws.com/research/academics/2020RES_APR2019PubDataShare.csv")
ncaa_df.to_csv("data/ncaa_df.csv")
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

ncaa_long.to_csv("data/ncaa_long.csv")