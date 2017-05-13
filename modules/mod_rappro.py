#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
REGROUPE LES FONCTIONS DE RAPPROCHEMENT DU LIGAND VERS LA PROTEINE
"""

from mod_move import *
from mod_sampling import *
from mod_pdb import *
import copy, itertools
path_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


#==============================================================================
#                               RAPPROCHEMENTS
#==============================================================================

def rapprochement(nameFile, coord_R, coord_L, centre_masseR, centre_masseL, dist_clash, dist_tolerance, path_mini):
    """
    ### Description
    Rapproche le ligand du recepteur
    
    ### Input
    nameFile : Pour sauvegarder le pdb du rapprochement
    dist_clash : float : distance minimum entre deux atomes (sans clash) 
    coord_R : [[x,y,z,atomeID,resID,chainID,resNum,atomNum],...] : list de coordonnees 3D du recepteur
    coord_L : [[x,y,z,atomeID,resID,chainID,resNum,atomNum],...] : list de coordonnees 3D du ligand
    centre_masseR : [x,y,z] : list : coordonnees du centre de masse recepteur
    centre_masseL : [x,y,z] : list : coordonnees du centre de masse ligand
    dist_clash : distance en dessous de laquelle on a un clash
    dist_tolerance : tolerance entre la vraie distance et la distance de clash (vraie dist toujours superieure)
    
    ### Output
    new_coord_L : [[x,y,z,atomeID,resID,chainID,resNum,atomNum],...] : nouvelles coordonnees du ligand
    """
    
    minDist = fast_dist_min(coord_R, coord_L)
    c_R = centre_masseR
    c_L = centre_masseL
    newCoord_L = copy.deepcopy(coord_L)

    # pour limiter le nombre d'iterations du while au cas ou
    compteur = 0
    nb_max = 100

    while compteur < nb_max and (minDist - dist_clash) > dist_tolerance:
        vecteurTranslation = vect_trans_sec(c_R, c_L, minDist, dist_clash )
        translation_result = transfer_protein(vecteurTranslation, c_L, newCoord_L)

        minDist = fast_dist_min(coord_R, translation_result[0])

        if (minDist - dist_clash) > dist_tolerance:
            newCoord_L = translation_result[0]
            c_L = translation_result[1]

        compteur += 1
    
    fileOut(nameFile, newCoord_L, 'RP', path_mini)
    


#==============================================================================
#                           DISTANCE ENTRE DEUX POINTS
#==============================================================================

def distancePoints(point1, point2):
    """
    ### Description
    Calcule de la distance d'un point à un autre point
    
    ### Input
    point1 : [x,y,z] : list de coordonnees 3D du recepteur
    point2 : [x,y,z] : list de coordonnees 3D du ligand    
    
    ### Output
    distance : distance entre les deux points donnees
    """
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)

def fast_dist_min(proteineR, proteineL):
    """
    ### Description
    Calcule la distance entre chaque combinaison de pair d'atomes entre la proteine et le ligand
    
    ### Input
    proteineR : [[x,y,z,atomeID,resID,chainID,resNum,atomNum],...] : list de coordonnees 3D du recepteur
    proteineL : [[x,y,z,atomeID,resID,chainID,resNum,atomNum],...] : list de coordonnees 3D du ligand

    ### Output
    distMin : reenvoie de la distance minimal entre les deux proteines
    """
    distMin = float("Inf")
    atomL = 0
    atomR = 0
    for i in range(len(proteineR)):
        atomR = proteineR[i]
        for j in range(len(proteineL)):
            atomL = proteineL[j]
            dij = (atomR[0]-atomL[0])**2 + (atomR[1]-atomL[1])**2 +(atomR[2]-atomL[2])**2
            if (dij<distMin):
                distMin = dij
    return math.sqrt(distMin)
