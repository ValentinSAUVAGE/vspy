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
    
    Plage de validité : de 0.05 K à 2K
    Source : "Thermal conductivity of some common cryostat materials between 0.05 and 2 K " from J.R. Olson, 1992
    
    Entrée : Temmperature en  K
    Sortie : La conductivité thermique sera fournie en W/m/K
     
    """  
    
    A = 170e-4
    B = 2.65
    Lambda = A*Temperature**B 
    return Lambda
