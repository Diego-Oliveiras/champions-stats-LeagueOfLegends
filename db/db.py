import psycopg2
import pandas as pd
#import os
#from dotenv import load_dotenv, find_dotenv
#from pathlib import Path
import psycopg2.extras as extras

#dotenv_path = Path('var.env')
#load_dotenv(dotenv_path)


def conect_leagueOflegends():
    con = psycopg2.connect(host='localhost',
                           port='5432',
                           database='leagueOfLegends',
                           user='postgres',
                           password='3j0%CAlEF')
    return con

def insert_in_LeagueOflegends(df, table):
    conn = conect_leagueOflegends()
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()