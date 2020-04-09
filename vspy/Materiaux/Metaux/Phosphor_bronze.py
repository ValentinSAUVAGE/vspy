#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:51:12 2020

@author: valentinsauvage
"""

import numpy as np

################################################################################################################    
    
def conductivite_thermique(Temperature):
    
    """ 
    
    Cette fonction permet de determiner la conductivité thermique
    
    Plage de validité : 1K à 300K
    Source : https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20090032058.pdf
    
    Entrée : La température doit être donnée en K
    Sortie : La conductivité thermique est fournie en W/m/K
    
    """  
    
    A = [-10.9482,28.4752,-32.3378,20.9036,-8.05399,1.90329,-0.271774,0.0215998,-7.35095e-4]
    lnk = 0
    for i in range(len(A)):
        lnk = lnk+A[i]*np.log(Temperature)**i
    k = np.exp(lnk)
    return k
    





