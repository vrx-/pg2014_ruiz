#V.Ruiz
#2014-10-14
#Homework 2, problem 5.b
#World map plot script
#uses read_etopo5.py


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

from read_etopo5 import read_etopo5

x,y,z= read_etopo5('global_merged5.txt')
dx=len(np.where(x==x[0])[0])
dy=len(np.where(y==y[0])[0])
x=x.reshape(dx,dy)
y=y.reshape(dx,dy)
z=z.reshape(dx,dy)

m = Basemap(projection='mill',
            llcrnrlon=x.min(), 
            urcrnrlon=x.max(), 
            llcrnrlat=y.min(), 
            urcrnrlat=y.max(),
            resolution='c')
xx,yy=m(x,y)

fig=plt.figure()
ax = fig.add_subplot(111)
pcm=ax.pcolormesh(xx,yy,z, cmap=plt.cm.seismic, vmin=-10000., vmax=10000.)
#pcm=ax.pcolormesh(xx,yy,z, vmin=-10000., vmax=10000.)
m.drawparallels(np.arange(-80,80,20), labels=[0,0,1,0])
m.drawmeridians(np.arange(-180, 180, 60), labels=[1,0,0,1])
cb=plt.colorbar(pcm)
cb.set_label('Elevation in m', rotation=270)
cont=ax.contour(xx,yy,z,levels=np.arange(-1000, 0, 1000), 
                linewidths=np.arange(.5, 4, .5), colors='k')
ax.set_title('World topography/bathymetry - ETOPO5')

plt.show()
