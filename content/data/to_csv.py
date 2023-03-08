import pandas as pd

read_file = pd.read_csv (r'/home/pippozord/Scrivania/anagrafica.txt')
read_file.to_csv (r'/home/pippozord/Scrivania/Statistica/2023/superhero-datascience/content/data/anagrafica.csv', index=None)