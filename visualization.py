import matplotlib.pyplot as plt
from analyze import frequent_itemsets
# 只选取支持度最高的前20个频繁项集
top_itemsets = frequent_itemsets.head(20)

# 将项集列转换为字符串
top_itemsets['itemsets'] = top_itemsets['itemsets'].apply(lambda x: ', '.join(str(item) for item in x))

plt.figure(figsize=(12, 8))
plt.bar(top_itemsets['itemsets'], top_itemsets['support'], color='blue')
plt.xlabel('Itemsets')
plt.ylabel('Support')
plt.title('Top 20 Frequent Itemsets by Support')
plt.xticks(rotation=90) 
plt.show()
