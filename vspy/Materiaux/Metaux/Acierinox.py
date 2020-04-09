#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Created on Mon Feb 18 17:25:52 2019 - @author: valentinsauvage """

# Ce programme compile plein de fonctions 
# Constantes à importer
import numpy as np
import warnings
warnings.filterwarnings("ignore")
np.set_printoptions(precision=20)


def conductivite_thermique(Temperature):
    
    """ 
    
    Cette fonction permet de determiner la conductivité thermique du matériau
    
    Plage de validité : 0.1 à 10K
    Source :
        
    Entrée : Temperature en  K
    Sortie : La conductivité thermique sera fournie en W/m/K
    
    Remarque : 
     
    """  
    if Temperature<10:
        if Temperature > 0.1:
            A = 1e-3
            B = 0.92
            
    
    Lambda = A*Temperature**B 
    return Lambda


