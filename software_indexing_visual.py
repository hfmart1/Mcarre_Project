##Importer les bibliothèques
import pandas as pd
import os
from subprocess import Popen

import pymysql
from sqlalchemy import create_engine


##  Récupérer les données sur le serveur et les exporter en format csv
def listsoft_df():
    df = pd.read_sql_table("listsoft", engine)
    return df

def clean_csv_soft(df):
    df.to_csv('listsoft.csv', index = False)
    return


##  Supprimer les données sur le serveur
def del_sql_listsoft():
    engine.connect().execute("DELETE FROM listsoft")


##  Créer un dataframe à partir d'un fichier csv
def listsoft_rcsv():
    df = pd.read_csv("listsoft.csv")
    return df

## Importer le fichier csv sur le serveur
def export_data(df):
    df.to_sql('listsoft', con = engine, if_exists = 'append', chunksize = 1000, index=False)


def intro():
    print("                   ,---------------------------,")
    print("                   |  /---------------------\  |")
    print("                   | |                       | |")
    print("                   | |    Visual             | |")
    print("                   | |     Software          | |")
    print("                   | |      Indexing         | |")
    print("                   | |       Mcarre          | |")
    print("                   | |                       | |")
    print("                   |  \_____________________/  |")
    print("                   |___________________________|")
    print("                 ,---\_____     []     _______/------,")
    print("               /         /______________\           /|")
    print("             /___________________________________ /  | ___")
    print("             |                                   |   |    )")
    print("             |  _ _ _                 [-------]  |   |   (")
    print("             |  o o o                 [-------]  |  /    _)_")
    print("             |__________________________________ |/     /  /")
    print("         /-------------------------------------/|      ( )/")
    print("       /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /")
    print("     /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /")
    print("     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n\n")

    print("!!! ATTENTION !!!!"  + "\n\n")
    print("Une mauvaise utilisation de ce logiciel peut engendrer la suppression du tableau des données.")




if __name__ == '__main__':
    ## create sqlalchemy engine for dev
    engine = create_engine("mysql+pymysql://{user}:{pw}@########"/{db}"
                           .format(user="#############", pw="#########",
                                   db="############")).connect()

    intro()

    clean_csv_soft(listsoft_df())

    Popen('listsoft.csv', shell = True)

    input("Une fois les modifications terminées appuyez sur Entrer pour continuer...")

    temp = listsoft_rcsv()

    del_sql_listsoft()

    export_data(temp)

    os.remove('listsoft.csv')
