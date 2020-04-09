#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Created on Mon Feb 18 17:25:52 2019 - @author: valentinsauvage """

# Ce programme compile plein de fonctions 
# Constantes à importer
import numpy as np
import warnings
warnings.filterwarnings("ignore")
np.set_printoptions(precision=20)
from scipy.interpolate import interp1d



def conductivite_thermique(Temperature):
    
    """ 
    
    Cette fonction permet de determiner la conductivité thermique du matériau
    
    Plage de validité : de 0.05 K à 2K
    Source : 
        Thermal Conductivity of Selected Materials
        R. W. Powell,* C. Y. Ho,* and P. E. Liley*
    
    Entrée : Temmperature en  K
    Sortie : La conductivité thermique sera fournie en W/m/K
    
    Remarque : copper 84%, manganese 12%, nickel 4% by weight
     
    """  
    
    Temp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,25,30,35,40,45,50,60,70,80,90,100,150,200,250,273,300,350]
    Lambda = [0,0.0007,0.0018,0.0031,0.0046,0.0062,0.0078,0.0095,0.0111,0.0128,0.0145,0.0162,0.0180,0.0197,0.0215,0.0232,0.0250,0.0285,0.0322,0.0410,0.0497,0.0583,0.067,0.075,0.082,0.09097,0.110,0.120,0.127,0.133,0.156,0.172,0.193,0.206,0.222,0.250]
    
    f = interp1d(Temp, Lambda)
    
    return f(Temperature)*100
