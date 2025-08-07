import pandas as pd

df = pd.read_excel('titanic.xlsx') 
df.columns = df.columns.str.strip()  

print("Colunas do DataFrame:", df.columns)

mediana = df['Age'].median()
df['Age'].fillna(mediana, inplace=True)

print("Mediana utilizada:", mediana)

df.to_csv('titanic_tratado.csv', index=False)
print("Arquivo salvo como 'titanic_tratado.csv'")

