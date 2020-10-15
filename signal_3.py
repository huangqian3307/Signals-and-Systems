#一般复指数信号
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']  #标题可以出现中文
plt.rcParams['axes.unicode_minus']=False    #正常显示负号

t=np.linspace(-3.0,3.0,1000)
plt.ylim(0,4)
f=2*np.exp((complex(-0.5,8))*t)
plt.subplot(221)
plt.title(u'实部')
plt.plot(t,np.real(f))
plt.subplot(222)
plt.title(u'虚部')
plt.plot(t,np.imag(f))
plt.subplot(223)
plt.title(u'绝对值')
plt.plot(t,np.abs(f))
plt.subplot(224)
plt.title(u'angle')
plt.plot(t,np.angle(f))
plt.show()