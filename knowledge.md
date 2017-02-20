线性判别
LASSO
常见的时间序列算法模型 ARMA



SVM核函数包括：线性核函数，多项式核函数，径向基核函数，高斯核函数，幂指数核函数，拉普拉斯核函数，ANOVA核函数，二次有理核函数，多元二次核函数，逆向多元二次核函数及Sigmoid核函数。


LDA
如果先验分布和似然函数可以使得先验分布和后验分布有相同的形式，那么就称先验分布与似然函数是共轭的
SVM的原理，SVM里面的核
K-means，如何用hadoop实现k-means
naive bayes和logistic regression的区别
LDA的原理和推导
做广告点击率预测，用哪些数据什么算法
推荐系统的算法中最近邻和矩阵分解各自适用场景
用户流失率预测怎么做（游戏公司的数据挖掘都喜欢问这个）
一个游戏的设计过程中该收集什么数据
如何从登陆日志中挖掘尽可能多的信息

作者：刘志权
链接：https://www.zhihu.com/question/23259302/answer/24300412
来源：知乎
著作权归作者所有，转载请联系作者获得授权。



首先介绍自己的研究经历。会随机问一些细节。
我面的推荐，问了各类协同过滤的好与坏。
然后我说我做过LDA，问我，Dirichlet Distribution的定义和性质，并问我，为什么它和multinomial distribution是共轭的，顺便问了我啥叫共轭分布。
问了一个很有意思的问题，现实应用中的Top-N推荐问题和学术研究中的评分预测问题之间有什么不同。
问我ItemCF的工程实现，面对大数据如何实现，又追问了有没有什么工程优化算法。这个问题我没答好，一开始我说了一个MapReduce模型，他问能不能更快一点，我就卡那了。。。最后面试官告诉我，不能只从算法角度分析，要从系统设计分析，利用内存来减小MapReduce的吞吐量。（当然也许从MapReduce那一刻开始我就输了也不一定）
最后考了我一个基本概念，什么叫判别模型什么叫生成模型。

作者：王养浩
链接：https://www.zhihu.com/question/23259302/answer/24294685
来源：知乎
著作权归作者所有，转载请联系作者获得授权。