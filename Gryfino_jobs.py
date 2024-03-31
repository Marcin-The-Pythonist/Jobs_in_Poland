"""
EN: Generate a csv file and a barchart with the number of jobs per job category in Gryfino. 
PL: Wygeneruj plik csv i wykres słupkowy z liczbą prac z podziałem na kategorie w Gryfinie.

Use Graph Function to see the result.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from scrape import scrape_data

def graph():
    """
    Generate barplot with the number of jobs per job name
    """
    scrape_data()
    df = pd.read_csv('Praca_w_Gryfinie.csv')
    plt.figure(figsize=(12,6))
    sns.barplot(x='Job_name',y='Number_of_Jobs',data=df,hue='Job_name',palette='Set3')
    plt.xticks(rotation=90)
    plt.ylabel('Liczba prac')
    plt.xlabel("Nazwa stanowiska")
    plt.subplots_adjust(bottom=0.4)
    plt.title("Prace w Gryfinie")
    plt.savefig('Praca_w_Gryfinie.png')


