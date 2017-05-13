#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################
#                 IMPORT DES MODULES
#######################################################

import sys,os,argparse,shutil,timeit,time,subprocess,re
from os import listdir
from numpy import mean

# importer les fonctions
from modules.mod_sampling import *
from modules.mod_scoring import *
from modules.mod_pdb import *
from modules.mod_rappro import *
from modules.mod_move import *
from modules.mod_filtre import *


#######################################################
#                 GESTION DES ARGUMENTS
#######################################################

parser = argparse.ArgumentParser(description="Le code %s execute un docking entre deux proteines et retourne dans un dossier Resultats les <NUM> meilleures conformations predites de l'une des deux, numerotees dans l'ordre decroissant de probabilite et un fichier texte avec les scores pour chaque conformation"%sys.argv[0].split("/")[-1])
parser.add_argument("-num",  required = False, help = "number of best complexes to output (10 by default)")
parser.add_argument("-ab",  action='store_true', required = False, help = "add this argument if you have an antibody-antigen complex")
parser.add_argument("-twoRuns",  action='store_true', required = False, help = "add this argument if would like to perform a second sampling and scoring accoring to the best results in the first run")
parser.add_argument("-N", required = False, help = "number of positions of complexes generated during sampling (default value takes into account the size of the receptor)")
parser.add_argument("-A", required = False, help = "number of angles per axis for the ligand during sampling (default value is 4)")
parser.add_argument("-mini", required = False, help = "directory where the Minimizer is stored")
parser.add_argument("-input1", required = True, help = "pdb filename of the 1st protein or of receptor if argument -ab is True")
parser.add_argument("-input2", required = True, help = "pdb filename of the 2nd protein or of ligand if argument -ab is True")
args = parser.parse_args()

path_dir = os.path.dirname(os.path.realpath(__file__)) # position du code

infile1 = args.input1
infile2 = args.input2
anticorps = args.ab         # si c'est un complexe Ac-Ag
second_run = args.twoRuns   # si on veut faire un deuxieme sampling

if args.N:
    nb_pos = int(args.N)    # nombre de positions du ligand autour du recepteur
else:
    nb_pos = False

if args.num:
    num_scoring = int(args.num)    # nombre de complexes a renvoyer
else:
    num_scoring = 10

if args.A:
    nb_angles = int(args.A) # nombre d'angles de rotation du ligand pour alpha, beta et gamma
else:
    nb_angles = 4

if args.mini:
    path_mini = args.mini   # chemin vers le minimiseur
else:
    path_mini = path_dir+'/Minimizer'


#######################################################
#                 RANGEMENT DES DOSSIERS
#######################################################

# Degager le dossier temp et Rotameres dans le dossier Resultats et le dossier Proteins, pdb_mini et global_out dans le minimiseur
dossiers=[path_dir+'/Resultats',path_mini+'/Proteins',path_mini+'/pdb_mini',path_mini+'/global_out']
for dossier in dossiers:
    if os.path.exists(dossier):
        shutil.rmtree(dossier, ignore_errors=True)
        os.makedirs(dossier)
    else:
        os.makedirs(dossier)


#######################################################
#                 FONCTION INTERMEDIAIRE
#######################################################

def rappro_mini_best_conf(rotamere_files,sampling_coord,mtxL,mtxR,CDM_R,atoms_R,num_mini, num_scoring,clash_dist,tolerance_dist,rayon_R,rayon_L,name_R,path_dir,path_mini):

    dicoSpheres = {}      # garde en memoire la position de chaque sphere
    best_conf = []        # garde en memoire les noms des meilleurs conformations
    memoire = []          # garde en memoire chaque complexe pour eviter les doublons
    best_scores_mini = [] # liste meilleurs scores minimisation
    best_scores = []      # garde en memoire le score des meilleurs conformations

    Emin_list = []
    names_all_after_mini = []

    # sampling avec toutes les rotations et toutes les positions
    for rot_num, rotamere in enumerate(rotamere_files):

        if rot_num != 0:
            os.remove(path_dir+"/Resultats/Rotameres/"+rotamere_files[rot_num-1])

        atoms = findAtomsInfo(path_dir+'/Resultats/Rotameres/'+rotamere) # charger les atomes du rotamere

        for idx, sphere in enumerate(sampling_coord):

            dicoSpheres["Sphere"+str(idx)] = list(sphere)
            name = rotamere[:17] + "_Sphere"+str(idx)

            # deplacer le ligand
            newatoms_L, newCDM_L = place_ligand_sampling(sphere, coord_mass_center(atoms), atoms)

            # faire le rapprochement vers le recepteur
            rapprochement(name, atoms_R, newatoms_L, CDM_R, newCDM_L, clash_dist, tolerance_dist, path_mini)

            # lancer la minimisation
            os.system('python %s/runMini.py -rec %s -lig %s -wd %s' %(path_mini,name_R+'.pdb',name+'.pdb',path_mini))

            #nom du fichier attendu apres minimisation
            name_L_aftermini = path_mini+"/pdb_mini/"+name_R+'_'+name+'.pdb'

            # si le fichier existe
            if os.path.isfile(name_L_aftermini):

                atoms_aftermini = findAtomsInfo(name_L_aftermini) # charger les atomes du rotamere

                # pour enlever les doublons
                if str(atoms_aftermini[:10]) not in memoire:
                    memoire.append(str(atoms_aftermini[:10]))

                    Emin = read_global_out(path_mini+"/global_out/global_"+name_R+'_'+name+'.dat')

                    #sauvegarde du score et du nom du fichier
                    Emin_list.append(Emin)
                    names_all_after_mini.append(name_L_aftermini)

                    # supprimer les global_out et pdb rapproches
                    os.remove(path_mini+"/global_out/global_"+name_R+'_'+name+'.dat')
                    os.remove(path_mini+"/Proteins/"+name+'.pdb')

                    # sauvegarder les premiers scores avec les noms (nombre de scores = num_mini)
                    if len(best_scores_mini) < num_mini :
                        best_scores_mini.append(Emin)
                        best_conf.append(name)
                            
                        #ranger les scores et les noms dans l'ordre des scores (croissant)
                        tri = sorted(zip(best_scores_mini,best_conf), key=lambda pair: pair[0])
                        best_scores_mini = [e for (e,n) in tri]
                        best_conf = [n for (e,n) in tri]

                    else:
                        # quand on a deja le nombre max de scores en memoire, tester si on remplace le moins bon par le nouveau
                        # si le score est inferieur au score maximum

                        if Emin < best_scores_mini[-1]:

                            #retirer le dernier de la liste et supprimer le pdb correspondant
                            best_scores_mini.pop()
                            name_to_remove = best_conf.pop()
                            os.remove(path_mini+"/pdb_mini/"+name_R+'_'+name_to_remove+'.pdb')

                            #ajouter le nouveau score et le nouveau nom
                            best_scores_mini.append(Emin)
                            best_conf.append(name)

                            #ranger les scores et les noms dans l'ordre des scores (croissant)
                            tri = sorted(zip(best_scores_mini,best_conf), key=lambda pair: pair[0])
                            best_scores_mini = [e for (e,n) in tri]
                            best_conf = [n for (e,n) in tri]
                        else:
                            # si cette conformation n'est pas meilleure, la retirer
                            os.remove(name_L_aftermini)

    # retirer les dossiers Rotameres et temp et Proteins et global_out
    shutil.rmtree(path_dir+"/Resultats/Rotameres", ignore_errors=True)
    shutil.rmtree(path_dir+"/Resultats/temp", ignore_errors=True)
    shutil.rmtree(path_mini+"/Proteins", ignore_errors=True)
    shutil.rmtree(path_mini+"/global_out", ignore_errors=True)

    # scoring sur les meilleures conformations
    for conf in best_conf:
        atoms_L_best = findAtomsInfo(path_mini+"/pdb_mini/"+name_R+'_'+conf+'.pdb') # charger les atomes
        CDML = coord_mass_center(atoms_L_best)

        # scoring sur cette conformation
        score = scoring_partiel_function_one_conformation(atoms_L_best,CDML,rayon_L,atoms_R,CDM_R,rayon_R,mtxR,mtxL)
        best_scores.append(score)

    # tri des scores du scoring
    tri = sorted(zip(best_scores,best_conf), key=lambda pair: pair[0])
    best_scores = [e for (e,n) in tri]
    best_conf = [n for (e,n) in tri]

    return best_conf[0:num_scoring], best_scores[0:num_scoring], dicoSpheres, Emin_list, names_all_after_mini



#######################################################
#                 FONCTION PRINCIPALE
#######################################################

def fonctionMain(infile1, infile2, anticorps, nb_pos, nb_angles, num_scoring, second_run, path_dir, path_mini):
    """
    ### Description
    Function Main du projet
    
    ### Input
    infile1 : string : nom d'un fichier pdb (recepteur si anticorps=True)
    infile2 : string : nom d'un fichier pdb (ligand si anticorps=True)
    anticorps : boolean : True si on a un complexe anticorps-antigene
    nb_pos : int : nombre de positions autour du recepteur sur la sphere de sampling (False par defaut)
    nb_angles : int : nombre d'angles par axe pour la rotation du ligand
    num_scoring : int : nombre de meilleurs conformations a retourner
    second_run : boolean : si True, le programme fait un deuxieme sampling avec plus de rotameres mais 
                cible sur les positions des meilleurs complexes du premier tour
    path_dir : string : chemin vers la ou se situe ce fichier python
    path_mini : string : chemin vers le dossier Minimizer

    ### Output
    Retourne dans un dossier Resultats les num_scoring meilleurs conformations du ligand numerotes dans 
    l'ordre decroissant de probabilite et un fichier texte avec les scores pour chaque conformation
    """
    if second_run:
        print "\nRound one...\n"

    # parametres de distances
    clash_dist = 6.0        # distance de clash minimale
    tolerance_dist = 1.     # distance de tolerance maximale (distance minimale entre clash_dist et clash_dist+tolerance_dist)

    # Recuperer les noms des proteines a partir des noms des fichiers
    name_R = (infile1.split("/")[-1]).split(".")[0]
    name_L = (infile2.split("/")[-1]).split(".")[0]

    # Obtenir les atoms qui appartiennent a chacune des proteines: Recepteur et Ligand 
    atoms_R = findAtomsInfo(infile1)
    atoms_L = findAtomsInfo(infile2)
    
    # Si ce n'est pas un Ac-Ag, on peut choisir la plus petite proteine comme ligand 
    if not anticorps:
        atoms_R, atoms_L, name_R, name_L = defRecepLigand(atoms_R,atoms_L,name_R,name_L)

    # Enregistrement du pdb recepteur dans le dossier "Minimizer/Proteins/"
    fileOut(name_R, atoms_R, 'RP', path_mini)

    # Calcul du centre de masse pour chacune des proteines
    CDM_R = coord_mass_center(atoms_R)
    CDM_L = coord_mass_center(atoms_L)
    
    # Calcul du rayon de chacune des proteines
    rayon_R = rayon_protein(atoms_R, CDM_R)[1]
    rayon_L = rayon_protein(atoms_L, CDM_L)[1]
   
    # Calcul des points autour de la proteine recepteur
    if anticorps:  # Filtrage des points de sampling autour de l'anticorps
        sampling_coord = Ac_Ag_domaine_variable(atoms_R, rayon_L+10, nb_pos)
    else:
        sampling_coord = points_sphere_around_recep((rayon_R+rayon_L+10), rayon_R, CDM_R, nb_pos)

    fileOut("samplingSpheres", sampling_coord, 'CS') 
    
    # Calcul des combinaisons d'angles pour la rotation du ligand
    anglesRotation = angles_rotation(nb_angles)     

    print "testing %d complexes..." %(len(anglesRotation)*len(sampling_coord))
    # Creation des rotameres dans Results/Rotameres
    rotate_all_ligand(name_L, anglesRotation, atoms_L, CDM_L)

    # Recuperer la liste des noms des fichiers pdb rotameres
    rotamere_files = [f for f in listdir(path_dir+'/Resultats/Rotameres')]

    # Pour chaque rotamere, on va le positionner a chaque position autour du recepteur
    # faire le rapprochement puis la minimisation
    mtxR = all_parametres_intraproteiques_scoring(atoms_R)
    mtxL = all_parametres_intraproteiques_scoring(atoms_L)
    num_mini = 500
    best_conf,best_scores,dicoSpheres, Emin_list, names_all_after_mini = rappro_mini_best_conf(rotamere_files,sampling_coord,mtxL,mtxR,CDM_R,atoms_R,num_mini,num_scoring,clash_dist,tolerance_dist,rayon_R,rayon_L,name_R,path_dir,path_mini)
    # best_conf : liste des noms des meilleurs conformations
    # best_scores : liste des meilleurs scores
    # dicoSpheres : dictionnaire qui associe a chaque numero de position autour du recepteur les coordonnees de ce point
    # Emin_list : liste de tous les scores du minimiseur (non trie)
    # names_all_after_mini : liste des fichiers correspondants a Emin_list

    if not second_run:

        # Creation d'un fichier texte avec le resume des scores et des conformations
        # et deplacement des resultats dans un dossier Resulats
        f=open("%s/Resultats/%d_meilleurs_complexes.txt"%(path_dir,len(best_conf)),'w')
        f.write("#filename\tscore\n")
        for i,filename in enumerate(best_conf):
            shutil.move(path_mini+"/pdb_mini/"+name_R+'_'+filename+'.pdb',path_dir+"/Resultats/"+name_L+'_'+str(i+1)+'.pdb')
            f.write("%s\t%.3f\n"%(name_L+'_'+str(i+1),best_scores[i]))
        f.close()
        shutil.rmtree(path_mini+"/pdb_mini", ignore_errors=True)

    ################################################

    # ETAPE DE DEUXIEME SAMPLING - RAFFINEMENT
    else :

        # Creation d'un fichier texte avec le resume des scores et des conformations
        # et deplacement des resultats dans un dossier Resulats/First_run
        os.makedirs(path_dir+"/Resultats/First_run")
        f=open("%s/Resultats/First_run/%d_meilleurs_complexes.txt"%(path_dir,len(best_conf)),'w')
        f.write("#filename\tscore\n")
        for i,filename in enumerate(best_conf):
            shutil.move(path_mini+"/pdb_mini/"+name_R+'_'+filename+'.pdb',path_dir+"/Resultats/First_run/"+name_R+'_'+filename+'.pdb')
            f.write("%s\t%.3f\n"%(name_R+'_'+filename,best_scores[i]))
        f.close()
        shutil.rmtree(path_mini+"/pdb_mini", ignore_errors=True)

        print "\nRound two...\n"

        os.makedirs(path_dir+"/Resultats/Rotameres")
        os.makedirs(path_dir+"/Resultats/temp")
        os.makedirs(path_mini+"/pdb_mini")
        os.makedirs(path_mini+"/global_out")
        os.makedirs(path_mini+"/Proteins")

        # Enregistrement du pdb recepteur dans le dossier "Minimizer/Proteins/"
        fileOut(name_R, atoms_R, 'RP', path_mini)

        nb_angles = 10

        # creation des rotameres et recuperation de la liste des noms des fichiers pdb rotameres
        anglesRotation = angles_rotation(nb_angles)
        rotate_all_ligand(name_L, anglesRotation, atoms_L, CDM_L)
        rotamere_files = [f for f in listdir(path_dir+'/Resultats/Rotameres')]

        # definition des positions
        sampling_coord = []
        for fichier in best_conf:
            key = re.search("Sphere[0-9]*",fichier).group(0)
            sampling_coord.append(dicoSpheres[key])

        print "testing %d complexes..."%len(anglesRotation)*len(sampling_coord)
    
        best_conf,best_scores,dicoSpheres, Emin_list, names_all_after_mini = rappro_mini_best_conf(rotamere_files,sampling_coord,mtxL,mtxR,CDM_R,atoms_R,num_mini,num_scoring,clash_dist,tolerance_dist,rayon_R,rayon_L,name_R,path_dir,path_mini)[:2]

        os.makedirs(path_dir+"/Resultats/Second_run")
        f=open("%s/Resultats/Second_run/%d_meilleurs_complexes.txt"%(path_dir,len(best_conf)),'w')
        f.write("#filename\tscore\n")
        for i,filename in enumerate(best_conf):
            shutil.move(path_mini+"/pdb_mini/"+name_R+'_'+filename+'.pdb',path_dir+"/Resultats/"+name_L+'_'+str(i)+'.pdb')
            f.write("%s\t%.3f\n"%(name_L+'_'+str(i),best_scores[i]))
        f.close()
        shutil.rmtree(path_mini+"/pdb_mini", ignore_errors=True)

        os.makedirs(path_mini+"/pdb_mini")
        os.makedirs(path_mini+"/global_out")
        os.makedirs(path_mini+"/Proteins")



##################################################################################

# Execution du main
if __name__=="__main__":

    start = timeit.default_timer()
    fonctionMain(infile1, infile2, anticorps, nb_pos, nb_angles, num_scoring, second_run, path_dir, path_mini)
    print timeit.default_timer()-start