#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Created on Fri Feb 22 09:33:56 2019 - @author: valentinsauvage """

# Ce programme compile plein de fonctions calculant et regroupant les propriétés de l'helium 4


# Fonctions à importer
import VSAUVAGE.catalogue_fonctions as cf
# Constantes à importer
import VSAUVAGE.catalogue_constantes as cc
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

        
""" Constantes de l'helium 4 """

# Masse de l'atome d'helium 4 
masse = 2*(cc.m_electron + cc.m_proton + cc.m_neutron)

# Masse atomique de l'atome d'helium 4 (from https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=)
masse_atomique = 4.00260325412  # uma

################################################################################################################

def viscosite_dynamique(T):
    
    """ 
    
    Cette fonction permet de determiner la viscosite dynamique de l'Helium 4 en fonction de la Temperature
    
    Plage de validité : ?
    Source : Fonction python Gerard Vermeulen
    
    Entrée : La température doit être donnée en K
    Sortie : La viscosité dynamique est fournie en Pa.s 
     
    """
    
    return 5.18e-7 * T ** 0.64

################################################################################################################

def impedance(n_dot, P_in, P_out, T):
    
    """ 
    
    Cette fonction permet de determiner l'impedance produit par un capillaire sous un flux d'helium 4
    
    Plage de validité : Toujours
    Source : Documentation à compléter
    
    Entrée : La température doit être donnée en K
             La pression doit être donnée en Pa
             Le débit doit être donné en mol/s
    Sortie : L'impédance est fournie en ?
     
    """
    
    return (P_in ** 2 - P_out ** 2) / (2 * n_dot * cc.R * T * viscosite_dynamique(T))

################################################################################################################

def diametre_capillaire(V_dot,P_in,P_out,T,L):
    
    """ 
    
    Cette fonction permet de determiner le diametre d'un capillaire mesuré sous helium 4
    
    Plage de validité : Toujours
    Source : Documentation à compléter
    
    Entrée : La température doit être donnée en K
             La pression doit être donnée en Pa
             Le débit doit être donné en m3/s
    Sortie : Le diamètre est fournie en m
     
    """
    
    return (128 * L / (np.pi * impedance(cf.debit_molaire(V_dot,T), P_in, P_out,T))) ** 0.25

################################################################################################################

def permeabilite(V_dot,P_in,P_out,T,L,diam):

    """ 
    
    Cette fonction permet de determiner la perméabilité d'un poreux mesuré sous helium 4
    
    Plage de validité : Toujours
    Source : Documentation à compléter
    
    Entrée : La température doit être donnée en K
             La pression doit être donnée en Pa
             Le débit doit être donné en m3/s
    Sortie : Le diamètre est fournie en m
     
    """    
    
    return L/cf.surface(diam)/impedance(cf.debit_molaire(V_dot,T), P_in, P_out,T)
    
################################################################################################################    

def densite_liquide(T):

    """ 
    
    Cette fonction permet de determiner la densité de l'helium 4 liquide en fonction de sa température
    
    Plage de validité : Entre 0.8 K et 5.1 K
    Source : Documentation à compléter
    
    Entrée : La température doit être donnée en K
    Sortie : La densité est fournie en kg/m3
     
    """    

    temperature_0dot8to5dot1 = [0.8 , 0.85, 0.9 , 0.95, 1.  , 1.05, 1.1 , 1.15, 1.2 , 1.25, 1.3 ,
       1.35, 1.4 , 1.45, 1.5 , 1.55, 1.6 , 1.65, 1.7 , 1.75, 1.8 , 1.85,
       1.9 , 1.95, 2.  , 2.05, 2.1 , 2.15, 2.2 , 2.25, 2.3 , 2.35, 2.4 ,
       2.45, 2.5 , 2.55, 2.6 , 2.65, 2.7 , 2.75, 2.8 , 2.85, 2.9 , 2.95,
       3.  , 3.05, 3.1 , 3.15, 3.2 , 3.25, 3.3 , 3.35, 3.4 , 3.45, 3.5 ,
       3.55, 3.6 , 3.65, 3.7 , 3.75, 3.8 , 3.85, 3.9 , 3.95, 4.  , 4.05,
       4.1 , 4.15, 4.2 , 4.25, 4.3 , 4.35, 4.4 , 4.45, 4.5 , 4.55, 4.6 ,
       4.65, 4.7 , 4.75, 4.8 , 4.85, 4.9 , 4.95, 5.  , 5.05, 5.1]
    
    densite_liquide_0dot8to5dot1 = [145.2 , 145.2 , 145.2 , 145.2 , 145.2 , 145.2 , 145.2 , 145.2 ,
       145.2 , 145.2 , 145.2 , 145.2 , 145.2 , 145.2 , 145.2 , 145.3 ,
       145.3 , 145.3 , 145.3 , 145.4 , 145.4 , 145.5 , 145.5 , 145.6 ,
       145.7 , 145.7 , 145.9 , 146.  , 146.1 , 146.  , 145.9 , 145.7 ,
       145.5 , 145.3 , 145.  , 144.7 , 144.4 , 144.1 , 143.8 , 143.4 ,
       143.  , 142.6 , 142.2 , 141.8 , 141.4 , 140.9 , 140.4 , 139.9 ,
       139.4 , 138.9 , 138.4 , 137.8 , 137.3 , 136.7 , 136.1 , 135.5 ,
       134.8 , 134.2 , 133.5 , 132.8 , 132.  , 131.3 , 130.5 , 129.7 ,
       128.9 , 128.1 , 127.2 , 126.3 , 125.4 , 124.4 , 123.4 , 122.3 ,
       121.3 , 120.1 , 118.9 , 117.7 , 116.3 , 114.9 , 113.5 , 111.9 ,
       110.2 , 108.3 , 106.3 , 104.  , 101.4 ,  98.4 ,  94.71]

    densite_liquide_0dot8to5dot1_fun = np.poly1d(cf.Fit_courbe(temperature_0dot8to5dot1,densite_liquide_0dot8to5dot1,20))

    if 0.8 <= T and T <= 5.1:
        return densite_liquide_0dot8to5dot1_fun(T)
    

################################################################################################################    

def pression_liquide(T):

    """ 
    
    Cette fonction permet de determiner la pression de l'helium 4 liquide en fonction de sa température
    
    Plage de validité : Entre 0.8 K et 5.1 K
    Source : Documentation à compléter
    
    Entrée : La température doit être donnée en K
    Sortie : La pression est fournie en Pa
     
    """    

    temperature_0dot8to5dot1 = [0.8 , 0.85, 0.9 , 0.95, 1.  , 1.05, 1.1 , 1.15, 1.2 , 1.25, 1.3 ,
       1.35, 1.4 , 1.45, 1.5 , 1.55, 1.6 , 1.65, 1.7 , 1.75, 1.8 , 1.85,
       1.9 , 1.95, 2.  , 2.05, 2.1 , 2.15, 2.2 , 2.25, 2.3 , 2.35, 2.4 ,
       2.45, 2.5 , 2.55, 2.6 , 2.65, 2.7 , 2.75, 2.8 , 2.85, 2.9 , 2.95,
       3.  , 3.05, 3.1 , 3.15, 3.2 , 3.25, 3.3 , 3.35, 3.4 , 3.45, 3.5 ,
       3.55, 3.6 , 3.65, 3.7 , 3.75, 3.8 , 3.85, 3.9 , 3.95, 4.  , 4.05,
       4.1 , 4.15, 4.2 , 4.25, 4.3 , 4.35, 4.4 , 4.45, 4.5 , 4.55, 4.6 ,
       4.65, 4.7 , 4.75, 4.8 , 4.85, 4.9 , 4.95, 5. , 5.05, 5.1]
    

    pression_liquide_0dot8to5dot1 = [1.475e+00, 2.914e+00, 5.379e+00, 9.379e+00, 1.557e+01, 2.478e+01,
       3.800e+01, 5.645e+01, 8.148e+01, 1.147e+02, 1.579e+02, 2.129e+02,
       2.820e+02, 3.674e+02, 4.715e+02, 5.970e+02, 7.464e+02, 9.224e+02,
       1.128e+03, 1.366e+03, 1.638e+03, 1.949e+03, 2.299e+03, 2.692e+03,
       3.129e+03, 3.612e+03, 4.141e+03, 4.715e+03, 5.335e+03, 6.005e+03,
       6.730e+03, 7.512e+03, 8.354e+03, 9.258e+03, 1.023e+04, 1.126e+04,
       1.237e+04, 1.355e+04, 1.481e+04, 1.614e+04, 1.755e+04, 1.905e+04,
       2.063e+04, 2.229e+04, 2.405e+04, 2.589e+04, 2.784e+04, 2.987e+04,
       3.201e+04, 3.425e+04, 3.659e+04, 3.904e+04, 4.159e+04, 4.426e+04,
       4.704e+04, 4.994e+04, 5.296e+04, 5.609e+04, 5.935e+04, 6.274e+04,
       6.625e+04, 6.989e+04, 7.366e+04, 7.757e+04, 8.162e+04, 8.581e+04,
       9.014e+04, 9.461e+04, 9.923e+04, 1.040e+05, 1.089e+05, 1.140e+05,
       1.193e+05, 1.247e+05, 1.303e+05, 1.360e+05, 1.419e+05, 1.480e+05,
       1.543e+05, 1.608e+05, 1.674e+05, 1.743e+05, 1.813e+05, 1.886e+05,
       1.960e+05, 2.037e+05, 2.116e+05]

    pression_0dot8to5dot1_fun = np.poly1d(cf.fitting(temperature_0dot8to5dot1,np.log(pression_liquide_0dot8to5dot1)))

    if 0.8 <= T and T <= 5.1:
        return np.exp(pression_0dot8to5dot1_fun(T))
    
################################################################################################################    

def enthalpie_liquide(T):
    
    """ 
    
    Cette fonction permet de determiner l'enthalpie de l'helium 4 liquide en fonction de sa température
    
    Plage de validité : Entre 0.8 K et 5.1 K
    Source : Documentation à compléter
    
    Entrée : La température doit être donnée en K
    Sortie : L'enthalpie est fournie en J/g
     
    """  

    temperature_0dot8to2dot2 = [0.8 , 0.85, 0.9 , 0.95, 1.  , 1.05, 1.1 , 1.15, 1.2 , 1.25, 1.3 ,
       1.35, 1.4 , 1.45, 1.5 , 1.55, 1.6 , 1.65, 1.7 , 1.75, 1.8 , 1.85,
       1.9 , 1.95, 2.  , 2.05, 2.1 , 2.15, 2.2]
    
    temperature_2dot2to5dot1 = [2.2 , 2.25, 2.3 , 2.35, 2.4 ,
       2.45, 2.5 , 2.55, 2.6 , 2.65, 2.7 , 2.75, 2.8 , 2.85, 2.9 , 2.95,
       3.  , 3.05, 3.1 , 3.15, 3.2 , 3.25, 3.3 , 3.35, 3.4 , 3.45, 3.5 ,
       3.55, 3.6 , 3.65, 3.7 , 3.75, 3.8 , 3.85, 3.9 , 3.95, 4.  , 4.05,
       4.1 , 4.15, 4.2 , 4.25, 4.3 , 4.35, 4.4 , 4.45, 4.5 , 4.55, 4.6 ,
       4.65, 4.7 , 4.75, 4.8 , 4.85, 4.9 , 4.95, 5.  , 5.05, 5.1 ]

    enthalpie_liquide_0dot8to2dot2 = [1.877e-03, 3.275e-03, 5.356e-03, 8.381e-03, 1.268e-02, 1.865e-02,
       2.676e-02, 3.759e-02, 5.176e-02, 7.001e-02, 9.315e-02, 1.221e-01,
       1.579e-01, 2.015e-01, 2.543e-01, 3.174e-01, 3.923e-01, 4.804e-01,
       5.836e-01, 7.034e-01, 8.422e-01, 1.002e+00, 1.186e+00, 1.398e+00,
       1.642e+00, 1.926e+00, 2.261e+00, 2.671e+00, 3.090e+00]
                          
    enthalpie_liquide_2dot2to5dot1 = [ 3.090e+00, 3.270e+00,
       3.418e+00, 3.552e+00, 3.678e+00, 3.801e+00, 3.922e+00, 4.040e+00,
       4.161e+00, 4.284e+00, 4.408e+00, 4.534e+00, 4.662e+00, 4.791e+00,
       4.923e+00, 5.058e+00, 5.195e+00, 5.337e+00, 5.483e+00, 5.633e+00,
       5.787e+00, 5.945e+00, 6.108e+00, 6.276e+00, 6.448e+00, 6.625e+00,
       6.806e+00, 6.992e+00, 7.184e+00, 7.380e+00, 7.581e+00, 7.787e+00,
       7.998e+00, 8.215e+00, 8.437e+00, 8.665e+00, 8.899e+00, 9.140e+00,
       9.387e+00, 9.640e+00, 9.901e+00, 1.017e+01, 1.045e+01, 1.073e+01,
       1.102e+01, 1.133e+01, 1.164e+01, 1.197e+01, 1.231e+01, 1.267e+01,
       1.304e+01, 1.343e+01, 1.385e+01, 1.429e+01, 1.476e+01, 1.528e+01,
       1.585e+01, 1.649e+01, 1.726e+01]


    enthalpie_liquide_0dot8to2dot2_fun = np.poly1d(cf.fitting(temperature_0dot8to2dot2, np.log(enthalpie_liquide_0dot8to2dot2)))
    enthalpie_liquide_2dot2to5dot1_fun = np.poly1d(cf.fitting(temperature_2dot2to5dot1, np.log(enthalpie_liquide_2dot2to5dot1)))


    if 0.8 <= T and T <= 2.2:
        return np.exp(enthalpie_liquide_0dot8to2dot2_fun(T))
        
    if 2.2 < T and T <= 5.1:
        return np.exp(enthalpie_liquide_2dot2to5dot1_fun(T))


################################################################################################################    

def entropie_liquide(T):
    
    """ 
    
    Cette fonction permet de determiner l'entropie de l'helium 4 liquide en fonction de sa température
    
    Plage de validité : Entre 0.8 K et 5.1 K
    Source : Documentation à compléter
    
    Entrée : La température doit être donnée en K
    Sortie : L'entropie est fournie en J/g/K
     
    """  

    temperature_0dot8to2dot2 = [0.8 , 0.85, 0.9 , 0.95, 1.  , 1.05, 1.1 , 1.15, 1.2 , 1.25, 1.3 ,
       1.35, 1.4 , 1.45, 1.5 , 1.55, 1.6 , 1.65, 1.7 , 1.75, 1.8 , 1.85,
       1.9 , 1.95, 2.  , 2.05, 2.1 , 2.15, 2.2]
    
    temperature_2dot2to5dot1 = [2.2 , 2.25, 2.3 , 2.35, 2.4 ,
       2.45, 2.5 , 2.55, 2.6 , 2.65, 2.7 , 2.75, 2.8 , 2.85, 2.9 , 2.95,
       3.  , 3.05, 3.1 , 3.15, 3.2 , 3.25, 3.3 , 3.35, 3.4 , 3.45, 3.5 ,
       3.55, 3.6 , 3.65, 3.7 , 3.75, 3.8 , 3.85, 3.9 , 3.95, 4.  , 4.05,
       4.1 , 4.15, 4.2 , 4.25, 4.3 , 4.35, 4.4 , 4.45, 4.5 , 4.55, 4.6 ,
       4.65, 4.7 , 4.75, 4.8 , 4.85, 4.9 , 4.95, 5.  , 5.05, 5.1 ]
    
    entropie_liquide_0dot8to2dot2 = [4.713e-03, 6.392e-03, 8.748e-03, 1.198e-02, 1.634e-02, 2.210e-02,
       2.956e-02, 3.905e-02, 5.096e-02, 6.566e-02, 8.357e-02, 1.051e-01,
       1.308e-01, 1.610e-01, 1.962e-01, 2.370e-01, 2.839e-01, 3.374e-01,
       3.981e-01, 4.666e-01, 5.437e-01, 6.302e-01, 7.270e-01, 8.356e-01,
       9.578e-01, 1.096e+00, 1.256e+00, 1.447e+00, 1.638e+00]

    entropie_liquide_2dot2to5dot1 =     [1.638e+00, 1.717e+00,
       1.780e+00, 1.835e+00, 1.886e+00, 1.934e+00, 1.980e+00, 2.024e+00,
       2.068e+00, 2.112e+00, 2.155e+00, 2.198e+00, 2.240e+00, 2.282e+00,
       2.324e+00, 2.366e+00, 2.408e+00, 2.451e+00, 2.494e+00, 2.537e+00,
       2.581e+00, 2.625e+00, 2.670e+00, 2.715e+00, 2.760e+00, 2.806e+00,
       2.852e+00, 2.899e+00, 2.946e+00, 2.994e+00, 3.042e+00, 3.091e+00,
       3.140e+00, 3.189e+00, 3.239e+00, 3.290e+00, 3.341e+00, 3.392e+00,
       3.444e+00, 3.497e+00, 3.551e+00, 3.605e+00, 3.661e+00, 3.717e+00,
       3.775e+00, 3.833e+00, 3.893e+00, 3.955e+00, 4.018e+00, 4.084e+00,
       4.151e+00, 4.222e+00, 4.296e+00, 4.375e+00, 4.458e+00, 4.549e+00,
       4.649e+00, 4.763e+00, 4.898e+00]
    
    entropie_liquide_0dot8to2dot2_fun = np.poly1d(cf.fitting(temperature_0dot8to2dot2, np.log(entropie_liquide_0dot8to2dot2)))
    entropie_liquide_2dot2to5dot1_fun = np.poly1d(cf.fitting(temperature_2dot2to5dot1, np.log(entropie_liquide_2dot2to5dot1)))

    if 0.8 <= T and T <= 2.2:
        return np.exp(entropie_liquide_0dot8to2dot2_fun(T))
        
    if 2.2 < T and T <= 5.1:
        return np.exp(entropie_liquide_2dot2to5dot1_fun(T))


################################################################################################################    

def debit_pf(T,Q,unit):

    """ 
    
    Cette fonction permet de determiner le débit d'helium 4 liquide en sortie de pompe à effet fontaine
    
    Plage de validité : 1 K à 2.177 K
    Source : Documentation à compléter
    
    Entrée : La température doit être donnée en K
             La puissance doit être donnée en W
             Le paramètre unité est à choisir entre 'mole' ou 'g'
    Sortie : Le débit est fourni en mol/s ou en g/s suivant le choix
     
    """  
    
    if unit in ['mol','mole']:
        return masse_atomique*Q/T/entropie_liquide(T)

    if unit in ['g','gramme']:
        return Q/T/entropie_liquide(T)
    
    ################################################################################################################    

def densite_PVS(T):

    """ 
    
    Cette fonction permet de determiner la densité de l'helium 4
    
     
    """  
    

    
    





