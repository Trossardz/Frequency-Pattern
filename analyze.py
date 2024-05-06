import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from data_process import transactions
transaction_list = transactions['ToNodeId'].tolist()
te = TransactionEncoder()
te_ary = te.fit(transaction_list).transform(transaction_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = fpgrowth(df, min_support=0.01, use_colnames=True).sort_values(by='support', ascending=False)
pd.set_option('display.max_rows', None)
print(frequent_itemsets)
pd.reset_option('display.max_rows')