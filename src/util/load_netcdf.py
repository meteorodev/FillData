'''
Created on 24 feb. 2018

@author: Darwin Rosero Vaca <darwin11rv@gmail.com>
'''

import numpy as np
import netCDF4 as nc
from scipy.io import netcdf
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
        
    def loadnc(self,ruta):
        slp = nc.Dataset(ruta) #slp por 'sea level pressure'
        
        print(slp)
        #f=netcdf.netcdf_file(ruta,'r')
        #for v in f.variables:
        #    print(v)

lnc=LoadNetcdf()
lnc.loadnc("/home/darwin/Descargas/data.nc")

print("just say hello word")  