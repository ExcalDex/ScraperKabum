import json
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

name_file: str = input("digite o nome do arquivo json (sem .json no final)")
name_product: str = input("Digite o nome do produto ")

with open(f'{name_file}.json', 'r') as f:
    df_data: pd.DataFrame = pd.DataFrame(json.loads(f.read()))

product_data = df_data[df_data['Nome'].str.contains(name_product, case=False, na=False)]
product_data.sort_values(by="Valor", inplace=True)
print(product_data)
