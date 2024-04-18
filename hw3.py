## Exercise 0
def github(): 
    """
    This function returns a link to my solutions on GitHub.
    """    
    return "https://github.com/LinyiXia01/ECON481-Sp24/blob/main/hw3.py"

github()


## Exercise 1
import pandas as pd

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    This function takes as its argument a list of years and returns a concatenated DataFrame 
    of the Direct Emitters tab of EPA excel sheet for the given years.
    """
    df_list = []
    for year in years:
        url = f"https://lukashager.netlify.app/econ-481/data/ghgp_data_{year}.xlsx"
        df = pd.read_excel(url, sheet_name = "Direct Emitters", skiprows=3)        
        df['year'] = year
        df_list.append(df)
    concat_df = pd.concat(df_list, ignore_index = True)
    
    return concat_df

years_list = [2019]
df1 = import_yearly_data(years_list)
print(df1)


## Exercise 2
def import_parent_companies(years: list) -> pd.DataFrame:
    """
    This function takes as its argument a list of years and returns a concatenated DataFrame 
    of the corresponding year tabs in the parent companies excel sheet.
    """ 
    df_list = []
    url = "https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb"
    excel = pd.ExcelFile(url)  # read the url of the excelfile and store it. 
    for year in years:
        # determine if the years in input has corresponding sheets in the excel 
        if year in excel.sheet_names:   
            df = pd.read_excel(excel)
            df['year'] = year
            df_list.append(df)
        else:
            print("sheet name did not find.")
    concat_df = pd.concat(df_list, ignore_index = True)
    concat_df[~concat_df.isna()]
    return concat_df

## test
years = [2019, 2020]
df2 = import_parent_companies(years)
print(df2)
    

## Exercise 3
def n_null(df: pd.DataFrame, col: str) -> int:
    """
    This function takes a dataframe and the dataframe's column names as its arguments 
    and returns the number of null values in the specific columns.
    """
    return df[col].isnull().sum()


## Exercise 4
def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes Exercise 1 and Exercise 2's outputs as its arguments and returns
    a cleaned dataframe.
    """
    parent_data.rename(columns = {'GHGRP FACILITY ID': 'Facility Id'}, inplace = True)
    merged_df= pd.merge(emissions_data, parent_data, on=['year', 'Facility Id'], how ='left')
    
    subset_df = merged_df.loc[['Facility Id', 'year', 'State', 'Industry Type (sectors)',
                                   'Total reported direct emissions', 'PARENT CO. STATE', 
                                   'PARENT CO. PERCENT OWNERSHIP']]
    subset_df.columns = subset_df.columns.str.lower()  #lowercase all the column names
   
    return subset_df


## Exercise 5
def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    This function akes as input a DataFrame with the schema of the output of Exercise 4 
    and a list of variables and produces the min, median, mean, and max values for the given variables 
    aggregated at the level of the variables supplied in the argument and returns the data 
    sorted by highest to lowest mean total reported direct emissions.
    """
    group_df = df.groupby(group_vars, as_index=True)["total reported direct emissions", "parent co. percent ownership"]
    agg_df = group_df.agg(["min", "median", "mean", "max"])
    agg_df = agg_df.sort_values(by=("total reported direct emissions", "mean"), ascending = False)
    return agg_df



