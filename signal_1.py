#指数信号
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']  #标题可以出现中文
plt.rcParams['axes.unicode_minus']=False    #正常显示负号

t = np.linspace(-10,10.100)     #t的取值范围
plt.ylim(0,10)      #纵轴y的取值范围

plt.subplot(2,2,1)      #生成的图像位置
plt.title(u'exp(-0.5*t)')   #函数名称
ft=np.exp(-0.5*t)   #调用exp函数
plt.plot(t,ft)  #绘制信号图像

plt.subplot(2,2,2)
plt.title(u'exp(0.5*t)')
ft1=np.exp(0.5*t)
plt.plot(t,ft1)

plt.subplot(2,1,2)
plt.title(u'exp(0*t)')
ft2=np.exp(0*t)
plt.plot(t,ft2)
plt.show()