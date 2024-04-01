import requests
from bs4 import BeautifulSoup
import pandas as pd 
from googletrans import Translator

translator = Translator()
def scrape_data(lang):
    """
    Scrape data from OLX sites about jobs in Gryfino. 
    """
    raw_data = requests.get('https://www.olx.pl/praca/gryfino/')
    html_data = BeautifulSoup(raw_data.text,'html.parser')
    job_name = html_data.select('.css-1bdi9t1')


    if lang == 'pl':
        list_of_jobs = []

        for i in range(len(job_name)):
            list_of_jobs.append(job_name[i].text)

        number_of_jobs = []

        for item in list_of_jobs:
            number_of_jobs.append(item[-1])

        list_of_jobs_trimmed = []

        for item in list_of_jobs:
            list_of_jobs_trimmed.append(item[:-1])

        data = list(zip(list_of_jobs_trimmed,number_of_jobs)) 

        df = pd.DataFrame(data,columns=['Job_name','Number_of_Jobs'])

        df.to_csv('Praca_w_Gryfinie.csv')

    if lang == 'en':
        pl = """Administracja biurowa
Badania i rozwój
Budowa / remonty
Dostawca, kurier miejski
E-commerce (handel internetowy)
Edukacja
Energetyka
Finanse / księgowość
Franczyza / Własna firma
Fryzjerstwo, kosmetyka
Gastronomia
HR
Hostessa, roznoszenie ulotek
Hotelarstwo
Inżynieria
IT / telekomunikacja
Kierowca
Logistyka, zakupy, spedycja
Marketing i PR
Mechanika i lakiernictwo
Montaż i serwis
Obsługa klienta i call center
Ochrona
Opieka
Praca za granicą
Prace magazynowe
Pracownik sklepu
Produkcja
Rolnictwo i ogrodnictwo
Sprzątanie
Sprzedaż
Wykładanie i ekspozycja towaru
Zdrowie
Pozostałe oferty pracy
Praktyki / staże
Kadra kierownicza
Praca sezonowa
Zapraszamy seniorów
Praca dodatkowa"""
        en = """office administration
Research and development
Construction/renovations
Delivery person, city courier
E-commerce (online trade)
Education
Power engineering
Finance/accounting
Franchise / Own company
Hairdressing, cosmetics
Gastronomy
HR
Hostess, distributing leaflets
Hotel industry
Engineering
IT/telecommunications
Driver
Logistics, purchasing, forwarding
Marketing and PR
Mechanics and painting
Installation and service
Customer service and call center
Security
Care
working abroad
Warehouse work
Store employee
Production
Agriculture and gardening
Cleaning
Sale
Arranging and displaying goods
Health
Other job offers
Internships/internships
Managers
seasonal work
We welcome seniors
additional job"""   

        en_list = en.split("\n")
        pl_list = pl.split("\n")
        en_dict = dict(zip(pl_list,en_list))
        print(en_dict)

        list_of_jobs = []

        for i in range(len(job_name)):
            list_of_jobs.append(job_name[i].text)

        number_of_jobs = []

        for item in list_of_jobs:
            number_of_jobs.append(item[-1])

        list_of_jobs_trimmed = []

        for item in list_of_jobs:
            list_of_jobs_trimmed.append(en_dict.get(item[:-1]))
            print(en_dict.get(item[:-1]))

        data = list(zip(list_of_jobs_trimmed,number_of_jobs)) 

        df = pd.DataFrame(data,columns=['Job_name','Number_of_Jobs'])

        df.to_csv('Praca_w_Gryfinie.csv')