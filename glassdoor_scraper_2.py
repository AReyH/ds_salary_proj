import glassdoor_scraper as gs
import pandas as pd

path = 'C:/Users/Arthur Rey/Desktop/ds_salary_proj/chromedriver.exe'
df = gs.get_jobs('data scientist',10,False,path)

df.to_csv('selenium3.csv')