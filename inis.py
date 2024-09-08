from  sklearn import datasets #加载数字数据集
from  sklearn.model_selection import train_test_split
'''导入train_test_split`函数train_test_split`函数用于将
数据集划分为训练集和测试集，train_test_split为模块'''
#from  sklearm.linear_model import import logisticRegression
         from sklearn.linear_model import LogisticRegression
'''1. `LinearRegression`: 用於執行簡單的線性回歸分析。
2. `Ridge`和`Lasso`: 這兩個類別是使用梯度下降法進行懲罰回歸分析。
3. `HuberRegressor`: 與`LineraRegression`不同的地方在於，它能更好地處理含有出     
圍錯誤的數據集。
4. `RandomForestRegressor`: 基於決策樹的線性回歸模型。
5. `SGDRegressor`: 使用梯度下降法進行線性回歸分析。
6. `BayesianRidge`: 該模型結合了線性回歸和高斯過程來對數況進行預測。'''

#加载鸢尾花数据集
iris = datasets.load_iris() '''iris是鹤尾花数据集代称该
数据集包含3种不同的植物（瘴薄荷、红杉花和琼藕），每
种植物都有4个特征（花瓣长度、花瓣宽度、 sepala
length(长度) 和 sepala width(宽度)）
'''

x = iris.data   # 输出所有特征值
y = iris.target  # 输出标签值


# 将数据集拆分为70%训练集和30%测试集
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.3)
'''train是指训练模型test是指训练好的模型'''

#创建逻辑回归对象
'''这里我们没有传递任何参数到`LogisticRegression()`函数中，所以默认情况下，它将使    
用逻辑回归模型的默认参数。'''
lr = LogisticRegressiom()
''''"fit"是一個常用的Python機器學習庫中的函數，主要用於訓練模型。它接收兩個參數：    
數據集（X）和標籤（y）。`fit`函數會將這些數據用於調整模型參數，使其能更好地進     
行數況分類或數況回歸。'''
lr.fit(x_train,y_train)

#对测试集进行预测
y_pred = lr.predict(x_test)