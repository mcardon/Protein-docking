#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FONCTIONS D'ECRITURE ET LECTURE DE FICHIERS PDB ET LECTURE DES FICHIERS RESULTATS DU MINIMISEUR
"""
import os,sys
from mod_filtre import *
path_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#==============================================================================
#                                 lecture de pdb
#==============================================================================    
ACE_Atom_1 = {"N" : 'N', "CA": 'CA', "C" : 'C', "O" : 'O' , "CB" : 'CB'}
ACE_Atom_2 = {
"PROCG":  'CB', "PROCD":  'CB', "LYSCE":  'KN', "LYSNZ":  'KN', "LYSCD":  'KC', "ASPCG":  'DO', "ASPOD":  'DO', "GLUCD":  'DO', "GLUOE":  'DO', 
"ARGCZ" : 'RNn', "ARGNH" : 'RNn', "ASNCG": 'NN', "ASNND": 'NN', "ASNOD": 'NN', "GLNCD": 'NN', "GLNOE": 'NN', "GLNNE": 'NN', "ARGCD": 'RNe', 
"ARGCD": 'RNe', "ARGNE": 'RNe', "SERCB": 'SO', "SEROG": 'SO', "THROG": 'SO', "TYROH": 'SO', "HISCG": 'HN', "HISND": 'HN', "HISCD": 'HN', 
"HISCE": 'HN', "HISNE": 'HN', "TRPNE": 'HN', "TYRCE": 'YC', "TYRCZ": 'YC', "ILECG": 'LC', "METCE": 'LC', "VALCG": 'LC', "CYSSG": 'CS' }

def findAtomsInfo(infile):
    """
    ### Description
    To parse a pdb file (infile)

    ### Input
    infile : string : nom du fichier pdb (ex: "3pdz.pdb")
    
    ### Output
    atomsList : [[x1,y1,z1, NomAtom, NomRes, Chaine, NbrResi, NbrAtom ],[x2,y2,z2, NomAtom, NomRes, Chaine, NbrResi,NbrAtom ]...]
    Liste de liste des Atoms de la proteine ou pour chaque atome il y a l'information 
    de ses coordonnees x,y,z, le nom de l'atome, le nom du residu, la chaine, le numero du residu et le nombre de l'atome. (toute chaine confondue)
    """
    f = open(infile, 'r')
    atoms=[]
    for line in f:  
        l = line.split();
        if l[0] == 'ATOM':
            curres = "%s"%(line[22:26]).strip()
            res = line[17:20].strip()
            atome = line[12:15].strip() 
            
            if line[12:16].strip() == 'OXT':
                atome = 'O'

            try:
                if res != 'GLY' and atome != 'CA':
                    key = ACE_Atom_1[atome]
                else: 
                    key = 'GC'
            except KeyError:
                try:
                    key = ACE_Atom_2[res+atome]
                except KeyError:
                    if res != 'ILE' and atome != 'CG':
                        key = 'FC'
                    else:
                        if line[12:16].strip() == 'CG1':
                            key = 'FC'
                        else:
                            key = 'LC'
            if line[12:16].strip() == 'OXT':
                atome = 'O'
            else:
                atome = line[12:16].strip()
       
            atom = [float(line[30:38]), float(line[38:46]), float(line[46:54]), atome, res, line[21], int(curres), int(l[1]), key] # Coordonnees x,y,z de l'atom            
            atoms.append(atom)
    f.close()

    return atoms


def defRecepLigand(atoms1, atoms2, infile1, infile2):
    """
    ### Description
    Cette fonction sert a decider quelle proteine sera la proteine Recepteur
    et quelle proteine sera la proteine Ligand en fonction la taille de la 
    proteine (nombre des atomes)

    ### Input
    infile1 : string : nom d'un fichier pdb (ex: "3pdz.pdb")
    infile2 : string : nom d'un fichier pdb (ex: "3pdz.pdb")
    atoms1 : [[x1,y1,z1, NomAtom, NomRes, Chaine, NbrResi, NbrAtom ],.. ] : liste d'atomes d'une proteine
    atoms2 : [[x1,y1,z1, NomAtom, NomRes, Chaine, NbrResi, NbrAtom ],...] : liste d'atomes d'une proteine
    
    ### Output
    list d'atomes de la proteine recepteur    
    list d'atomes de la proteine ligand
    """
    # tout depend de si on veut importer dans la fonction ou avant puis renommer les listes apres...
#    atoms1 = findAtomsInfo(infile1)   
#    atoms2 = findAtomsInfo(infile2)

    if len(atoms1) > len(atoms2):
        return atoms1, atoms2, infile1, infile2
    else:
        return atoms2, atoms1, infile2, infile1


#==============================================================================
#                          lecture des output du minimiseur
#==============================================================================    

def read_global_out(filename):
    """
    ### Description
    Cette fonction lit un fichier global_out (fichier renvoye par le minimiseur)
    et renvoie l'energie d'une conformation

    ### Input
    filename : string : nom d'un fichier global_out
    
    ### Output
    energie_totale : float : energie de la conformation
    """
    f=open(filename)
    line=f.readline()
    while not line:   # au cas ou c'est pas la premiere ligne
        line=f.readline()
    line=[float(i) for i in line.split(" ") if i != ""]
    energie_totale=line[-1]
    f.close()

    return energie_totale


#==============================================================================
#                                  ecriture de pdb
#==============================================================================

def fileOut(nomFileOut, atoms, typeFile, path_mini=None):
    """
    ### Description
    Cette fonction est utilisee pour ecrire un fichier pdb a partir d'une liste
    d'atomes reçue par parametres ou une liste de coordonees x,y,z (cas des spheres autour de la proteine)
    
    Note : si la variance circulaire est calculee (position 8) 
    elle est ecrite dans le champ temperature factor (b-factor pour pymol)

    Note2 : si la variance circulaire est calculee ET un difference de variance circulaire (pour detecter les cavites)
    la valeur de variance circulaire est ecrite dans le champ occupancy
    la valeur de difference est ecrite dans le champ b-factor (pour visualiser dans pymol)

    ### Input
    nomFileOut  : string : nom du fichier qui va être cree
    atoms       : liste  : liste des atomes a sauvegarder dans le fichier
    typeFile    : String : String qui permet identifier qu'el type de fichier pdb on souhaite sauvegarder
                Si typeFile == RR --> On va sauvegarder les résultats du calcul des rotations dans un répertoire Résultats/Rotameres
                Si typeFile == CS --> On va sauvegarder les résultats du calcul du centre de masse et des sphères dans Résultats/CentresSpheres
                Si typeFile == RP --> On va sauvegarder les rapprochement pour chaque rotation dans chaque sphere du sampling dans Résultats/Raprochements                
    path_mini   : string : chemin vers le dossier du 'Minimizer', il doit etre precise dans l'option 'RP'
    """
    if  typeFile == "RR":
        all_path = path_dir+'/Resultats/Rotameres'
            
    if  typeFile == "CS":
        all_path = path_dir+'/Resultats/temp'

    if  typeFile == "RP":
        all_path = path_mini+"/Proteins"
        
    if not os.path.exists(all_path):
        os.makedirs(all_path)

    fout = open(all_path+'/'+nomFileOut+'.pdb', "w")
    
    if len(atoms[0]) == 3:
        for atom in atoms:
            fout.write("ATOM %6s  %-4s%3s %s%4s    %8.3f%8.3f%8.3f  1.00  1.00 X X\n"%(1, "", "GEN"," ", 1,atom[0], atom[1],atom[2]))

    elif len(atoms[0]) < 9:        
        for atom in atoms:
            fout.write("ATOM %6s  %-4s%3s %s%4s    %8.3f%8.3f%8.3f  1.00  1.00 X X\n"%(atom[7], atom[3], atom[4],atom[5], atom[6], atom[0] ,atom[1],atom[2] ))

    elif len(atoms[0]) == 9:
        try:
            int(atoms[0][8])
            for atom in atoms:
                fout.write("ATOM %6s  %-4s%3s %s%4s    %8.3f%8.3f%8.3f  1.00  %1.2f X X\n"%(atom[7], atom[3], atom[4],atom[5], atom[6], atom[0] ,atom[1],atom[2],atom[8] ))

        except ValueError:
            for atom in atoms:
                fout.write("ATOM %6s  %-4s%3s %s%4s    %8.3f%8.3f%8.3f  1.00  1.00 X X\n"%(atom[7], atom[3], atom[4],atom[5], atom[6], atom[0] ,atom[1],atom[2]))

    else:        
        for atom in atoms:
            fout.write("ATOM %6s  %-4s%3s %s%4s    %8.3f%8.3f%8.3f  %1.2f  %1.2f X X\n"%(atom[7], atom[3], atom[4],atom[5], atom[6], atom[0] ,atom[1],atom[2],atom[8],atom[9] ))

    fout.close()
