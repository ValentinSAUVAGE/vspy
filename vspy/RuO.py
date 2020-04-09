#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Created on Sun Mar 24 17:36:20 2019 - @author: valentinsauvage """

import numpy as np

################################################################################################################    

def Xsymbol(res):
    """ 
    Model : RuO
    Calibration : By IAS in Dracula
    Use : none
    Domaine : 25 mK to 101K
    """
    
    Fit1 = np.poly1d([
        1.8137025216013217e-10, -7.7285162285621021e-09,
        9.3822677665445573e-08,  1.7091736058552259e-07,
       -7.0175074363433868e-06, -3.7586102769503047e-05,
        3.9875117836912370e-04,  5.5592356543180182e-03,
        1.7101148310620505e-03, -4.7067687877404329e-01,
       -3.3233892671186531e+00,  1.9567464220051644e+01,
        4.1038923070836717e+02,  4.0612047812077395e+02,
       -3.5306185200452332e+04, -1.0709002594508344e+05,
        3.5656048551622890e+06, -1.8197515831288122e+07,
        3.0079544655893497e+07])
    
    Fit2 = np.poly1d([
       -7.4267799415581817e+02,  8.2366771424715225e+03,
        3.1844677321152372e+04, -1.9296386966549081e+05,
       -2.8478795689291586e+06, -1.0517028917559536e+07,
        9.5185385818230048e+07,  1.3404400394585948e+09,
       -6.6077572079252300e+09])
    
    if res > 1632.99 :
        Temperature = np.exp(Fit1(np.log(res)))
    elif res <= 1632.99 : 
        Temperature = np.exp(Fit2(np.log(res)))
        
    return Temperature

################################################################################################################    

################################################################################################################    

def X0(res):
    """ 
    Model : RuO
    Calibration : By IAS in Dracula
    Use : none
    Domaine : 50 mK to 14K
    """
    
    Fit1 = np.poly1d([
        6.1673954296015150e-18, -2.1031757836576000e-16,
        1.1858494769960136e-15,  1.8798169202230593e-14,
       -2.9992495519453070e-15, -1.8626856530270924e-12,
       -1.7784417002191795e-11,  2.7011915011102329e-12,
        1.9151621369559458e-09,  2.2543103405084840e-08,
        6.8274442498377744e-08, -1.6019839616824820e-06,
       -2.7178832086629009e-05, -1.5845004505817508e-04,
        1.0429513739906424e-03,  2.9323428245775711e-02,
        2.1667601855137339e-01, -8.6326595564944897e-01,
       -3.1919330712684417e+01, -1.8198689888449061e+02,
        2.3048040828849330e+03,  3.0991862884964186e+04,
       -3.4194104685960774e+05,  8.6545986157050147e+05])
    
    Fit2 = np.poly1d([
       -7.6865541469160862e-11,  3.0545615837567138e-09,
       -3.0995559939034903e-08, -1.1700437196281132e-07,
        1.8094605867122539e-06,  1.6749404065007953e-05,
       -2.9376326986690730e-05, -1.4670720514096984e-03,
       -8.9121403541241127e-03,  4.4357486858555638e-02,
        1.0525269494628098e+00,  4.3917536934078782e+00,
       -5.5497099998491500e+01, -7.0194202912612582e+02,
        1.7303714456372256e+03,  6.7028652358254141e+04,
       -4.5727876636629010e+05,  8.6979933643526526e+05])
    
    if res > 6684.1 :
        Temperature = np.exp(Fit1(np.log(res)))
    elif res <= 6684.1 : 
        Temperature = np.exp(Fit2(np.log(res)))
        
    return Temperature

################################################################################################################    
