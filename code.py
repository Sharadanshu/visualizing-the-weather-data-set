# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    """
    monthly_data = weather_df.groupby(weather_df.index.strftime(period))[[col]].mean()
    calender_months = calendar.month_name[1:]
    calender_months
    plt.plot(calender_months,monthly_data['Temp (C)'])
    plt.ylabel('Temp (C)')
    plt.xticks(rotation = 90)
    plt.title('Temperature Trend, 2012')
    plt.show()
 

# Function to perform univariate analysis of categorical columns

def plot_categorical_columns(df):
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    for i in df.columns:
        c = df.groupby(i).size().reset_index(name='counts')
        plt.figure(figsize=(10,5))
        plt.bar(c[i],c['counts'])
        plt.xticks(rotation =90)
        plt.show()
 

# Function to plot continous plots

def plot_cont(df,plt_typ):
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """
    for i in numerical.columns:
        sns.distplot(numerical[i])
        plt.xlabel(i)
        plt.title((numerical.columns).get_loc(i) + 1)
        plt.show()
 

# Function to plot grouped values based on the feature

def group_values(df,col1,agg1,col2):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    groupby_weather = df.groupby(col2).agg({col1:agg1})
    plt.figure(figsize=(20,5))
    plt.bar(groupby_weather.index,groupby_weather[col1])
    plt.xticks(rotation = 90)
    plt.show()
    

# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df  = pd.read_csv(path,parse_dates=True, index_col='Date/Time')
weather_df.head()

# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
line_chart(weather_df,'%m','Temp (C)') 


# Now let's perform the univariate analysis of categorical features.
categorical = weather_df.select_dtypes(include = 'object')
numerical = weather_df.select_dtypes(include = 'number')
# Call the "function plot_categorical_columns()" with appropriate parameters.
plot_categorical_columns(categorical)  


# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot
plot_cont(weather_df,'boxplot')    


# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
group_values(weather_df,'Visibility (km)','mean','Weather')



