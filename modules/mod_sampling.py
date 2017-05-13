#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FONCTIONS DE REPARTION AUTOUR D'UNE SPHERE ET CALCUL DU CENTRE DE MASSE ET RAYON DE PROTEINE
"""

import math, string
import numpy as np
from numpy import cos, sin, pi, sqrt

#==============================================================================
#         APPROXIMATION DE LA PROTEINE PAR UNE SPHERE (RAYON ET CENTRE)
#==============================================================================

def coord_mass_center(all_atoms_coord): 
    """
    ### Description
    Calcule les coordonnees du centre de masse a partir des atomes donnes
    
    ### Input
    all_atoms_coord : [[x,y,z,type_atome,type_residu,chain],...] : liste de tous les atomes de la protéine
    
    ### Output
    CDM : (x_c, y_c, z_c) : coordonnees 3D de centre de masse
    """  
    x = 0.0
    y = 0.0
    z = 0.0
    n = len(all_atoms_coord) # nombre total des atoms dans la protéine
    
    for i in all_atoms_coord:
       x += i[0]
       y += i[1]
       z += i[2]
    
    CDM = [round(x/n,3), round (y/n,3), round(z/n,3)]
    return CDM


def rayon_protein(all_atoms_coord, CDM): 
    """
    ### Description
    Calcule le rayon maximum de la proteine a partir du centre de masse et
    des atomes consideres dans la proteine
    
    ### Input
    all_atoms_coord : liste de tous les atomes de la protéine : [[x,y,z,type_atome,type_residu,chain],...]
    CDM : (x_c, y_c, z_c) : coordonnees 3D de centre de masse
    
    ### Output
    point : [x,y,z,type_atome,type_residu,chain] : coordonnees de l'atome le plus 
            eloigne du centre de masse
    rayon_prot : float : rayon maximum de la proteine (= distance de l'atome 
            le plus eloigne du centre de masse)
    """
    
    rayon_prot = 0.0
    point = [] # Point [x,y,z] qui represente l'atome le plus loin du centre de masse
    
    for i in all_atoms_coord:
       dij = (CDM[0]-i[0])**2 + (CDM[1]-i[1])**2 + (CDM[2]-i[2])**2
       if dij > rayon_prot :
           rayon_prot = dij
           point = i
            
    return point, sqrt(rayon_prot)


#==============================================================================
#                   REPARTITION AUTOUR DU CENTRE DE MASSE
#==============================================================================

def ideal_number(rayon,air_par_pt):
    """
    ### Description
    Trouve le nombre de points ideal a placer autour de la sphere
    
    ### Input
    rayon : float : rayon de la sphere
    air_par_pt : float : air moyen autour d'un point sur la sphere
            idealement entre 30 et 70 A    
    ### Output
    N : float : nombre de points "ideal" autour de la sphere
    """

    surface=4*pi*rayon**2
    N=int(surface/air_par_pt)

    return N


def points_sphere_around_recep(dist_opti, rayon_recep, CDM, N=False):
    """
    ### Description
    Calcule la position de N points equitablement repartis sur une sphere
    de rayon dist_opti et de centre CDM
    Adapte du site :
    http://web.archive.org/web/20120421191837/http://www.cgafaq.info/wiki/Evenly_distributed_points_on_sphere
    
    ### Input
    N : int : nombre de points sur la sphere
    rayon_recep : int : rayon du recepteur
    dist_opti : float : distance optimale entre recepteur et ligand (rayon_recep + rayon_lig)
    CDM : (x_c, y_c, z_c) : coordonnees 3D de centre de masse
    
    ### Output
    sampling_coord : np.array([[x1,y1,z1], [x2,y2,z2], ...]) : liste de coordonnees 3D 
    repartis de facon a peu pres equitable sur une sphere autour du point de masse
    """   
    # dans le cas ou on ne precise pas N parce qu'on ne sait pas quoi choisir
    if not N: 
        N=ideal_number(rayon_recep,30)  # je mets 70 A par point pour l'instant, 
                                      # on verra ensuite quel est l'air ideal

    xo,yo,zo = CDM

    Theta = 0.                          # theta initial i.e. azimuth
    dTheta = pi*(3.-sqrt(5.))           # selection du pas de theta selon le nombre d'or pour 
                                        # garantir un espacement correct des points

    dz = 2./N*dist_opti                 # pas de l'altitude z
    z = dist_opti-dz/2.                 # premiere valeur de z

    sampling_coord = []                 # liste des coordonnees

    #creation des points en variant z et theta (selon une sorte de spirale)
    for i in range(N): 

        #calcul du point
        r = sqrt(dist_opti**2 - z**2)
        x = cos(Theta)*r + xo
        y = sin(Theta)*r + yo
        sampling_coord.append([x,y,z+zo])

        #incrementation de z et theta
        z = z - dz
        Theta = Theta + dTheta

    return np.array(sampling_coord)