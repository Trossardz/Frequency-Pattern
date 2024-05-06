import pandas as pd
data = pd.read_csv('Cit-HepTh.txt', sep='\t', header=0)
transactions = data.groupby('FromNodeId')['ToNodeId'].apply(list).reset_index()
print(transactions.head())