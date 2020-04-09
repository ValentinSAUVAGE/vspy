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
    
    Plage de validité :  1.8 à 40 K
    Source : 
        
    Entrée : Temmperature en  K
    Sortie : La conductivité thermique sera fournie en W/m/K
    
    Remarque : 
     
    """  
    
    if Temperature<40:
        if Temperature > 5:
            A = 1.9e-5
            B = 2
    if Temperature<4:
        if Temperature > 1.8:
            A = 2.1e-5
            B = 1.6
            
    Lambda = A*Temperature**B 
    return Lambda



