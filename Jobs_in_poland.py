"""
EN: Generate a csv file and a barchart with the number of jobs per job category in the specified city in Poland. 
PL: Wygeneruj plik csv i wykres słupkowy z liczbą prac z podziałem na kategorie w wybranym polskim mieście.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from scrape import scrape_data

def graph(lang,city):
    """
    graph(lang,city)\n
    lang - pl or en\n
    city - any city in Poland written in english alphabet i.e. ó -> o, ś -> s etc.\n
    IMPORTANT:NAME OF THE CITY MUST BE IN POLISH\n
    Generate barplot with the number of jobs per job name
    """
    if lang not in ['en','pl']:
        return print('Error: Pleas select a valid paramater.\nTip: You can choose en for english and pl for polish.')
    if lang == 'pl':
        scrape_data(lang,city)
        df = pd.read_csv('Praca_w_Gryfinie.csv')
        plt.figure(figsize=(12,6))
        sns.barplot(x='Job_name',y='Number_of_Jobs',data=df,hue='Job_name',palette='Set3',dodge=False)
        plt.xticks(rotation=90)
        plt.ylabel('Liczba prac')
        plt.xlabel("Nazwa stanowiska")
        plt.subplots_adjust(bottom=0.4)
        plt.title(f"Liczba ofert prac ze względu na kategorie - {city}")
        plt.legend([],[], frameon=False)
        plt.savefig(f'Praca_w_{city}.png')
    if lang == 'en':
        scrape_data(lang,city)
        df = pd.read_csv('Praca_w_Gryfinie.csv')
        plt.figure(figsize=(12,6))
        sns.barplot(x='Job_name',y='Number_of_Jobs',data=df,dodge=False,hue='Job_name',palette='Set3')
        plt.xticks(rotation=90)
        plt.ylabel('Number of jobs')
        plt.xlabel("Occupation category")
        plt.subplots_adjust(bottom=0.4)
        plt.title(f"Jobs in {city}")
        plt.legend([],[], frameon=False)
        plt.savefig(f'Jobs_in_{city}.png')
