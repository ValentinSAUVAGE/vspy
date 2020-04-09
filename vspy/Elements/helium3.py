#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Created on Fri Feb 22 09:33:56 2019 - @author: valentinsauvage """

# Ce programme compile plein de fonctions calculant et regroupant les propriétés de l'helium 3

# Fonctions à importer
import VSAUVAGE.catalogue_fonctions as cf
# Constantes à importer
import VSAUVAGE.catalogue_constantes as cc
import numpy as np

""" Constantes de l'helium 3 """

# Masse de l'atome d'helium 3 
masse = 2*(cc.m_electron + cc.m_proton ) + cc.m_neutron

# Masse atomique de l'atome d'helium 3 (from https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=)
masse_atomique = 3.0160293201  # uma


