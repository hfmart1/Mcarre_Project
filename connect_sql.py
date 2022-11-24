import pandas as pd

##import mysql.connector as msql
##from mysql.connector import Error

import pymysql

from sqlalchemy import create_engine

## Import csv file
df_soft = pd.read_csv("data_soft.csv")

#### create sqlalchemy engine
##engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"  
##                      .format(user="root", pw="password", 
##                      db="m2db"))


###### EXPORT DF CSV

## create sqlalchemy engine for dev
engine = create_engine("mysql+pymysql://{user}:{pw}@10.1.15.12:3306/{db}"  
                      .format(user="dev", pw="dev", 
                      db="m2db"))

##Insert whole DataFrame into MySQL
df_soft.to_sql('listsoft', con = engine, if_exists = 'append', chunksize = 1000, index=False)

###### END



########## READ TABLE
##
#### create sqlalchemy engine for dev
##engine = create_engine("mysql+pymysql://{user}:{pw}@10.1.15.12:3306/{db}"  
##                      .format(user="dev", pw="dev", 
##                      db="m2db")).connect()
##
#### table as panda df
##df = pd.read_sql_table("softwarem2", engine)
##
##print(df.head())
##
########## END
