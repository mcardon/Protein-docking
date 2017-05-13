#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

FONCTIONS DE SCORING

"""
import numpy as np
from mod_ForceField import *
from mod_pdb import *
from mod_filtre import select_using_CDM
from mod_sampling import coord_mass_center,rayon_protein

#==============================================================================
#               Import des donnees Force Field : variables globales
#==============================================================================


dvdw, depsilon = epsilon_vdw_PDB()  # rayon de van der Waals : sigma_i selon la nature du residu puis le type d'atome (dico); 
                                    # profondeur du puit de vdW : esp_i selon la nature du residu puis le type d'atome (dico)


#==============================================================================
#                Calcule des differents termes de fonction de scoring 
#==============================================================================

def dist_square(at1,at2):
    """
    ### Description
    Determine la distance carre entre deux atomes i et j

    ### Input
    atom_i : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : list de coordonnees 3D d'atome i.
    atom_j : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : list de coordonnees 3D d'atome j.  

    ### Output
    Dist_rij : distance au carre entre deux atomes en Angstrom.    
    """

    d=0.
    for i in range(3):
        d+=(at1[i]-at2[i])**2

    return d

def determine_rij(atom_i,atom_j):
    """
    ### Description
    Determine la distance rij entre deux atomes i et j

    ### Input
    atom_i : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : list de coordonnees 3D d'atome i.
    atom_j : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : list de coordonnees 3D d'atome j.  

    ### Output
    Dist_rij : distance entre deux atomes en Angstrom.    
    """
    rij=dist_square(atom_i,atom_j)
    rij=np.sqrt(rij)
    return rij

def determine_epsilonij(atom_i,atom_j):
    """
    ### Description
    Calcul le epsilon entre les atomes i et j (depend du type de residu et d'atome)
    Epsilon est constant pour un type d’atomes donné, et décrit la profondeur du puits d’énergie à son minimum. 

    ### Input
    atom_i : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : list de coordonnees 3D d'atome i.
    atom_j : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : list de coordonnees 3D d'atome j. 

    ### Output
    Epsilon : float 
    """
    return np.sqrt(depsilon[atom_i[4]][atom_i[3]]*depsilon[atom_j[4]][atom_j[3]])

def determine_sigmaij(atom_i,atom_j):
    """
    ### Description
    Calcul le rayon de van der Waals entre les atomes i et j (depend du type de residu et d'atome)

    ### Input
    atom_i : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : list de coordonnees 3D d'atome i.
    atom_j : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : list de coordonnees 3D d'atome j. 

    ### Output
    sigmaij : float

    """
    return dvdw[atom_i[4]][atom_i[3]]+dvdw[atom_j[4]][atom_j[3]]

def van_der_waals_repulsive_long(rij,sigmaij,epsilonij):
    """
    ### Description
    Calcule d'energie de van der waals attractive pour 0.6 sigmaij < rij < 0.89 sigmaij
    Meme fonction que Van der waals attractive!

    ### Input
    rij : distance entre deux atomes i et j.
    sigmaij : le rayon de van der Waals entre les atomes i et j.
    epsilonij : float, la profondeur du puits d’énergie à son minimum.

    ### Output
    van_der_waals_repulsive_long : float
    """ 
    quotient=sigmaij/rij
    somme=(quotient**12)-(2*(quotient**6))
    return epsilonij*somme 

def van_der_waals_repulsive_short(rij,sigmaij,epsilonij):
    """
    ### Description
    Calcule d'energie de van der waals repulsive pour rij < 0.6 sigmaij

    ### Input
    rij : distance entre deux atomes i et j.
    sigmaij : le rayon de van der Waals entre les atomes i et j.
    epsilonij : float, la profondeur du puits d’énergie à son minimum.

    ### Output
    force : float, energie Van der Waals repulsive à courte distance.
    """
    sig2=0.6*sigmaij
    sig12=sigmaij**12
    sig6=sigmaij**6

    quotient1=(sig12)/((sig2)**12)
    quotient2=(sig6)/((sig2)**6)
    A=quotient1-(2*quotient2)

    quotient3=(sig12)/((sig2)**13)
    quotient4=(sig6)/((sig2)**7)
    B=12*(quotient4-quotient3)

    force=epsilonij*(A+(((sig2)-rij)*B))
    return force 

def atome_parametres_scoring(rij,at1,at2):
    """
    ### Description
    Calcul le parametre EwdW_r du couple d'atomes (at1, at2)

    ### Input
    rij : float : distance entre les atomes at1 et at2
    at1 : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : un 1er atome
    at2 : [x,y,z,atomeID,resID,chainID,resNum,atomNum] : un 2eme atoms

    ### Output
    EwdW_r : float : repulsive van der Waals
    """
    sigmaij=determine_sigmaij(at1,at2)
    epsilonij=determine_epsilonij(at1,at2)
    
    EwdW_r=0
    # terme de van der Waals
    if 0.6*sigmaij<=rij<=0.89*sigmaij:
        EwdW_r=van_der_waals_repulsive_long(rij,sigmaij,epsilonij)
    if rij<0.6*sigmaij:
        EwdW_r=van_der_waals_repulsive_short(rij,sigmaij,epsilonij)

    return EwdW_r

def intraproteique_parametres_scoring(idx,mtx):
    """
    ### Description
    Calcul le parametre EwdW_r intra-moleculaire pour les atomes selectionnes 
    de la proteine

    ### Input
    idx : liste de interger : liste des indices des atomes dans la proteine
    mtx : np.array(len(protein)*len(protein)) : matrice avec tous les parametres des pairs intra atomiques de la proteine

    ### Output
    EwdW_r : float : repulsive van der Waals
    """
    return mtx[idx,:][:,idx].sum(axis=1).sum(axis=0)   

def all_parametres_intraproteiques_scoring(protein):
    """
    ### Description
    Calcule le parametre EwdW_r pour toutes les paires intra-proteique 
    de la proteine

    ### Input
    protein : [[x,y,z,atomeID,resID,chainID,resNum,atomNum], ...] : tous les atomes de la proteine
                   
    ### Output
    Matrice avec le parametre EwdW_r du scoring pour chaque couple d'atomes
    EwdW_r : float : repulsive van der Waals
    """
    lg=len(protein)
    mtx=np.zeros((lg,lg))
    for i1 in range(0,lg-1):
        at1 = protein[i1]
        for i2 in range(i1+1,lg):
            at2 = protein[i2]
            dist = dist_square(at1,at2)  # distance au carre
            if dist<64:   # i.e. 8 au carre
                rij = np.sqrt(dist)
                mtx[i1,i2]=atome_parametres_scoring(rij,at1,at2)

    return mtx

#==============================================================================
#                          Calcule de score scoring
#==============================================================================

def scoring_partiel_function_one_conformation(list_atom,CDML,RL,recepteur,CDMR,RR,mtxR,mtxL):
    """
    ### Description
    Calcule le score scoring sur la conformation

    ### Input
    list_atom : [[x,y,z,atomeID,resID,chainID,resNum,atomNum],...] : list des atomes dans le ligand
    CDML : [x,y,z] : coordonnees du centre de masse du ligand
    RL : float : rayon du ligand
    recepteur : [[x,y,z,atomeID,resID,chainID,resNum,atomNum],...] : list des atomes dans le recepteur 
    CDMR : [x,y,z] : coordonnees du centre de masse du recepteur
    RR : float : rayon du recepteur
    mtxR : liste de listes : parametres de scoring entre chaque pair d'atomes du ligand
    mtx L : liste de listes : parametres de scoring entre chaque pair d'atomes du recepteur
    
    ### Output
    score : score scoring de la conformation
    """
    # cas ou tous les atomes sont trop distants, on retourne +inf
    distCDM=determine_rij(CDML,CDMR)
    if RL+RR+8 < distCDM :
        return float("Inf")

    # initiation des parametres
    parametres=0

    # trouver les indices des atomes qui sont proches de la proteine opposee
    idxL=select_using_CDM(list_atom,CDMR,RR+8)
    idxR=select_using_CDM(recepteur,CDML,RL+8)

    idxL2={}
    idxR2={}

    compteur=0   # compte le nombre de paires qui sont eloignes de moins de 8 A
    for i1 in idxL:
        atL = list_atom[i1]
        for i2 in idxR:
            atR = recepteur[i2]
            dist = dist_square(atL,atR)  # distance au carre
            if dist<64:   # i.e. 8 au carre
                rij = np.sqrt(dist)
                compteur+=1
                parametres+=atome_parametres_scoring(rij,atL,atR)
                idxL2[i1]=0
                idxR2[i2]=0

    idxL2=idxL2.keys()
    idxR2=idxR2.keys()

    # utilisation des energies intra-atomiques des atomes qui sont a l'interface 
    # (i.e. les atomes qui sont impliques dans des interactions inter-proteiques)
    parametres+=intraproteique_parametres_scoring(idxL2,mtxL)
    parametres+=intraproteique_parametres_scoring(idxR2,mtxR)

    if compteur != 0:
        score=parametres
    else:
        score=float("Inf") # verification : cas ou tous les atomes sont eloignes de plus de 8 A

    return score