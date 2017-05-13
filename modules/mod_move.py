#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
REGROUPE LES FONCTIONS DE ROTATION ET TRANSLATION DE PROTEINES
"""

import math
from mod_pdb import *
import itertools
from copy import deepcopy

#==============================================================================
#                                 ROTATION
#==============================================================================

def angles_rotation(N):
    """
    ### Description
    Calcule N**3 angles de rotation equitablement repartis dans les orientations possibles
    Pour choisir les angles de rotation pour le ligand
    
    ### Input
    N : int : racine cubique du nombre d'orientations souhaitees
        
    ### Output
    All_rotation_angles : list of lists of float : liste des angles alpha,beta et gamma pour chaque rotation en radians [[alpha1,beta1,gamma1],[alpha2,beta2,gamma2],...]
    """
    # Creation de liste des N angles de rotation en radians pour une dimention (alpha ou beta ou gamma)
    List_angle_rotate_1D =[]

    # On divise 2pi radians d'une dimension par N intervalles 
    pas = float(2*math.pi/N) # un pas de changement d'angle en radians

    somme = 0 
    for j in range(N):
        if j == 0 :
            List_angle_rotate_1D.append(j)
            somme=0   # variable locale qui permet de calculer l'angle 
        else:
            somme += pas
            List_angle_rotate_1D.append(somme)

    #Liste des angle alpha, beta et gamma dans 3 listes separees 
    list_angle_alpha_beta_gamma=[List_angle_rotate_1D,List_angle_rotate_1D,List_angle_rotate_1D]

    # liste de N**3 angles de rotation equitablement repartis dans les orientations possibles, chaque angle 3D est dans un tuple 
    list_tuple_rotation_angles=list(itertools.product(* list_angle_alpha_beta_gamma))

    # liste de N**3 angles de rotation equitablement repartis dans les orientations possibles, chaque angle 3D est dans une liste 
    All_rotation_angles=[list(one_angle) for one_angle in list_tuple_rotation_angles]
    return All_rotation_angles

# tous les atomes, 1 rotation
def rotate_whole_ligand(nom_ligand_conformation,alpha, beta, gamma, atomsList, CDM):
    """
    ### Description
    Calcule les nouvelles coordonnees du ligand apres UNE SEULE rotation
    
    ### Input
    nom_ligand_conformation :nom du ligand 
    alpha, beta, gamma : floats : the angles of the rotation (en radians)
    atomsList : [[x1,y1,z1, NomAtom, NomRes, Chaine, NbrResi, NbrAtom ],[x2,y2,z2, NomAtom, NomRes, Chaine, NbrResi,NbrAtom ]...]
    dist_sopti : float : distance optimale entre recepteur et ligand (rayon_recep + rayon_lig)
    CDM : (x_c, y_c, z_c) : coordonnees 3D de centre de masse
        
    ### Output
    new_all_atoms_coord : Liste des nouveaux coordonees des atomes du ligand apres la rotation (meme format que atomsList)
    Stockage de conformation dans un fichier pdb
    """
    new_all_atoms_coord = []
    for atom in atomsList:
        lista = rotate(atom[0], atom[1],atom[2], CDM[0], CDM[1], CDM[2], alpha, beta, gamma)
        newCoor = [lista[0], lista[1], lista[2]]+atom[3:]
        new_all_atoms_coord.append(newCoor)
    
    # Ecrire un fichier pdb a partir de liste d'atomes avec les nouvaux coordonees apres une rotation
    fileOut(nom_ligand_conformation, new_all_atoms_coord, 'RR')

    
# 1 atome, 1 rotation
def rotate(x, y ,z, x0, y0, z0, alpha, beta, gamma):
    """
    ### Description
    rotation of the atom with coords (x, y, z) according to the angles alpha, beta, gamma
    
    ### Input
    x, y, z : floats : the 3D coordinates of the point to rotate
    x0,y0,z0 : floats : the coordinates of the center of rotation (i.e. center of mass of the object we want to rotate)
    alpha, beta, gamma : floats : the angles of the rotation (en radians)
                
    ### Output
    (x3i,y3i,z3i) : floats : the final coordinates in the initial referential
    """   
    # centering according to the center of rotation
    x1i=x-x0
    y1i=y-y0
    z1i=z-z0

    # computing cos and sin of each angle
    c_a=math.cos(alpha)
    s_a=math.sin(alpha)

    c_b=math.cos(beta)
    s_b=math.sin(beta)

    c_g=math.cos(gamma)
    s_g=math.sin(gamma)


    # applying rotation
    x3i = (c_a*c_b*c_g-s_a*s_g)*x1i + (-c_a*c_b*s_g-s_a*c_g)*y1i + c_a*s_b*z1i 
    y3i = (c_a*s_g+s_a*c_b*c_g)*x1i + (-s_a*c_b*s_g+c_a*c_g)*y1i + s_a*s_b*z1i
    z3i = -s_b*c_g*x1i + s_b*s_g*y1i + c_b*z1i 

    # back to the input referential
    x3i = x3i + x0
    y3i = y3i + y0
    z3i = z3i + z0
    finalC = [round(x3i, 3),round(y3i, 3),round(z3i, 3)]

    return finalC

def rotate_all_ligand(nom_ligand,all_angles, all_atoms_coord, CDM):
    """
    ### Description
    Calcule les nouvelles coordonnees du ligand apres les rotations avec tous les angles alpha, beta et gamma
    ==> execute rotate_whole_ligand() pour tous les angles
    
    ### Input
    nom_ligand :nom du ligand 
    all_angles : 
    all_atoms_coord : [[x,y,z,type_atome,type_residu,chain],...] : liste de tous les atomes de la protéine
    dist_sopti : float : distance optimale entre recepteur et ligand (rayon_recep + rayon_lig)
    CDM : (x_c, y_c, z_c) : coordonnees 3D de centre de masse
        
    ### Output
    ecriture de chaque rotation dans un fichier PDB
    """ 
    for i in range(len(all_angles)):
        a,b,c=all_angles[i]
        rotate_whole_ligand("%1.3f_%1.3f_%1.3f_%s"%(a,b,c,nom_ligand),a, b, c, all_atoms_coord, CDM)


#==============================================================================
#                                 TRANSLATION
#==============================================================================

def determineFirstTranslationVector(centerReceptor, centerLigand):
    """ 
    ### Description
    Calcule les coordonnees du vecteur de translation a partir des coordonees
    3D du centre de masse du ligand et du point de la sphere sur lequel doit 
    etre translater le centre de masse du ligand 
    
    ### Input
    centrerReceptor : (x_i, y_i, z_i) : coordonnees du centre de masse du ligand
    
    ### Output
    coordonnees du vecteur de translation
    """
    return [centerReceptor[0]-centerLigand[0],  centerReceptor[1]-centerLigand[1], centerReceptor[2]-centerLigand[2]]


def translation_1_atom(atom, translationVector):   
    """
    ### Description
    Calcule les nouvelles coordonnees d'un atome apres translation
    
    ### Input
    translationVector : (x, y, z) : coordonnees du vecteur de translation
    atom : [x1,y1,z1, NomAtom, NomRes, Chaine, NbrResi, NbrAtom ] : description de l'atome
    
    ### Output
    new_coord :[x2,y2,z2, NomAtom, NomRes, Chaine, NbrResi, NbrAtom ] : description de l'atome avec les nouvelles coordonnees apres deplacement
    """
    new_coord=[round((atom[0]+translationVector[0]), 3), round((atom[1]+translationVector[1]), 3) , round((atom[2]+translationVector[2]), 3)] + deepcopy(atom[3:])
    return new_coord


def transfer_protein(translation_vect, origin, all_atoms_coord_ligand):  
    """
    ### Description
    Calcule les nouvelles coordonnees du ligand pour le sampling
    (deplace le ligand apres rotation pour le placer sur la sphere autour de recepteur)
    
    ### Input
    translation_vect : (x_i, y_i, z_i) : coordonnees du vecteur de translation
    origine : (x_i, y_i, z_i) : coordonnees du centre de masse initial du ligand
    all_atoms_coord_ligand : [[x,y,z,type_atome,type_residu,chain],...] : list de coordonnees 3D du ligand avant deplacement
    
    ### Output
    all_atoms_coord_ligand_sample_new : [[x,y,z,type_atome,type_residu,chain],...] : list de coordonnees 3D du ligand apres deplacement
    CDM : [x,y,z] : Nouveau centre de masse du Ligand
    """
    
    all_atoms_coord_ligand_sample_new = []
    for i in range(len(all_atoms_coord_ligand)):
        atomeTranslate = translation_1_atom(all_atoms_coord_ligand[i],translation_vect)
        all_atoms_coord_ligand_sample_new.append(atomeTranslate)
    
    CDM = translation_1_atom(origin, translation_vect)

    return all_atoms_coord_ligand_sample_new, CDM


def place_ligand_sampling(destination, origin, all_atoms_coord_ligand):
    """
    ### Description
    Calcule les nouvelles coordonnees du ligand pour le sampling
    (deplace le ligand apres rotation pour le placer sur la sphere autour de recepteur)
    
    ### Input
    destination : (x_i, y_i, z_i) : coordonnees du point ou on veut placer le centre du ligand
    origine : (x_i, y_i, z_i) : coordonnees du centre de masse initial du ligand
    all_atoms_coord_ligand : [[x,y,z,type_atome,type_residu,chain],...] : list de coordonnees 3D du ligand avant deplacement
    
    ### Output
    all_atoms_coord_ligand_sample_new : [[x,y,z,type_atome,type_residu,chain],...] : list de coordonnees 3D du ligand apres deplacement
    CDM : [x,y,z] : Nouveau centre de masse du Ligand
    """
    translation_vect = determineFirstTranslationVector(destination, origin)
    all_atoms_coord_ligand_sample_new, CDM = transfer_protein(translation_vect, origin, all_atoms_coord_ligand)

    return all_atoms_coord_ligand_sample_new, CDM
    


def vect_trans_sec(center_receptor,center_ligand,dist_min, dist_clash):
    """
    Calcule le vecteur de transition entre 2 proteines
    """
    dist=math.sqrt((center_receptor[0]-center_ligand[0])**2+(center_receptor[1]-center_ligand[1])**2+(center_receptor[2]-center_ligand[2])**2)
    dist_rappro = dist_min - dist_clash
    rapport=dist/(dist_rappro)
    vect_trans=[((center_receptor[0]-center_ligand[0])/rapport),((center_receptor[1]-center_ligand[1])/rapport),((center_receptor[2]-center_ligand[2])/rapport)]
    return np.array(vect_trans)
