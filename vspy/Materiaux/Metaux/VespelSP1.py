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
    
    Plage de validité : de 1.4 à 4.5 K
    Source : 
        
    Entrée : Temmperature en  K
    Sortie : La conductivité thermique sera fournie en W/m/K
    
    Remarque : 
     
    """  
    
    if Temperature<4.5:
        if Temperature > 1.4:
            A = 1.7e-5
            B = 1.18
            
    Lambda = A*Temperature**B 
    return Lambda



