#se importa el bd y se crea un data frame
import pandas as pd 
df = pd.read_csv('vgsales.csv')
print (df.head())

#eliminar duplicados
df = df.drop_duplicates()


#Rellenar valores nulos
df = df.fillna("Unknown")

#Convertir año a entero (algunos vienen como float o NaN)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)

# Crear una métrica: ventas totales por
sales_by_genre = df.groupby("Genre") ["Global_Sales"].sum().reset_index()
print("\n",sales_by_genre)

#calcular el top 5
top_publishers = df.groupby("Publisher")["Global_Sales"].sum().nlargest(5).reset_index()
print("\n",top_publishers)

japan_sales = df.groupby('Name')['JP_Sales'].sum().nlargest(10).reset_index()
print("\n",japan_sales)

EU_sales = df.groupby('Name')['EU_Sales'].sum().nlargest(10).reset_index()
print("\n",EU_sales)

NA_sales = df.groupby('Name')['NA_Sales'].sum().nlargest(10).reset_index()
print("\n",NA_sales)

jp_gre_sales = df.groupby('Genre')['JP_Sales'].sum().nlargest(10).reset_index()
print("\n",jp_gre_sales)

EU_gre_sales = df.groupby('Genre')['EU_Sales'].sum().nlargest(10).reset_index()
print("\n",EU_gre_sales)

NA_gre_sales = df.groupby('Genre')['NA_Sales'].sum().nlargest(10).reset_index()
print("\n",NA_gre_sales)


import sqlite3

conn = sqlite3.connect("videogames.db")
df.to_sql("vgsales_clean", conn, if_exists="replace", index=False)
sales_by_genre.to_sql("sales_by_genre", conn, if_exists="replace", index=False)
top_publishers.to_sql("top_publishers", conn, if_exists="replace", index=False)
japan_sales.to_sql("japan_sales", conn, if_exists="replace", index=False)
jp_gre_sales.to_sql("jp_genre_sales", conn, if_exists="replace", index=False)
EU_gre_sales.to_sql("eu_sales", conn, if_exists="replace", index=False)
NA_gre_sales.to_sql("na_sales", conn, if_exists="replace", index=False)
EU_sales.to_sql("EU_sales_name", conn, if_exists="replace", index=False)
NA_sales.to_sql("NA_sales_name", conn, if_exists="replace", index=False)

conn.close()

print ("Datos cargados en la base de datos.")
#

try:
    import streamlit as st
except ModuleNotFoundError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
    import streamlit as st
import sqlite3
import pandas as pd

# Conectar a la base
conn = sqlite3.connect("videogames.db")

# Cargar tabla
df = pd.read_sql("SELECT * FROM vgsales_clean", conn)

# Dashboard
st.title("Ventas de Videojuegos")
st.bar_chart(df.groupby("Genre")["Global_Sales"].sum())
st.line_chart(df.groupby("Year")["Global_Sales"].sum())