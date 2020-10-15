#正弦函数信号
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.unicode_minus']=False    #正常显示负号

x = np.linspace(0, 4 * np.pi, 100)     #x的取值范围
y = np.sin(x)
plt.ylim(-1,1)      #纵轴y的取值范围
plt.subplot(1,2,1)      #生成的图像位置
plt.title(r'$f(x)=sin(x)$')   #函数名称
plt.plot(x,y)  #绘制信号图像

x1=[t*0.5*np.pi for t in x]
y1=np.sin(x1)
plt.subplot(1,2,2)
plt.title(r'$f(x)=sin(\frac{1}{2} \pi x)$')
plt.plot(x1,y1)

plt.show()