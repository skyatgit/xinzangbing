import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#根据数据显示图表
def show_data(s_data):
    plt.xticks(rotation=90)  #字体倾斜度
    plt.xlabel(u'%s'%s_data[1])  # x轴标签
    plt.ylabel(u'患病人数')
    plt.title(u'%s--患病关系图'%s_data[1])  # 图的名称
    Healthy = [i[0] for i in s_data[0].values()]#健康人数列表
    ill = [i[1] for i in s_data[0].values()]#患病人数列表
    plt.bar(x=s_data[0].keys(),height=Healthy)#画健康人数柱
    plt.bar(x=s_data[0].keys(), height=ill,bottom=Healthy)#在健康人数柱上继续画患病人数柱
    plt.show()#显示图表
#对数据进行处理
def deal_data(data,sort_id):
    sort_data = data.sort_values(by=names[sort_id])#根据某一属性排序
    dict_data={}
    #统计该属性下每一值患病情况
    for i in sort_data.values.tolist():
        index = str(i[sort_id])
        value = int(i[13])
        if index in dict_data:
            dict_data[index][value] += 1
        else:
            dict_data[index] = [0, 0]
            dict_data[index][value] += 1
    return dict_data,names[sort_id]
names=['年龄','性别','胸腔疼痛类型','静态血压','胆固醇','空腹血糖含量是否达到120mg/dl','静态心电图','最大心率','运动是否引发心绞痛','运动相对休息诱发ST段压低','运动峰ST段坡度','用荧光染色的主要血管数量','地中海贫血','是否患有心脏病']
f_data=pd.read_csv('heart.csv',header=None,names=names)#读取数据
for i in range(14):
    sort_data = deal_data(f_data, i)
    show_data(sort_data)