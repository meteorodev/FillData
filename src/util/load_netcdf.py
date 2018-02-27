'''
Created on 24 feb. 2018

@author: Darwin Rosero Vaca <darwin11rv@gmail.com>
'''
'''
import sys
sys.path.append("C:\Program Files\QGIS Pisa\apps\Python27\Lib")

import qgis.core
But be aware that the QGIS Python packages were likely built for a different version of Python. So things might not work smoothly.

Note: QGIS Python plugins are installed here: ~\.qgis2\python\plugins, so you might need to sys.path.append that too.
'''


import numpy as np
from netCDF4 import Dataset as nc
import matplotlib.pyplot as plt
#from mpl_toolkits import basemap as bm


class LoadNetcdf(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        print("just say hello in constructor")
        
    def loadnc(self, ruta):
        ncd = nc(ruta)  # slp por 'sea level pressure'
        print(ncd.variables)
        print(ncd)
        rrda = ncd.variables['prcp'][:]
        nlat = ncd.variables['Y'][:]
        nlong = ncd.variables['X'][:]
        print(len(rrda), " ", len(nlat), " ", len(nlong))
        print(type(rrda), " ", type(nlat), " ", type(nlong))
        print(rrda)
        #map = bm.Basemap(projection='ortho', lat_0=50, lon_0=-100, resolution='l', area_thresh=1000.0)
        #map.drawcoastlines()
         
        plt.show()
        import sys

        for path in sys.path:
            print(path)

lnc = LoadNetcdf()
lnc.loadnc("/home/darwin/Descargas/data.nc")

print("just say hello word")  
