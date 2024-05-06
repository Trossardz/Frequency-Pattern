论文引用模式挖掘
数据获取与预处理
本次作业选用的数据集为SNAP中的High-energy physics theory citation network数据集。数据集中涵盖了来自arXiv上高能物理领域共计27,770篇论文和352,807条引用关系。
可以用节点表示一篇论文，用有向边表示论文之间的引用关系。如果论文 i 引用了论文 j，则该图包含从 i 到 j 的有向边。
在预处理部分将数据整理成一个事务列表，其中每个事务包含一个论文（FromNodeId）引用的所有其他论文（ToNodeId）。这部分代码见data_process.py。
频繁模式挖掘
数据集中包括27770个论文（事务），如果使用Apriori算法进行频繁模式挖掘，频繁2项集的数量就高达七亿，产生的开销过大。
这里采用FP-growth算法进行频繁模式挖掘。
具体来说，首先对数据库进行一次扫描，统计每个项的支持度（出现频率），去除不满足最小支持度阈值的项。
然后，构建初始FP树，将所有事务重新按项的支持度降序排序后插入FP树。开始时，FP树只有一个根节点，依次将每个事务中的项按顺序插入到FP树中，共享公共前缀的路径。条件模式基是指以目标项为结尾的路径集合，它相当于是该项的一个“条件”数据库。对每个项的条件模式基构建FP树，并递归地挖掘这些树，直到树变得足够小或者不能再分解。
这部分代码见analyze.py。
数据挖掘结果分析
如果设定支持度阈值为0.05，得到的频繁项集如下所示：

从中我们可以看出，最频繁地被引用的三篇论文是编号为9711200，9802150，9802109这三篇论文，而引用了这三篇论文中任意一篇，大概率也会引用其余两篇。
数据可视化展示

  这里展示了支持度前20的频繁项集。这部分代码见visualization.py# Frequency-Pattern
