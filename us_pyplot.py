#!/bin/python
# -*- coding:UTF-8 -*-
# data source : https://www.kaggle.com/kaggle/us-baby-names/data


########################### 利用ipython绘图

import pandas as pd 
import numpy as np 
from collections import Counter
import matplotlib.pyplot as plt

############## 图1 

# years = [1880, 1881, ..., 2014]
years = range(1880, 2015)

# 使用matplotlib进行数据可视化
f, ax = plt.subplots(figsize=(10, 6))

# 设置x轴数值范围
ax.set_xlim([1880, 2014])

# years为x轴，average_length为y轴
# 女性曲线为红色，男性为蓝色
plt.plot(years, female_average_length, label='Average length of female names', color='r')
plt.plot(years, male_average_length, label='Average length of male names', color='b')

# 设置x,y轴标签
ax.set_ylabel('Length of name')
ax.set_xlabel('Year')

# 设置图像名称
ax.set_title('Average length of names')

# 设置图例
legend = plt.legend(loc='best', frameon=True, borderpad=1, borderaxespad=1)
#如果不加plt.show()，图像显示不出来的
plt.show()


############## 图2
f, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim([1880, 2014])

plt.plot(years, percent_unique_names, label='Percent of unique names', color='black')

ax.set_ylabel('Percent of unique names')
ax.set_xlabel('Year')
ax.set_title('Percent of unique names')
legend = plt.legend(loc='best', frameon=True, borderpad=1, borderaxespad=1)
plt.show()



############## 图3
def plotname(name, gender):
    """
        对姓名及性别进行可视化
    """
    # 找到符合条件的数据
    data_named = data[(data.Name==name) & (data.Gender==gender)]
        
    plt.figure(figsize=(10,6))    
    # 对数据的年份，数量进行可视化
    plt.plot(data_named.Year,data_named.Count,'g-')
    plt.title('%s name variation over time'%name)
    plt.ylabel('counts')
    plt.xticks(data_named.Year,rotation='vertical')
    
    # 设置x轴数值范围
    plt.xlim([1985,2015])    
    plt.show()

#老友记 姓名影响分析
friends_characters = [('Rachel','F'),('Monica','M'),('Phoebe','F'),('Ross','F'),('Chandler','F'),('Joey','F')]

for character in friends_characters:
    plotname(character[0],character[1])



# 冰火歌 和 生活大爆炸 姓名影响分析
more_characters = [('Khaleesi', 'F'), ('Sheldon', 'M')]

for character in more_characters:
    plotname(character[0],character[1])