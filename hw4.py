## Exercise 0
def github(): 
    """
    This function returns a link to my solutions on GitHub.
    """    
    return "https://github.com/LinyiXia01/ECON481-Sp24/blob/main/hw4.py"

github()


## Exercise 1
import pandas as pd

def load_data() -> pd.DataFrame:
    """
    This function accesses the Tesla stock price file on the course website
    and returns the data as pd.DataFrame
    """
    url = "https://lukashager.netlify.app/econ-481/data/TSLA.csv"
    tsla_df = pd.read_csv(url)

    return tsla_df


## Exercise 2
import matplotlib.pyplot as plt

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    The function takes dataframe, an optional start and end date as arguments
    and plots the closing price of the stock between those dates as a line graph.
    """
    date1 = pd.to_datetime(start)
    date2 = pd.to_datetime(end)
    df2 = df[['Date', 'Close']].copy() #create a copy for the slice
    df2['Date'] = pd.to_datetime(df2['Date'])
    select_df = df2[(df2['Date'] >= date1) & (df2['Date'] <= date2)]
    
    plt.plot(select_df['Date'], select_df['Close'])
    plt.title(f"Closing Price of Tesla Stock ({start} to {end})")
    plt.xlabel("Date")
    plt.ylabel("Price")

data = load_data()
plot_close(data, '2010-06-29', '2021-07-06')


## Exercise 3
import statsmodels.api as sm

def autoregress(df: pd.DataFrame) -> float:
    """
    This function takes a single df as argument and 
    returns the t statistics on beta hat from the given regression equation.
    """
    df['Datetime'] = df['Date']
    df = df.set_index('Datetime')
    df.index = pd.to_datetime(df.index)    
    
    df['delta_x'] = df['Close'] - df['Close'].shift(1,freq = 'D')
    df = df[~pd.isna(df['delta_x'])]
    df['delta_x-1'] = df['delta_x'].shift(1)
    df = df[~pd.isna(df['delta_x-1'])]
    
    y = df['delta_x']
    X = df['delta_x-1']
    model = sm.OLS(y, X)
    results = model.fit(cov_type='HC1')
    
    return results.tvalues['delta_x-1']

autoregress(data)


## Exercise 4
def autoregress_logit(df: pd.DataFrame) -> float:
    """
    This function takes a single df as argument and returns 
    the t statistics on beta hat from the given logistic regression.
    """
    df['Datetime'] = df['Date']
    df = df.set_index('Datetime')
    df.index = pd.to_datetime(df.index)      
    df['delta_x'] = df['Close'] - df['Close'].shift(1,freq = 'D')
    df = df[~pd.isna(df['delta_x'])]
    df['delta_x-1'] = df['delta_x'].shift(1)
    df = df[~pd.isna(df['delta_x-1'])]
    df['positive_delta_x'] = (df['delta_x'] > 0).astype(int)
    
    y = df['positive_delta_x']
    X = df['delta_x-1']
    model = sm.Logit(y, X)
    results = model.fit()

    return results.tvalues['delta_x-1']

autoregress_logit(data)


## Exercise 5
def plot_delta(df: pd.DataFrame) -> None:
    """
    This function takes a single argument df (the output of load_data()) and 
    plots the delta_xt for the full dataset.
    """
    df['Close_diff'] = df['Close'] - df['Close'].shift(1)
    df = df[~pd.isna(df['Close_diff'])]
    
    plt.plot(df['Date'], df['Close_diff'])
    plt.title("Differences of closing prices for two consecutive days")
    plt.xlabel("Date")
    plt.ylabel("Delta closing price")

plot_delta(data)
    





