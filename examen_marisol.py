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

#Peores publicadores de videojuegos Top 10
ventas_consola = df.groupby("Publisher") ["JP_Sales"].sum().nsmallest(10).reset_index()
print("\n",ventas_consola)

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

menos_vendidos_nom_plat = df.groupby(["Name", "Platform"])["Global_Sales"].sum().nsmallest(10).reset_index()
print("\n", menos_vendidos_nom_plat)

menos_vendidos_plat = df.groupby(["Platform"])["Global_Sales"].sum().nsmallest(10).reset_index()
print("\n", menos_vendidos_plat)

mas_vendidos_nom_gen = df.groupby(["Name", "Genre"])["Global_Sales"].sum().nlargest(10).reset_index()
print("\n", mas_vendidos_nom_gen)