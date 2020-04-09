#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Created on Mon Feb 18 17:25:52 2019 - @author: valentinsauvage """

# Ce programme compile plein de fonctions 
# Constantes à importer
import numpy as np
import warnings
warnings.filterwarnings("ignore")
np.set_printoptions(precision=20)


def Puissance(Surface,Longueur,Tmin,Tmax):
    
    """ 
    
    Cette fonction permet de determiner la puissance thermique mise en jeu
    
    Plage de validité : de 300 K à 1K
    Source : pres_ProprieteCryo_JPT.pdf
    
    Entrée : La surface en m2
             La longueur en m
             Les températures en K
    Sortie : La puissance sera fournie en W
     
    """  
    

    