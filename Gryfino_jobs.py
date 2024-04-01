"""
EN: Generate a csv file and a barchart with the number of jobs per job category in Gryfino. 
PL: Wygeneruj plik csv i wykres słupkowy z liczbą prac z podziałem na kategorie w Gryfinie.

Use Graph Function to see the result.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from scrape import scrape_data

def graph(lang):
    """
    Params: lang='en' or 'pl'\n
    Generate barplot with the number of jobs per job name
    """
    if lang not in ['en','pl']:
        return print('Error: Pleas select a valid paramater.\nTip: You can choose en for english and pl for polish.')
    if lang == 'pl':
        scrape_data(lang)
        df = pd.read_csv('Praca_w_Gryfinie.csv')
        plt.figure(figsize=(12,6))
        sns.barplot(x='Job_name',y='Number_of_Jobs',data=df,hue='Job_name',palette='Set3',dodge=False)
        plt.xticks(rotation=90)
        plt.ylabel('Liczba prac')
        plt.xlabel("Nazwa stanowiska")
        plt.subplots_adjust(bottom=0.4)
        plt.title("Prace w Gryfinie")
        plt.legend([],[], frameon=False)
        plt.savefig('Praca_w_Gryfinie.png')
    if lang == 'en':
        scrape_data(lang)
        df = pd.read_csv('Praca_w_Gryfinie.csv')
        plt.figure(figsize=(12,6))
        sns.barplot(x='Job_name',y='Number_of_Jobs',data=df,hue='Job_name',palette='Set3',dodge=False)
        plt.xticks(rotation=90)
        plt.ylabel('Number of jobs')
        plt.xlabel("Occupation category")
        plt.subplots_adjust(bottom=0.4)
        plt.title("Jobs in Gryfino")
        plt.legend([],[], frameon=False)
        plt.savefig('Jobs_in_Gryfino.png')