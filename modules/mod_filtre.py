#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FONCTIONS POUR DIMINUER LE NOMBRE D'ATOMES OU DE CONFORMATIONS A TESTER
"""
from mod_sampling import *
import numpy as np
from copy import deepcopy

norme = lambda vect: math.sqrt(vect[0]**2+vect[1]**2+vect[2]**2)

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

def read_rsa(filename):
    """
    ### Description
    Cette fonction importe les accessibilites contenus dans les
    fichier .rsa rendus par naccess sous forme de dictionnaire

    ### Input
    filename : string : nom d'un fichier rsa (ex: "3pdz.rsa")
    
    ### Output
    data : { chainID: {resID: accessibility} } : dictionnaire qui
            donne l'accessibilite de chaque residu sur chaque chaine
            (resID est le numero du residu)
    """
    f=open(filename)
    data={}
    line=f.readline()

    # parcourir le fichier
    while line:
        if line[:3]=="RES":
            filtered_line=[l for l in line[4:-1].split(" ") if l != ""]
            resID=int(filtered_line[2])
            chainID=filtered_line[1]
            access=float(filtered_line[4])

            # ajouter au dictionnaire
            if chainID in data:
                data[chainID][resID]=access
            else:
                data[chainID]={resID:access}

        line=f.readline()
    f.close()

    return data

def select_using_CDM(atoms,CDM,rayon):
    """
    ### Description
    Selectionne les atomes qui sont proches de la proteine opposee

    ### Input
    atoms: [[x1,y1,z1,aID1,rID1,cID1,rNum1,aNum1],...] : liste d'atomes dans la proteine
    CDM: [x,y,z] : centre de masse de la proteine opposee
    rayon: float : rayon de la proteine opposee
    
    ### Output
    idx_list: liste de integers : liste des indices des atomes selectionnes de la proteine
    """
    idx_list=[]
    for i,at in enumerate(atoms):
        if distancePoints(CDM,at) < rayon:
            idx_list.append(i)

    return idx_list


####################################################
### FILTRE ANTICORPS

def filtre_plan(atoms,normal,d):
	"""
	### Description
	Coupe la liste de coordonnees en deux selon un plan orthogonal de coordonnees le vecteur normal et d

	### Input
	atoms : [[x1,y1,z1,aID1,rID1,cID1,rNum1,aNum1],...] : liste des atomes de la proteine ou de coordonnees [x,y,z]
	normal : (x,y,z) : coordonnees du vecteur
	d : float : parametre du plan

	### Output
	new_atoms : [[x1,y1,z1,aID1,rID1,cID1,rNum1,aNum1],...] : nouvelle liste des atomes ou des points
	"""
	lg_normal = norme(normal)
	Vx,Vy,Vz = normal
	new_atoms=[]

	for atom in atoms:

		a,b,c = atom[:3]
		k = -(Vx*a + Vy*b + Vz*c + d)/(Vx*Vx + Vy*Vy + Vz*Vz)

		# projection de l'atome sur le plan
		x,y,z = (a + Vx*k, b + Vy*k, c + Vz*k)

		# vecteur entre la projection et l'atome
		vect = np.array([a-x,b-y,c-z])

		# angle entre vect et le vecteur normal au plan
		costheta = normal.dot(vect)/(lg_normal*norme(vect))

		if costheta > 0: 
		# si cos(theta) est positif, le point est au-dessus du plan 
		# (du meme cote que la deuxieme proteine)
			new_atoms.append(atom)

	new_atoms=np.array(new_atoms)

	return new_atoms

def get_DV_DC(atoms_R):
	"""
	### Description
	Recupere les indices des atomes qui sont dans la region variable et la region constante de l'anticorps

	### Input
	atoms_R : [[x1,y1,z1,aID1,rID1,cID1,rNum1,aNum1],...] : liste des atomes d'anticorps

	### Output
	DV : {chaineID : [idx1,idx2,...]} : liste des indices des atomes pour chaque chaine 
										qui sont dans le domaine variable
	DC : {chaineID : [idx1,idx2,...]} : liste des indices des atomes pour chaque chaine 
										qui sont dans le domaine constant
	"""
	DV={} # domaine variable
	DC={} # domaine constant
	i=0
	while i < len(atoms_R):
		ch=atoms_R[i][5]
		if ch not in DV:
			DV[ch]=[]
		if ch not in DC:
			DC[ch]=[]
		prev_residu=atoms_R[i][6]
		comp=0
		while i < len(atoms_R) and atoms_R[i][5]==ch:
			res=atoms_R[i][6]
			if res != prev_residu:
				comp += 1
				prev_residu = res        
			if comp < 110:
				DV[ch].append(i)
			else:
				DC[ch].append(i)
			i += 1

	return DV,DC

def find_chain_pairs(keys,DV,atoms_R):
	"""
	### Description
	Trouve des pairs de chaines de l'anticorps

	### Input
	DV : {chainID : [idx1,idx2,...]} : liste des indices des atomes pour chaque chaine 
										qui sont dans le domaine variable
	keys : [chainID1, chainID2, ...] : liste des identifieurs de chaines dans l'anticorps
	atoms_R : [[x1,y1,z1,aID1,rID1,cID1,rNum1,aNum1],...] : liste des atomes d'anticorps

	### Output
	chain_pairs : [(chainID1,chainID2),...] : liste des paires de chaines (i.e. 1 chaine 
											legere + 1 chaine lourde)
	"""
	if len(keys) == 2:
		return [keys]

	centres=[]
	for ch in keys:
		centres.append(coord_mass_center([atoms_R[i] for i in DV[ch]]))

	mtx=np.ones((len(centres),len(centres)))*float("Inf")
	for i in range(0,len(centres)-1):
		for j in range(i+1,len(centres)):
			mtx[i,j]=np.sqrt(sum([(centres[i][k]-centres[j][k])**2 for k in range(3)]))

	chain_pairs=[]
	for i in range(len(centres)/2):
		a,b=np.unravel_index(mtx.argmin(), mtx.shape)
		mtx[a,b]=float("Inf")
		chain_pairs.append((keys[a],keys[b]))

	return chain_pairs

def trouver_plan(atoms_R,DV,CDM_DC,CDM_DV):
	"""
	### Description
	Trouve l'equation du plan separateur

	### Input
	atoms_R : [[x1,y1,z1,aID1,rID1,cID1,rNum1,aNum1],...] : liste des atomes de l'anticorps
	DV : liste de float : indexes des atomes de l'anticorps qui sont dans le domaine variable
	CDM_DC : [x,y,z] : centre de masse de la partie constante de l'anticorps
	CDM_DV : [x,y,z] : centre de masse de la partie variable de l'anticorps

	### Output
    vect : [x,y,z] : vecteur normal du plan
    d : float : constante d du plan
	"""
	# trouver un point du plan de separation :
	# on le definiera comme un point entre le point du domaine variable 
	# plus proche du centre de masse du domaine constant et celui le plus eloigne
	mini=float("Inf")
	maxi=-float("Inf")
	for d in DV:
	    atd=atoms_R[d]
	    m=sum([(atd[i]-CDM_DC[i])**2 for i in range(3)])
	    if m < mini:
	        mini=m
	        min_atd=atd[:3]
	    if m > maxi:
	        maxi=m
	        max_atd=atd[:3]

	pt = [(min_atd[i]*3+max_atd[i])/4. for i in range(3)]  # point du plan de separation qui va definir sa position

	norme = lambda vect: math.sqrt(vect[0]**2+vect[1]**2+vect[2]**2)

	# vecteur directeur du plan
	vect=np.array([CDM_DV[i]-CDM_DC[i] for i in range(3)]) # vecteur normal au plan qui va definir sa direction
	Vx,Vy,Vz = vect
	lg_vect=norme(vect)

	# calcul de d 
	d = -np.array(pt).dot(vect)

	return vect, d

def Ac_Ag_domaine_variable(atoms_R,rayon_L,nb_pos):
	"""
	### Description
	Renvoie des positions de sampling cibles autour des domaines variables des anticorps

	### Input
	atoms_R : [[x1,y1,z1,aID1,rID1,cID1,rNum1,aNum1],...] : liste des atomes d'anticorps
	rayon_L : float : rayon du ligand
	nb_pos : int : nombre de positions (si False, un nombre par default est choisi qui 
					prend en compte le rayon du recepteur)

	### Output
	chain_pairs : [(chainID1,chainID2),...] : liste des paires de chaines (i.e. 1 chaine 
											legere + 1 chaine lourde)
	"""
	# domaines variables et constants par chaine
	DV,DC = get_DV_DC(atoms_R)

	# longueur de la partie constante de la chaine legere
	lg = min(map(len,DC.values())) 

	keys = DV.keys() # noms des chaines

	# regrouper les chaines par 2 (i.e. 1 chaine lourde + 1 chaine legere forment 1 bras du Y)
	chain_pairs = find_chain_pairs(keys,DV,atoms_R)

	new_sampling = []
	for num in range(len(chain_pairs)):
		(ch1,ch2)=chain_pairs[num]
		atoms = [atoms_R[i] for i in DV[ch1]+DV[ch2]]
		CDM_DV = coord_mass_center(atoms)
		rayon = rayon_protein(atoms,CDM_DV)[1]
		sampling = points_sphere_around_recep(rayon+rayon_L,rayon,CDM_DV,nb_pos)
		CDM_DC = coord_mass_center([atoms_R[i] for i in DC[ch1][:lg]+DC[ch2][:lg]])
		vect, d = trouver_plan(atoms_R,DV[ch1]+DV[ch2],CDM_DC,CDM_DV)
		new_sampling += list(filtre_plan(sampling,vect,d))

	return new_sampling