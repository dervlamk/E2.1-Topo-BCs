import os
import sys
import xarray as xr
import netCDF4 as nc
import numpy as np
import metpy.calc as mp
from datetime import datetime


#############################

def windSpd(u,v):
    """
    Calculate wind speed from u and v components
    """
   windSpeed=np.sqrt(u**2 + v**2)
   return windSpeed


def froude(N,h,Uspd):
    """
    Calculate Froude value
    """
   fr=(N*h)/Uspd
   return fr

def convergence(u,v):
    """
    Calculate convergence from components
    """
    dudx, _ = mp.geospatial_gradient(u)
    _, dvdy = mp.geospatial_gradient(v)
    return(-(dudx + dvdy))