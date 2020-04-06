#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Created on Mon Feb 18 17:25:52 2019 - @author: valentinsauvage """

# Ce programme compile plein de fonctions 
# Constantes à importer
import VSAUVAGE.catalogue_constantes as cc
import numpy as np
import warnings
warnings.filterwarnings("ignore")
np.set_printoptions(precision=20)
import random
from scipy import interpolate
import matplotlib.pyplot as plt

################################################################################################################    

def fit_courbe(Res_etalon,Temp_etalon,Deg_max):
    
    # Détermination d'un point de cision minimisant l'erreur sur les polynômes
    
    diff = []

    
    for ind_split in range(1,len(Res_etalon)-1):
        # Construction de l'erreur maximale
        diff.append(max(error(np.log(Res_etalon[:ind_split]),np.log(Temp_etalon[:ind_split]),Deg_max),error(np.log(Res_etalon[ind_split:]),np.log(Temp_etalon[ind_split:]),Deg_max)))
        
    # +1 car position selon i qui commence à 1 au lieu de 0
    separation = [j for j,x in enumerate(diff) if x == min(diff)][0]+1
    
    
    # Détermination du premier polynôme (concernant la première partie de la courbe) en minimisant l'erreur
    
    diff = []
    
    for i in range(1,Deg_max):
        # Détermination du polynômef(log(Res))= log(T) de degrès i
        f = np.poly1d(np.polyfit(np.log(Res_etalon[:separation]),np.log(Temp_etalon[:separation]),i))
        # Calcul de l'erreur maximale présente dans la création de ce polynôme de degré i
        diff.append(max((Temp_etalon[:separation]-np.exp(f(np.log(Res_etalon[:separation]))))/Temp_etalon[:separation]))
        
    optimal = [j for j,x in enumerate(diff) if x == min(diff)]
    Fit1 = np.poly1d(np.polyfit(np.log(Res_etalon[:separation]),np.log(Temp_etalon[:separation]),optimal[0]))
    
    
    # Détermination du second polynôme (concernant la seconde partie de la courbe) en minimisant l'erreur
    
    diff = []
    for i in range(1,Deg_max):
        # Détermination du polynômef(log(Res))= log(T) de degrès i
        f = np.poly1d(np.polyfit(np.log(Res_etalon[separation:]),np.log(Temp_etalon[separation:]),i))
        # Calcul de l'erreur maximale présente dans la création de ce polynôme de degré i
        diff.append(max((Temp_etalon[separation:]-np.exp(f(np.log(Res_etalon[separation:]))))/Temp_etalon[separation:]))
        
    optimal = [j for j,x in enumerate(diff) if x == min(diff)]
    Fit2 = np.poly1d(np.polyfit(np.log(Res_etalon[separation:]),np.log(Temp_etalon[separation:]),optimal[0]))
    
    return Fit1,Fit2,Res_etalon[separation]

################################################################################################################    

def debit_molaire(Debit_volumique,Temperature,Pression):

    """ 
    
    Cette fonction permet de determiner le debit molaire d'un flux
    
    Plage de validité : Toujours
    Source : Documentation à compléter
    
    Entrée : La pression doit être donnée en Pa
             Le débit doit être donné en m3/s
             La température doit être donnée en K
    Sortie : Le débit molaire sera fourni en mol/s
     
    """  
    debit = Debit_volumique * Pression / (cc.R * Temperature)
    return debit

################################################################################################################    

def debit_sscmtosi(Debit_sccm,Temperature,Pression):

    """ 
    
    Cette fonction permet de convertir un débit sccm en débit SI
    
    Plage de validité : Toujours
    Source : Documentation à compléter
    
    Entrée : Debit_sccm doit être donnée en cm3/min
    Sortie : Debit_si sera fourni en m3/s
     
    """  
    
    Debit_si = Debit_sccm*1e-6/60
    return Debit_si
        
################################################################################################################    

def section(Diametre):

    """ 
    
    Cette fonction permet de déterminer la surface à partir d'un diamètre
    
    Plage de validité : Toujours
    Source : Géométrie
    
    Entrée : Diametre en m
    Sortie : Surface en m2
     
    """  
    
    return np.pi*Diametre**2/4

################################################################################################################    

def error(x,y,deg):
    
    """ 
    
    Cette fonction permet de déterminer l'erreur minimale possible lors d'un 
    fit polynomial pour un polynôme de degré 1 à "Deg_max"
    
    Plage de validité : Toujours
    
    Entrée : x et y de même taille
             deg un entier
     
    """  
    
    #   Initialisation de la variable "diff" 
    diff = []
    #   Pour un degré allant de 1 à "Deg_max", on va déterminer l'erreur maximale possible 
    for degre in range(1,deg):
        #   La fonction f représente le polynôme pour fiter la courbe
        f = np.poly1d(np.polyfit(x,y,degre))
        #   On calcule l'erreur relative associée au fit 
        diff.append(max((y-f(x))/y)*100)
        #   La fonction retourne l'erreur minimale possible pour un certain degré
    return min(diff)

################################################################################################################    

def puissance_conduction(Surface,Longueur,T_chaud,T_froid,a,b):
    
    
    """ 
    
    Cette fonction permet de déterminer la puissance thermique à l'autre extermité 
    
    
    Plage de validité : Toujours
    
    Source : thèse de Florian Martin, P121
    
    Entrée :
        T_chaud en K 
        T_froid en K
        Surface en m2
        Longueur en m
        Les paramètres a et b du matériau définissant sa conductivité thermique
        
    Sortie :
        Puissance en W
                
     
    """  
    
    Puissance = Surface/Longueur*(T_chaud**(b+1)-T_froid**(b+1))*a/(b+1)
    return Puissance
    
################################################################################################################    

def temperature_conduction(Surface,Longueur,Puissance,T_chaud,a,b):
    
    
    """ 
    
    Cette fonction permet de déterminer la temperature d'un materiau à un  point donné 
    connaissant ses propriétés, la puissance thermique qui le traverse et la temperature à l'une des extrémité
    
    Plage de validité : Toujours
    
    Source : thèse de Florian Martin, P121
    
    Entrée :
        T_chaud en K 
        Puissance en W
        Surface en m2
        Longueur en m
        Les paramètres a et b du matériau définissant sa conductivité thermique
        
    Sortie :
        Temperature en K
    """  
    
    Temperature = (T_chaud**(b+1)-Puissance*Longueur/Surface*(b+1)/a)**(1/(b+1))
    return Temperature


################################################################################################################    

def reynolds(Vitesse,Dimension,Viscosite_cinematique):
    
    """ 
    
    Cette fonction détermine le nombre de Reynolds d'un  écoulement
    
    
    Plage de validité : Toujours
    
    Entrée : Vitesse en m/s 
             Dimension 'caractéristique' en m
                 Tube -> Diamètre
             Viscosite_cinematique en m2/s
    Sortie : Reynolds sans unité
     
    """  

    Re = Vitesse*Dimension/Viscosite_cinematique
    return Re

################################################################################################################    

def permeabilite(Debit_volumique,Pression_entree,Pression_sortie,Viscosite_dynamique,Longueur,Section):
    
    """ 
    
    Cette fonction détermine la permeabilite d'un materiau
    
    
    Plage de validité : Ecoulement laminaire et régime non moléculaire
    
    Entrée : Debit_volumique en m3/s 
             Pression_entree en Pa
             Pression_sortie en Pa
             Viscosite_dynamique en kg/m/K
             Longueur en m
             Section en m2
    Sortie : k en m2
     
    """  

    k = 2*Debit_volumique*Pression_sortie*Viscosite_dynamique*Longueur/(Section*(Pression_entree**2-Pression_sortie**2))
    return k


################################################################################################################    

def impedance_tube(Diametre,Longueur,Viscosite_dynamique):
    
    """ 
    
    Cette fonction détermine l'impedance hydraulique dans un tube
    
    
    Plage de validité : Regime laminaire
    
    Entrée : Diametre en m
             Longueur en m
             Viscosite_dynamique en Pa/s
    Sortie : z en ...
     
    """  

    z = 128*Longueur*Viscosite_dynamique/np.pi/Diametre**4
    return z
 

################################################################################################################    
    
def pression_entree_tube(Debit_molaire,Temperature,Viscosite_dynamique,Pression_sortie,Longueur,Diametre):
    
    """ 
    
    Cette fonction détermine la pression en entree d'un fluide dans un tube
    
    
    Plage de validité : 
    
    Entrée : Debit_molaire en mol/s
             Temperature en K
             Impedance en 1/m
             Viscosite_dynamique en Pa/s
             Pression_sortie en Pa
             Longueur en m
             Diametre en m
    Sortie : Pression_entree en Pa
     
    """  

    Pression_entree = (2*impedance_tube(section(Diametre),Longueur)*Temperature*cc.R*Debit_molaire*Viscosite_dynamique+Pression_sortie**2)**0.5
    
    return Pression_entree


################################################################################################################    
    
def pression_sortie_tube(Debit_molaire,Temperature,Viscosite_dynamique,Pression_entree,Longueur,Diametre):
    
    """ 
    
    Cette fonction détermine la pression en entree d'un fluide dans un tube
    
    
    Plage de validité : 
    
    Entrée : Debit_molaire en mol/s
             Temperature en K
             Impedance en 1/m
             Viscosite_dynamique en Pa/s
             Pression_entree en Pa
             Longueur en m
             Diametre en m
    Sortie : Pression_sortie en Pa
     
    """  

    Pression_sortie = (-2*impedance_tube(section(Diametre),Longueur)*Temperature*cc.R*Debit_molaire*Viscosite_dynamique+Pression_entree**2)**0.5
    
    return Pression_sortie

################################################################################################################    
    
def vitesse_radiale_ecoulement(Rayon,Viscosite_dynamique,Pression_entree,Pression_sortie,Longueur,Distance_centre):
    
    """ 
    
    Cette fonction détermine de vitesse d'écoulement radial dans un tube à une distance donné du centre
    
    
    Plage de validité : Flux laminaire
    
    Entrée : Rayon en m
             Viscosite_dynamique en Pa/s
             Pression_entree en Pa
             Pressionb_sortie en Pa
             Longueur en m
             Distance_centre en m
    Sortie : Vitesse en m/s
     
    """  

    Vitesse = Rayon**2/4/Viscosite_dynamique*(abs(Pression_entree-Pression_sortie))/Longueur*(1-Distance_centre**2/Rayon**2)
    
    return Vitesse



################################################################################################################    

def fit_aTb(T1,T2,Power,S_sur_L):

    """ 
    
    Cette fonction détermine les coefficients a et b les plus optimaux sur un intervalle ainsi que l'erreur maximale du fit proposé
    
    Plage de validité : Tout le temps (à tester avec des plages de températures larges )
    
    Entrée :    T1 la température la plus haute
                T2 la température la plus basse
                Power la puissance injectée pour obtenir le couple T1, T2
                S_sur_L une constante correspondant au rapport entre la section et la longueur
    
    Sortie :    a un paramètre en W/m/K2
                b un paramètre sans unité
                erreur un vecteur en Watt
    
     
    """ 
    
    # Définition d'une fenêtre pour la valeur de a
    a_min = 0.02
    a_max = 0.04
    vect_a = np.arange(a_min,a_max,0.00001)
    
    # Définition d'une fenêtre pour la valeur de b
    b_min = 0.9
    b_max = 1.5
    vect_b = np.arange(b_min,b_max,0.001)
    
    # Initialisation de paramètres

    avant = 100
    
    for i in range(len(vect_a)):
        
        a = vect_a[i]
        
        for j in range(len(vect_b)):
            
            b = vect_b[j]
            
            Q1 = S_sur_L*(a/(b+1))*(((T1[0]**(b+1))-(T2[0]**(b+1))))
            Q = Power[0]
            old_erreur = abs((Q1-Q)/Q1)
            
            for n in np.arange(1,len(T1),1):
                Q1 = S_sur_L*(a/(b+1))*(((T1[n]**(b+1))-(T2[n]**(b+1))))
                Q = Power[n]
                erreur = abs((Q1-Q)/Q1)

                if old_erreur > erreur:
                    old_erreur = erreur

            if old_erreur < avant:
                param_a = a
                param_b = b
                avant = old_erreur
            
    a = param_a
    b = param_b

    error = []
    
    for i in range(len(Power)):
        error.append((puissance(a,b,T1,T2,S_sur_L)[i]-Power[i])/puissance(a,b,T1,T2,S_sur_L)[i])
    
    return a,b,np.array(error)


################################################################################################################    


def puissance(a,b,T1,T2,S_sur_L):
    
    """ 
    Cette fonction détermine la puissance transitant entre 2 points de température
    
    
    Plage de validité : Tout le temps (à tester avec des plages de températures larges )
    
    Entrée :    T1 la température la plus haute
                T2 la température la plus basse
                Power la puissance injectée pour obtenir le couple T1, T2
                S_sur_L une constante correspondant au rapport entre la section et la longueur
    
    Sortie :    Q_dot un vecteur de puissance
     
    """ 
    
    
    Q_dot = []
    for i in range(len(T1)):
        Q_dot.append(S_sur_L * a / (b+1) * (T1[i]**(b+1) - T2[i]**(b+1)))
    return np.array(Q_dot)


def random_color():
    r = random.uniform(0, 255)
    g = random.uniform(0, 255)
    b = random.uniform(0, 255)
    return 'rgb('+str(r)+','+str(g)+','+str(b)+')'



def fonction(Pression,Intensite):
    """ 
    
    Fournir un vectur de données " Pression " en pression avec leur intensité équivalente " Intensite " en mA
    
    """ 
    f = interpolate.interp1d(Intensite, Pression, fill_value="extrapolate", kind="linear")
    
    plt.figure()
    plt.plot(Intensite,Pression,'o')
    plt.plot(Intensite,f(Intensite),'-')
    plt.xlabel('Intensite (mA)')
    plt.ylabel('Presion (Bar)')
    plt.legend(labels = ["Points de mesure","Fonction extrapolée"])
    plt.title('Détermination de la fonction d\'équivalence du capteur')
    plt.grid()
    plt.show()
    return f