#V.Ruiz
#2014-10-14
#Homework 2, problem 5.a
#Funtion to read etopo5
# source data: http://www.nio.org/userfiles/file/datainfo/global_merged5.txt

import numpy as np

def read_etopo5(filename):
    """
    Reads the world topography/bathymetry from the ETOPO5 surface dataset txt file
    Returns x,y,z as arrays
    """
    f=open(filename)
    lines= f.readlines()
    f.close()

    lon=[]
    lat=[]
    depth=[]
    for line in lines:
        l=line.split()
        lon.append(float(l[0]))
        lat.append(float(l[1]))
        depth.append(float(l[2]))
    x=np.asarray(lon)
    y=np.asarray(lat)
    z=np.asarray(depth)
    return x,y,z


    




