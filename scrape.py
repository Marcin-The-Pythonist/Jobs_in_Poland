import requests
from bs4 import BeautifulSoup
import pandas as pd 
"""
Scrape data from OLX sites about jobs in Gryfino. 
"""
def scrape_data():
    """
    Scrape data from OLX sites about jobs in Gryfino. 
    """
    raw_data = requests.get('https://www.olx.pl/praca/gryfino/')
    html_data = BeautifulSoup(raw_data.text,'html.parser')
    job_name = html_data.select('.css-1bdi9t1')



    list_of_jobs = []

    for i in range(len(job_name)):
        list_of_jobs.append(job_name[i].text)

    number_of_jobs = []

    for item in list_of_jobs:
        number_of_jobs.append(item[-1])

    print(number_of_jobs)

    list_of_jobs_trimmed = []

    for item in list_of_jobs:
        list_of_jobs_trimmed.append(item[:-1])

    print(list_of_jobs_trimmed)


    data = list(zip(list_of_jobs_trimmed,number_of_jobs)) 


    df = pd.DataFrame(data,columns=['Job_name','Number_of_Jobs'])

    df.to_csv('Praca_w_Gryfinie.csv')