## Exercise 0
def github(): 
    """
    This function returns a link to my solutions on GitHub.
    """    
    return "https://github.com/LinyiXia01/ECON481-Sp24/blob/main/hw5.py"

github()


## Exercise 1
import requests
from bs4 import BeautifulSoup

def scrape_code(url: str) -> str:
    """
    This function takes the HTML format of a course website's URL as its argument and 
    returns a string containing all the python code in the lecture.  
    """
    req_obj = requests.get(url)
    
    if req_obj.ok == True:
        soup = BeautifulSoup(req_obj.text)
        code_obj = soup.find_all('code', attrs={'class': 'sourceCode python'})     
        python_code = ''      
        for code in code_obj:
            code_text = '\n'.join(line for line in code.get_text().splitlines() if not line.strip().startswith('%'))
            python_code += code_text + '\n'
        return python_code 
    
    else:
        return 'Failed to fetch.'

print(scrape_code('https://lukashager.netlify.app/econ-481/01_intro_to_python#/strings'))

