import pandas as pd

## Exercise 2
def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Some docstrings.
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