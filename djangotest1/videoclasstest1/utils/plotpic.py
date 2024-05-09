# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# fig = plt.figure()
# ax = Axes3D(fig,auto_add_to_figure=False)
# fig.add_axes(ax)
# # P2 = np.arange(0, 40, 0.1)
# P2 = [1,5,11,19,29,41]
# T = np.arange(0, 120, 0.1)
# G = np.arange(0, 2.5, 0.1)
# Y ,Time = np.meshgrid( G,T)
# # Z1  =  (1*Time+20)/((Time+1)**Y)
# Z2  =  (5+20)/((Time+1)**Y)
# # Z3  =  (11*Time+20)/((Time+1)**Y)
# Z4  =  (19+20)/((Time+1)**Y)
# # Z5  =  (29*Time+20)/((Time+1)**Y)
# Z6  =  (41+20)/((Time+1)**Y)
#
# plt.xlabel('Time')
# plt.ylabel('G')
# # plt.title("得分100的个体10日内不同G对W的影响")
# # ax.plot_surface(Time, Y, Z1, rstride=1, cstride=1, cmap='rainbow')
# ax.plot_surface(Time, Y, Z2, rstride=1, cstride=1,)
# # ax.plot_surface(Time, Y, Z3, rstride=1, cstride=1, cmap='rainbow')
# # ax.plot_surface(Time, Y, Z4, rstride=1, cstride=1, )
# # ax.plot_surface(Time, Y, Z5, rstride=1, cstride=1, cmap='rainbow')
# ax.plot_surface(Time, Y, Z6, rstride=1, cstride=1, cmap='rainbow')


# plt.show()

import numpy as np
import matplotlib.pyplot as plt
#
# ax1 = plt.figure(111)

x = np.arange(0, 120 ,0.1)
# y1 = (1+20) / (x + 1)**0.8
y2 = (5+20) / (x + 1)**0.5
y3 = (11+20) / (x + 1)**0.5
y4 = (19+20) / (x + 1)**0.5
y5 = (39+20) / (x + 1)**0.5
# y6 = (41+20) / (x + 1)0*1.8
y7 = (85+20) / (x + 1)**0.5



# plt.plot(x,y1,linewidth=1.5, linestyle="-",label = 'G=1.9')
plt.plot(x,y2,linewidth=1.5, linestyle="-",label = 'P=1')
# plt.plot(x,y3,linewidth=1.5, linestyle="-",label =P'G=1.6')
plt.plot(x,y4,linewidth=1.5, linestyle="-",label = 'P=19')
plt.plot(x,y5,linewidth=1.5, linestyle="-",label = 'P=29')
# plt.plot(x,y6,linewidth=1.5, linestyle="-",label = 'P=41')
plt.plot(x,y7,linewidth=1.5, linestyle="-",label = 'P=55')

plt.legend(loc='upper left')
plt.xlabel('Time')
plt.ylabel('W')
plt.title('G=0.5')
plt.ylim(0,20)
plt.show()


# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# from pylab import *
# from matplotlib import pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
# #
#
# x = np.arange(0, 3, 0.01)
# y = np.sin(x)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("正弦函数")
# plt.plot(x, y)
# plt.show()
#
# plot(
#     (p - 1) / (t + 2)^1.8,
#     (p - 1) / (t + 2)^0.5,
#     (p - 1) / (t + 2)^2.0
# ) where t=0..24, p=10
