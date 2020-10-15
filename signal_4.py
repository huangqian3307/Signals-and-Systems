#抽样函数
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']  #标题可以出现中文
plt.rcParams['axes.unicode_minus']=False    #正常显示负号

x = np.linspace(-5.0 * np.pi,5.0*np.pi,1000)  #t的取值范围
y = np.sinc(x/np.pi)   #调用sinc函数计算抽样信号
plt.ylim(-0.5,1.2)       #定义纵轴取值范围
plt.plot(x,y)               #绘图
plt.title(u'抽样信号') 
plt.show()