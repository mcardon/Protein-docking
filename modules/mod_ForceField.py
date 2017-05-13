#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DONNEES ISSUES DE CORNELL ET AL. 1995
"""
def chargePDB() :


    # charge (dcharge) : q_i selon la nature du residu puis le type d'atome (dico)
    
    dcharge = {}
    dcharge["GLY"] = {}
    dcharge["GLY"]["N"] = -0.4157
    dcharge["GLY"]["CA"] = -0.0252
    dcharge["GLY"]["C"] = 0.5973
    dcharge["GLY"]["O"] = -0.5679
    dcharge["GLY"]["H"] = 0.2719
    dcharge["GLY"]["HA2"] = 0.0698
    dcharge["GLY"]["HA3"] = 0.0698


    dcharge["ALA"] = {}
    dcharge["ALA"]["N"] = -0.4157
    dcharge["ALA"]["CA"] = 0.0337
    dcharge["ALA"]["C"] = 0.5973
    dcharge["ALA"]["O"] = -0.5679
    dcharge["ALA"]["CB"] = -0.1825
    dcharge["ALA"]["H"] = 0.2719
    dcharge["ALA"]["HB1"] = 0.0603
    dcharge["ALA"]["HB2"] = 0.0603
    dcharge["ALA"]["HB3"] = 0.0603
    dcharge["ALA"]["HA"] = 0.0823

    dcharge["ASP"] = {}
    dcharge["ASP"]["N"] = -0.5163
    dcharge["ASP"]["CA"] = 0.0381
    dcharge["ASP"]["C"] = 0.5366
    dcharge["ASP"]["O"] = -0.5819
    dcharge["ASP"]["CB"] = -0.0303
    dcharge["ASP"]["CG"] = 0.7994
    dcharge["ASP"]["OD1"] = -0.8014
    dcharge["ASP"]["OD2"] = -0.8014
    dcharge["ASP"]["H"] = 0.2936
    dcharge["ASP"]["HA"] = 0.0880
    dcharge["ASP"]["HB2"] = -0.0122
    dcharge["ASP"]["HB3"] = -0.0122


    dcharge["GLU"] = {}
    dcharge["GLU"]["N"] = -0.5163
    dcharge["GLU"]["CA"] = 0.0397
    dcharge["GLU"]["C"] = 0.5366
    dcharge["GLU"]["O"] = -0.5819
    dcharge["GLU"]["CB"] = 0.0560
    dcharge["GLU"]["CG"] = 0.0136
    dcharge["GLU"]["CD"] = 0.8054
    dcharge["GLU"]["OE1"] = -0.8188
    dcharge["GLU"]["OE2"] = -0.8188
    dcharge["GLU"]["H"] = 0.2936
    dcharge["GLU"]["HA"] = 0.1105
    dcharge["GLU"]["HB2"] = -0.0173
    dcharge["GLU"]["HB3"] = -0.0173
    dcharge["GLU"]["HG2"] = -0.0425
    dcharge["GLU"]["HG3"] = -0.0425


    dcharge["LEU"] = {}
    dcharge["LEU"]["N"] = -0.4157
    dcharge["LEU"]["CA"] = -0.0518
    dcharge["LEU"]["C"] = 0.5973
    dcharge["LEU"]["O"] = -0.5679
    dcharge["LEU"]["CB"] = -0.1102
    dcharge["LEU"]["CG"] = 0.3531
    dcharge["LEU"]["CD1"] = -0.4121
    dcharge["LEU"]["CD2"] = -0.4121
    dcharge["LEU"]["H"] = 0.2719
    dcharge["LEU"]["HA"] = 0.0922
    dcharge["LEU"]["HB2"] = 0.0457
    dcharge["LEU"]["HB3"] = 0.0457
    dcharge["LEU"]["HG"] = -0.0361
    dcharge["LEU"]["HD11"] = 0.1000
    dcharge["LEU"]["HD12"] = 0.1000
    dcharge["LEU"]["HD13"] = 0.1000
    dcharge["LEU"]["HD21"] = 0.1000
    dcharge["LEU"]["HD22"] = 0.1000
    dcharge["LEU"]["HD23"] = 0.1000
    
    dcharge["ASN"] = {}
    dcharge["ASN"]["N"] = -0.4157
    dcharge["ASN"]["CA"] = 0.0143
    dcharge["ASN"]["C"] = 0.5973
    dcharge["ASN"]["O"] = -0.5679
    dcharge["ASN"]["CB"] = -0.2041
    dcharge["ASN"]["CG"] = 0.7130
    dcharge["ASN"]["ND2"] = -0.9191
    dcharge["ASN"]["OD1"] = -0.5931
    dcharge["ASN"]["H"] = 0.2719
    dcharge["ASN"]["HA"] = 0.1048
    dcharge["ASN"]["HB2"] = 0.0797
    dcharge["ASN"]["HB3"] = 0.0797
    dcharge["ASN"]["HD21"] = 0.4196
    dcharge["ASN"]["HD22"] = 0.4196


    dcharge["GLN"] = {}
    dcharge["GLN"]["N"] = -0.4157
    dcharge["GLN"]["CA"] = -0.0031
    dcharge["GLN"]["C"] = 0.5973
    dcharge["GLN"]["O"] = -0.5679
    dcharge["GLN"]["CB"] = -0.0036
    dcharge["GLN"]["CG"] = -0.0645
    dcharge["GLN"]["CD"] = 0.6951
    dcharge["GLN"]["NE2"] = -0.9407
    dcharge["GLN"]["OE1"] = -0.6086
    dcharge["GLN"]["H"] = 0.2719
    dcharge["GLN"]["HA"] = 0.0850
    dcharge["GLN"]["HB2"] = 0.0171
    dcharge["GLN"]["HB3"] = 0.0171
    dcharge["GLN"]["HG2"] = 0.0352
    dcharge["GLN"]["HG3"] = 0.0352
    dcharge["GLN"]["HE21"] = 0.4251
    dcharge["GLN"]["HE22"] = 0.4251


    dcharge["ILE"] = {}
    dcharge["ILE"]["N"] = -0.4157
    dcharge["ILE"]["CA"] = -0.0597
    dcharge["ILE"]["C"] = 0.5973
    dcharge["ILE"]["O"] = -0.5679
    dcharge["ILE"]["CB"] = 0.1303
    dcharge["ILE"]["CG1"] = -0.0430
    dcharge["ILE"]["CG2"] = -0.3204
    dcharge["ILE"]["CD1"] = -0.0660
    dcharge["ILE"]["H"] = 0.2719
    dcharge["ILE"]["HA"] = 0.0869
    dcharge["ILE"]["HB"] = 0.0187
    dcharge["ILE"]["HG12"] = 0.0236
    dcharge["ILE"]["HG13"] = 0.0236
    dcharge["ILE"]["HG21"] = 0.0882
    dcharge["ILE"]["HG22"] = 0.0882
    dcharge["ILE"]["HG23"] = 0.0882
    dcharge["ILE"]["HD11"] = 0.0186
    dcharge["ILE"]["HD12"] = 0.0186
    dcharge["ILE"]["HD13"] = 0.0186

    dcharge["VAL"] = {}
    dcharge["VAL"]["N"] = -0.4157
    dcharge["VAL"]["CA"] = -0.0875
    dcharge["VAL"]["C"] = 0.5973
    dcharge["VAL"]["O"] = -0.5679
    dcharge["VAL"]["CB"] = 0.2985
    dcharge["VAL"]["CG1"] = -0.3192
    dcharge["VAL"]["CG2"] = -0.3192
    dcharge["VAL"]["H"] = 0.2719
    dcharge["VAL"]["HA"] = 0.0969
    dcharge["VAL"]["HB"] = -0.0297
    dcharge["VAL"]["HG11"] = 0.0791
    dcharge["VAL"]["HG12"] = 0.0791
    dcharge["VAL"]["HG13"] = 0.0791
    dcharge["VAL"]["HG21"] = 0.0791
    dcharge["VAL"]["HG22"] = 0.0791
    dcharge["VAL"]["HG23"] = 0.0791

    
    dcharge["SER"] = {}
    dcharge["SER"]["N"] = -0.4157
    dcharge["SER"]["CA"] = -0.0249
    dcharge["SER"]["C"] = 0.5973
    dcharge["SER"]["O"] = -0.5679
    dcharge["SER"]["CB"] = 0.2117
    dcharge["SER"]["OG"] = -0.6546
    dcharge["SER"]["H"] = 0.2719
    dcharge["SER"]["HA"] = 0.0843
    dcharge["SER"]["HB2"] = 0.0352
    dcharge["SER"]["HB3"] = 0.0352
    dcharge["SER"]["HG"] = 0.4275
 

    
    dcharge["THR"] = {}
    dcharge["THR"]["N"] = -0.4157
    dcharge["THR"]["CA"] = -0.0389
    dcharge["THR"]["C"] = 0.5973
    dcharge["THR"]["O"] = -0.5679
    dcharge["THR"]["CB"] = 0.3654
    dcharge["THR"]["OG1"] = -0.6761
    dcharge["THR"]["CG2"] = -0.2438
    dcharge["THR"]["H"] = 0.2719
    dcharge["THR"]["HA"] = 0.1007
    dcharge["THR"]["HB"] = 0.0043
    dcharge["THR"]["HG1"] = 0.4102
    dcharge["THR"]["HG21"] = 0.0642
    dcharge["THR"]["HG22"] = 0.0642
    dcharge["THR"]["HG23"] = 0.0642



    dcharge["CYS"] = {}
    dcharge["CYS"]["N"] = -0.4157
    dcharge["CYS"]["CA"] = 0.0213
    dcharge["CYS"]["C"] = 0.5973
    dcharge["CYS"]["O"] = -0.5679
    dcharge["CYS"]["CB"] = -0.1231
    dcharge["CYS"]["SG"] = -0.3119
    dcharge["CYS"]["H"] = 0.2719
    dcharge["CYS"]["HA"] = 0.1124
    dcharge["CYS"]["HB1"] = 0.1112
    dcharge["CYS"]["HB2"] = 0.1112
    dcharge["CYS"]["HG"] = 0.1933


    dcharge["PRO"] = {}
    dcharge["PRO"]["N"] = -0.2548
    dcharge["PRO"]["CA"] = -0.0266
    dcharge["PRO"]["C"] = 0.5896
    dcharge["PRO"]["O"] = -0.5748
    dcharge["PRO"]["CB"] = -0.0070
    dcharge["PRO"]["CG"] = 0.0189
    dcharge["PRO"]["CD"] = 0.0192 
    dcharge["PRO"]["HA"] = 0.0641
    dcharge["PRO"]["HB2"] = 0.0253
    dcharge["PRO"]["HB3"] = 0.0253
    dcharge["PRO"]["HG2"] = 0.0213
    dcharge["PRO"]["HG3"] = 0.0213
    dcharge["PRO"]["HD2"] = 0.0391
    dcharge["PRO"]["HD3"] = 0.0391
    


    dcharge["ARG"] = {}
    dcharge["ARG"]["N"] = -0.3479
    dcharge["ARG"]["CA"] = -0.2637
    dcharge["ARG"]["C"] = 0.7341
    dcharge["ARG"]["O"] = -0.5894
    dcharge["ARG"]["CB"] = -0.0007
    dcharge["ARG"]["CG"] = 0.0390
    dcharge["ARG"]["CD"] = 0.0486 
    dcharge["ARG"]["NE"] = -0.5295
    dcharge["ARG"]["CZ"] = 0.8076 
    dcharge["ARG"]["NH1"] = -0.8627 
    dcharge["ARG"]["NH2"] = -0.8627 
    dcharge["ARG"]["H"] = 0.2747
    dcharge["ARG"]["HA"] = 0.1560
    dcharge["ARG"]["HB2"] = 0.0327
    dcharge["ARG"]["HB3"] = 0.0327
    dcharge["ARG"]["HG2"] = 0.0285
    dcharge["ARG"]["HG3"] = 0.0285
    dcharge["ARG"]["HD2"] = 0.0687
    dcharge["ARG"]["HD3"] = 0.0687
    dcharge["ARG"]["HE"] = 0.3456
    dcharge["ARG"]["HH11"] = 0.4478
    dcharge["ARG"]["HH12"] = 0.4478
    dcharge["ARG"]["HH21"] = 0.4478    
    dcharge["ARG"]["HH22"] = 0.4478


    dcharge["LYS"] = {}
    dcharge["LYS"]["N"] = -0.3479
    dcharge["LYS"]["CA"] = -0.2400
    dcharge["LYS"]["C"] = 0.7341
    dcharge["LYS"]["O"] = -0.5894
    dcharge["LYS"]["CB"] = -0.0094
    dcharge["LYS"]["CG"] = 0.0187
    dcharge["LYS"]["CD"] = -0.0479 
    dcharge["LYS"]["CE"] = -0.0143
    dcharge["LYS"]["NZ"] = -0.3854 
    dcharge["LYS"]["H"] = 0.2747
    dcharge["LYS"]["HA"] = 0.1426
    dcharge["LYS"]["HB2"] = 0.0362
    dcharge["LYS"]["HB3"] = 0.0362
    dcharge["LYS"]["HG2"] = 0.0103
    dcharge["LYS"]["HG3"] = 0.0103
    dcharge["LYS"]["HD2"] = 0.0621
    dcharge["LYS"]["HD3"] = 0.0621
    dcharge["LYS"]["HE2"] = 0.1135
    dcharge["LYS"]["HE3"] = 0.1135
    dcharge["LYS"]["HZ2"] = 0.3400
    dcharge["LYS"]["HZ1"] = 0.3400    
    dcharge["LYS"]["HZ3"] = 0.3400

    dcharge["HIS"] = {}
    dcharge["HIS"]["N"] = -0.4157
    dcharge["HIS"]["CA"] = 0.0188
    dcharge["HIS"]["C"] = 0.5973
    dcharge["HIS"]["O"] = -0.5679
    dcharge["HIS"]["CB"] = -0.0462
    dcharge["HIS"]["CG"] = -0.0266
    dcharge["HIS"]["ND1"] = -0.3811 
    dcharge["HIS"]["CE1"] = 0.2057
    dcharge["HIS"]["NE2"] = -0.5727 
    dcharge["HIS"]["CD2"] = 0.1292 
    dcharge["HIS"]["H"] = 0.2719
    dcharge["HIS"]["HA"] = 0.0881
    dcharge["HIS"]["HB2"] = 0.0402
    dcharge["HIS"]["HB3"] = 0.0402
    dcharge["HIS"]["HE1"] = 0.1392
    dcharge["HIS"]["HD1"] = 0.3649
    dcharge["HIS"]["HD2"] = 0.1147


    dcharge["HIE"] = {}
    dcharge["HIE"]["N"] = -0.4157
    dcharge["HIE"]["CA"] = -0.0581
    dcharge["HIE"]["C"] = 0.5973
    dcharge["HIE"]["O"] = -0.5679
    dcharge["HIE"]["CB"] = -0.0074
    dcharge["HIE"]["CG"] = 0.1868
    dcharge["HIE"]["ND1"] = -0.5432 
    dcharge["HIE"]["CE1"] = 0.1635
    dcharge["HIE"]["NE2"] = -0.2795 
    dcharge["HIE"]["CD2"] = -0.2207 
    dcharge["HIE"]["H"] = 0.2719
    dcharge["HIE"]["HA"] = 0.1360
    dcharge["HIE"]["HB2"] = 0.0367
    dcharge["HIE"]["HB3"] = 0.0367
    dcharge["HIE"]["HE1"] = 0.1435
    dcharge["HIE"]["HE2"] = 0.3339
    dcharge["HIE"]["HD2"] = 0.1862

    dcharge["MET"] = {}
    dcharge["MET"]["N"] = -0.4157
    dcharge["MET"]["CA"] = -0.0237
    dcharge["MET"]["C"] = 0.5973
    dcharge["MET"]["O"] = -0.5679
    dcharge["MET"]["CB"] = 0.0342
    dcharge["MET"]["CG"] = 0.0018
    dcharge["MET"]["SD"] = -0.2737 
    dcharge["MET"]["CE"] = -0.0536
    dcharge["MET"]["H"] = 0.2719
    dcharge["MET"]["HA"] = 0.0880
    dcharge["MET"]["HB2"] = 0.0241
    dcharge["MET"]["HB3"] = 0.0241
    dcharge["MET"]["HG2"] = 0.0440
    dcharge["MET"]["HG3"] = 0.0440
    dcharge["MET"]["HE2"] = 0.0684
    dcharge["MET"]["HE3"] = 0.0684
    dcharge["MET"]["HE1"] = 0.0684    



    dcharge["PHE"] = {}
    dcharge["PHE"]["N"] = -0.4157
    dcharge["PHE"]["CA"] = -0.0024
    dcharge["PHE"]["C"] = 0.5973
    dcharge["PHE"]["O"] = -0.5679
    dcharge["PHE"]["CB"] = -0.0343
    dcharge["PHE"]["CG"] = 0.0118
    dcharge["PHE"]["CD1"] = -0.1256 
    dcharge["PHE"]["CD2"] = -0.1256 
    dcharge["PHE"]["CE1"] = -0.1704 
    dcharge["PHE"]["CE2"] = -0.1704
    dcharge["PHE"]["CZ"] = -0.1072 
    dcharge["PHE"]["H"] = 0.2719
    dcharge["PHE"]["HA"] = 0.0978
    dcharge["PHE"]["HB2"] = 0.0295
    dcharge["PHE"]["HB3"] = 0.0295
    dcharge["PHE"]["HD1"] = 0.1330
    dcharge["PHE"]["HD2"] = 0.1330
    dcharge["PHE"]["HE1"] = 0.1430
    dcharge["PHE"]["HE2"] = 0.1430
    dcharge["PHE"]["HZ"] = 0.1297
   

    

    dcharge["TYR"] = {}
    dcharge["TYR"]["N"] = -0.4157
    dcharge["TYR"]["CA"] = -0.0014
    dcharge["TYR"]["C"] = 0.5973
    dcharge["TYR"]["O"] = -0.5679
    dcharge["TYR"]["CB"] = -0.0152
    dcharge["TYR"]["CG"] = -0.0011
    dcharge["TYR"]["CD1"] = -0.1906 
    dcharge["TYR"]["CD2"] = -0.1906 
    dcharge["TYR"]["CE1"] = -0.2341 
    dcharge["TYR"]["CE2"] = -0.2341
    dcharge["TYR"]["CZ"] = 0.3226
    dcharge["TYR"]["OH"] = -0.5579
    dcharge["TYR"]["H"] = 0.2719
    dcharge["TYR"]["HA"] = 0.0876
    dcharge["TYR"]["HB2"] = 0.0295
    dcharge["TYR"]["HB3"] = 0.0295
    dcharge["TYR"]["HD1"] = 0.1699
    dcharge["TYR"]["HD2"] = 0.1699
    dcharge["TYR"]["HE1"] = 0.1656
    dcharge["TYR"]["HE2"] = 0.1656
    dcharge["TYR"]["HH"] = 0.3992



    
    dcharge["TRP"] = {}
    dcharge["TRP"]["N"] = -0.4157
    dcharge["TRP"]["CA"] = -0.0275
    dcharge["TRP"]["C"] = 0.5973
    dcharge["TRP"]["O"] = -0.5679
    dcharge["TRP"]["CB"] = -0.0050
    dcharge["TRP"]["CG"] = -0.1415
    dcharge["TRP"]["CD1"] = -0.1638 
    dcharge["TRP"]["CD2"] = 0.1243 
    dcharge["TRP"]["NE1"] = -0.3418 
    dcharge["TRP"]["CE2"] = 0.1380
    dcharge["TRP"]["CE3"] = -0.2387
    dcharge["TRP"]["CZ2"] = -0.2601
    dcharge["TRP"]["CZ3"] = -0.1972
    dcharge["TRP"]["CH2"] = -0.1134
    dcharge["TRP"]["H"] = 0.2719
    dcharge["TRP"]["HA"] = 0.1123
    dcharge["TRP"]["HB2"] = 0.0339
    dcharge["TRP"]["HB3"] = 0.0339
    dcharge["TRP"]["HD1"] = 0.2062
    dcharge["TRP"]["HE1"] = 0.3412
    dcharge["TRP"]["HE3"] = 0.1700
    dcharge["TRP"]["HZ2"] = 0.1572
    dcharge["TRP"]["HZ3"] = 0.1447
    dcharge["TRP"]["HH2"] = 0.1417

 
    return dcharge

def epsilon_vdw_PDB() :

    # rayon de van der Waals (dvdw) : Ri* selon la nature du residu puis le type d'atome (dico); 
    # profondeur du puit de vdW (depsilon) : esp_i selon la nature du residu puis le type d'atome (dico)

    dR = {}
    dR["C"] = 1.9080
    dR["CA"] = 1.9080
    dR["CM"] = 1.9080
    dR["Cs"] = 3.3950
    dR["CT"] = 1.9080
    dR["H"] = 0.6000
    dR["H1"] = 1.3870
    dR["H2"] = 1.2870
    dR["H3"] = 1.1870
    dR["H4"] = 1.4090
    dR["H5"] = 1.3590
    dR["HA"] = 1.4590
    dR["HC"] = 1.4870
    dR["HO"] = 0.0000
    dR["HP"] = 1.1000
    dR["HS"] = 0.6000
    dR["HW"] = 0.0000
    dR["IP"] = 1.8680
    dR["K"] = 2.6580
    dR["Li"] = 1.1370
    dR["N2m"] = 1.8240
    dR["N3n"] = 1.8750
    dR["O"] = 1.6612
    dR["O2"] = 1.6612
    dR["OH"] = 1.7210
    dR["OS"] = 1.6837
    dR["OW"] = 1.7683
    dR["S"] = 2.0000
    dR["SH"] = 2.0000


    dE = {}
    dE["C"] = 0.0860
    dE["CA"] = 0.0860
    dE["CM"] = 0.0860
    dE["Cs"] = 0.0000806
    dE["CT"] = 0.1094
    dE["H"] = 0.0157
    dE["H1"] = 0.0157
    dE["H2"] = 0.0157
    dE["H3"] = 0.0157
    dE["H4"] = 0.0150
    dE["H5"] = 0.0150
    dE["HA"] = 0.0150
    dE["HC"] = 0.0157
    dE["HO"] = 0.0000
    dE["HP"] = 0.0157
    dE["HS"] = 0.0157
    dE["HW"] = 0.0000
    dE["IP"] = 0.00277
    dE["K"] = 0.000328
    dE["Li"] = 0.0183
    dE["N2m"] = 0.1700
    dE["N3n"] = 0.1700
    dE["O"] = 0.2100
    dE["O2"] = 0.2100
    dE["OH"] = 0.2104
    dE["OS"] = 0.1700
    dE["OW"] = 0.1520
    dE["S"] = 0.2500
    dE["SH"] = 0.2500



    # vdw radius

    dvdw = {}
    dvdw["GLY"] = {}
    dvdw["GLY"]["N"] = dR["N2m"]
    dvdw["GLY"]["CA"] = dR["CT"]
    dvdw["GLY"]["C"] = dR["C"]
    dvdw["GLY"]["O"] = dR["O"]
    dvdw["GLY"]["H"] = dR["H"]
    dvdw["GLY"]["HA2"] = dR["H1"]
    dvdw["GLY"]["HA3"] = dR["H1"]
    
    dvdw["ALA"] = {}
    dvdw["ALA"]["N"] = dR["N2m"]
    dvdw["ALA"]["CA"] = dR["CT"]
    dvdw["ALA"]["C"] = dR["C"]
    dvdw["ALA"]["O"] = dR["O"]
    dvdw["ALA"]["CB"] = dR["CT"]
    dvdw["ALA"]["H"] = dR["H"]
    dvdw["ALA"]["HB1"] = dR["HC"]
    dvdw["ALA"]["HB2"] = dR["HC"]
    dvdw["ALA"]["HB3"] = dR["HC"]
    dvdw["ALA"]["HA"] = dR["H1"]

    dvdw["ASP"] = {}
    dvdw["ASP"]["N"] = dR["N2m"]
    dvdw["ASP"]["CA"] = dR["CT"]
    dvdw["ASP"]["C"] = dR["C"]
    dvdw["ASP"]["O"] = dR["O"]
    dvdw["ASP"]["CB"] = dR["CT"]
    dvdw["ASP"]["CG"] = dR["C"]
    dvdw["ASP"]["OD1"] = dR["O2"]
    dvdw["ASP"]["OD2"] = dR["O2"]
    dvdw["ASP"]["H"] = dR["H"]
    dvdw["ASP"]["HA"] = dR["H1"]
    dvdw["ASP"]["HB2"] = dR["HC"]
    dvdw["ASP"]["HB3"] = dR["HC"]


    dvdw["GLU"] = {}
    dvdw["GLU"]["N"] = dR["N2m"]
    dvdw["GLU"]["CA"] = dR["CT"]
    dvdw["GLU"]["C"] = dR["C"]
    dvdw["GLU"]["O"] = dR["O"]
    dvdw["GLU"]["CB"] = dR["CT"]
    dvdw["GLU"]["CG"] = dR["CT"]
    dvdw["GLU"]["CD"] = dR["C"]
    dvdw["GLU"]["OE1"] = dR["O2"]
    dvdw["GLU"]["OE2"] = dR["O2"]
    dvdw["GLU"]["H"] = dR["H"]
    dvdw["GLU"]["HA"] = dR["H1"]
    dvdw["GLU"]["HB2"] = dR["HC"]
    dvdw["GLU"]["HB3"] = dR["HC"]
    dvdw["GLU"]["HG2"] = dR["HC"]
    dvdw["GLU"]["HG3"] = dR["HC"]


    dvdw["LEU"] = {}
    dvdw["LEU"]["N"] = dR["N2m"]
    dvdw["LEU"]["CA"] = dR["CT"]
    dvdw["LEU"]["C"] = dR["C"]
    dvdw["LEU"]["O"] = dR["O"]
    dvdw["LEU"]["CB"] = dR["CT"]
    dvdw["LEU"]["CG"] = dR["CT"]
    dvdw["LEU"]["CD1"] = dR["CT"]
    dvdw["LEU"]["CD2"] = dR["CT"]
    dvdw["LEU"]["H"] = dR["H"]
    dvdw["LEU"]["HA"] = dR["H1"]
    dvdw["LEU"]["HB2"] = dR["HC"]
    dvdw["LEU"]["HB3"] = dR["HC"]
    dvdw["LEU"]["HG"] = dR["HC"]
    dvdw["LEU"]["HD11"] = dR["HC"]
    dvdw["LEU"]["HD12"] = dR["HC"]
    dvdw["LEU"]["HD13"] = dR["HC"]
    dvdw["LEU"]["HD21"] = dR["HC"]
    dvdw["LEU"]["HD22"] = dR["HC"]
    dvdw["LEU"]["HD23"] = dR["HC"]
    
    dvdw["ASN"] = {}
    dvdw["ASN"]["N"] = dR["N2m"]
    dvdw["ASN"]["CA"] = dR["CT"]
    dvdw["ASN"]["C"] = dR["C"]
    dvdw["ASN"]["O"] = dR["O"]
    dvdw["ASN"]["CB"] = dR["CT"]
    dvdw["ASN"]["CG"] = dR["C"]
    dvdw["ASN"]["ND2"] = dR["N2m"]
    dvdw["ASN"]["OD1"] = dR["O"]
    dvdw["ASN"]["H"] = dR["H"]
    dvdw["ASN"]["HA"] = dR["H1"]
    dvdw["ASN"]["HB2"] = dR["HC"]
    dvdw["ASN"]["HB3"] = dR["HC"]
    dvdw["ASN"]["HD21"] = dR["H"]
    dvdw["ASN"]["HD22"] = dR["H"]


    dvdw["GLN"] = {}
    dvdw["GLN"]["N"] = dR["N2m"]
    dvdw["GLN"]["CA"] = dR["CT"]
    dvdw["GLN"]["C"] = dR["C"]
    dvdw["GLN"]["O"] = dR["O"]
    dvdw["GLN"]["CB"] = dR["CT"]
    dvdw["GLN"]["CG"] = dR["CT"]
    dvdw["GLN"]["CD"] = dR["C"]
    dvdw["GLN"]["NE2"] = dR["N2m"]
    dvdw["GLN"]["OE1"] = dR["O"]
    dvdw["GLN"]["H"] = dR["H"]
    dvdw["GLN"]["HA"] = dR["H1"]
    dvdw["GLN"]["HB2"] = dR["HC"]
    dvdw["GLN"]["HB3"] = dR["HC"]
    dvdw["GLN"]["HG2"] = dR["HC"]
    dvdw["GLN"]["HG3"] = dR["HC"]
    dvdw["GLN"]["HE21"] = dR["H"]
    dvdw["GLN"]["HE22"] = dR["H"]


    dvdw["ILE"] = {}
    dvdw["ILE"]["N"] = dR["N2m"]
    dvdw["ILE"]["CA"] = dR["CT"]
    dvdw["ILE"]["C"] = dR["C"]
    dvdw["ILE"]["O"] = dR["O"]
    dvdw["ILE"]["CB"] = dR["CT"]
    dvdw["ILE"]["CG1"] = dR["CT"]
    dvdw["ILE"]["CG2"] = dR["CT"]
    dvdw["ILE"]["CD1"] = dR["CT"]
    dvdw["ILE"]["H"] = dR["H"]
    dvdw["ILE"]["HA"] = dR["H1"]
    dvdw["ILE"]["HB"] = dR["HC"]
    dvdw["ILE"]["HG12"] = dR["HC"]
    dvdw["ILE"]["HG13"] = dR["HC"]
    dvdw["ILE"]["HG21"] = dR["HC"]
    dvdw["ILE"]["HG22"] = dR["HC"]
    dvdw["ILE"]["HG23"] = dR["HC"]
    dvdw["ILE"]["HD11"] = dR["HC"]
    dvdw["ILE"]["HD12"] = dR["HC"]
    dvdw["ILE"]["HD13"] = dR["HC"]

    dvdw["VAL"] = {}
    dvdw["VAL"]["N"] = dR["N2m"]
    dvdw["VAL"]["CA"] = dR["CT"]
    dvdw["VAL"]["C"] = dR["C"]
    dvdw["VAL"]["O"] = dR["O"]
    dvdw["VAL"]["CB"] = dR["CT"]
    dvdw["VAL"]["CG1"] = dR["CT"]
    dvdw["VAL"]["CG2"] = dR["CT"]
    dvdw["VAL"]["H"] = dR["H"]
    dvdw["VAL"]["HA"] = dR["H1"]
    dvdw["VAL"]["HB"] = dR["HC"]
    dvdw["VAL"]["HG11"] = dR["HC"]
    dvdw["VAL"]["HG12"] = dR["HC"]
    dvdw["VAL"]["HG13"] = dR["HC"]
    dvdw["VAL"]["HG21"] = dR["HC"]
    dvdw["VAL"]["HG22"] = dR["HC"]
    dvdw["VAL"]["HG23"] = dR["HC"]

    
    dvdw["SER"] = {}
    dvdw["SER"]["N"] = dR["N2m"]
    dvdw["SER"]["CA"] = dR["CT"]
    dvdw["SER"]["C"] = dR["C"]
    dvdw["SER"]["O"] = dR["O"]
    dvdw["SER"]["CB"] = dR["CT"]
    dvdw["SER"]["OG"] = dR["OH"]
    dvdw["SER"]["H"] = dR["H"]
    dvdw["SER"]["HA"] = dR["H1"]
    dvdw["SER"]["HB2"] = dR["H1"]
    dvdw["SER"]["HB3"] = dR["H1"]
    dvdw["SER"]["HG"] = dR["HO"]
 

    
    dvdw["THR"] = {}
    dvdw["THR"]["N"] = dR["N2m"]
    dvdw["THR"]["CA"] = dR["CT"]
    dvdw["THR"]["C"] = dR["C"]
    dvdw["THR"]["O"] = dR["O"]
    dvdw["THR"]["CB"] = dR["CT"]
    dvdw["THR"]["OG1"] = dR["OH"]
    dvdw["THR"]["CG2"] = dR["CT"]
    dvdw["THR"]["H"] = dR["H"]
    dvdw["THR"]["HA"] = dR["H1"]
    dvdw["THR"]["HB"] = dR["H1"]
    dvdw["THR"]["HG1"] = dR["HO"]
    dvdw["THR"]["HG21"] = dR["HC"]
    dvdw["THR"]["HG22"] = dR["HC"]
    dvdw["THR"]["HG23"] = dR["HC"]



    dvdw["CYS"] = {}
    dvdw["CYS"]["N"] = dR["N2m"]
    dvdw["CYS"]["CA"] = dR["CT"]
    dvdw["CYS"]["C"] = dR["C"]
    dvdw["CYS"]["O"] = dR["O"]
    dvdw["CYS"]["CB"] = dR["CT"]
    dvdw["CYS"]["SG"] = dR["SH"]
    dvdw["CYS"]["H"] = dR["H"]
    dvdw["CYS"]["HA"] = dR["H1"]
    dvdw["CYS"]["HB1"] = dR["H1"]
    dvdw["CYS"]["HB2"] = dR["H1"]
    dvdw["CYS"]["HG"] = dR["HS"]


    dvdw["PRO"] = {}
    dvdw["PRO"]["N"] = dR["N2m"]
    dvdw["PRO"]["CA"] = dR["CT"]
    dvdw["PRO"]["C"] = dR["C"]
    dvdw["PRO"]["O"] = dR["O"]
    dvdw["PRO"]["CB"] = dR["CT"]
    dvdw["PRO"]["CG"] = dR["CT"]
    dvdw["PRO"]["CD"] = dR["CT"]
    dvdw["PRO"]["HA"] = dR["H1"]
    dvdw["PRO"]["HB2"] = dR["HC"]
    dvdw["PRO"]["HB3"] = dR["HC"]
    dvdw["PRO"]["HG2"] = dR["HC"]
    dvdw["PRO"]["HG3"] = dR["HC"]
    dvdw["PRO"]["HD2"] = dR["H1"]
    dvdw["PRO"]["HD3"] = dR["H1"]
    


    dvdw["ARG"] = {}
    dvdw["ARG"]["N"] = dR["N2m"]
    dvdw["ARG"]["CA"] = dR["CT"]
    dvdw["ARG"]["C"] = dR["C"]
    dvdw["ARG"]["O"] = dR["O"]
    dvdw["ARG"]["CB"] = dR["CT"]
    dvdw["ARG"]["CG"] = dR["CT"]
    dvdw["ARG"]["CD"] = dR["CT"]
    dvdw["ARG"]["NE"] = dR["N2m"]
    dvdw["ARG"]["CZ"] = dR["CA"]
    dvdw["ARG"]["NH1"] = dR["N2m"]
    dvdw["ARG"]["NH2"] = dR["N2m"]
    dvdw["ARG"]["H"] = dR["H"]
    dvdw["ARG"]["HA"] = dR["H1"]
    dvdw["ARG"]["HB2"] = dR["HC"]
    dvdw["ARG"]["HB3"] = dR["HC"]
    dvdw["ARG"]["HG2"] = dR["HC"]
    dvdw["ARG"]["HG3"] = dR["HC"]
    dvdw["ARG"]["HD2"] = dR["H1"]
    dvdw["ARG"]["HD3"] = dR["H1"]
    dvdw["ARG"]["HE"] = dR["H"]
    dvdw["ARG"]["HH11"] = dR["H"]
    dvdw["ARG"]["HH12"] = dR["H"]
    dvdw["ARG"]["HH21"] = dR["H"]  
    dvdw["ARG"]["HH22"] = dR["H"]


    dvdw["LYS"] = {}
    dvdw["LYS"]["N"] = dR["N2m"]
    dvdw["LYS"]["CA"] = dR["CT"]
    dvdw["LYS"]["C"] = dR["C"]
    dvdw["LYS"]["O"] = dR["O"]
    dvdw["LYS"]["CB"] = dR["CT"]
    dvdw["LYS"]["CG"] = dR["CT"]
    dvdw["LYS"]["CD"] = dR["CT"] 
    dvdw["LYS"]["CE"] = dR["CT"]
    dvdw["LYS"]["NZ"] = dR["N3n"] 
    dvdw["LYS"]["H"] = dR["H"]
    dvdw["LYS"]["HA"] = dR["H1"]
    dvdw["LYS"]["HB2"] = dR["HC"]
    dvdw["LYS"]["HB3"] = dR["HC"]
    dvdw["LYS"]["HG2"] = dR["HC"]
    dvdw["LYS"]["HG3"] = dR["HC"]
    dvdw["LYS"]["HD2"] = dR["HC"]
    dvdw["LYS"]["HD3"] = dR["HC"]
    dvdw["LYS"]["HE2"] = dR["HP"]
    dvdw["LYS"]["HE3"] = dR["HP"]
    dvdw["LYS"]["HZ2"] = dR["H"]
    dvdw["LYS"]["HZ1"] = dR["H"]   
    dvdw["LYS"]["HZ3"] = dR["H"]


    dvdw["HIE"] = {}
    dvdw["HIE"]["N"] = dR["N2m"]
    dvdw["HIE"]["CA"] = dR["CT"]
    dvdw["HIE"]["C"] = dR["C"]
    dvdw["HIE"]["O"] = dR["O"]
    dvdw["HIE"]["CB"] = dR["CT"]
    dvdw["HIE"]["CG"] = dR["CA"]
    dvdw["HIE"]["ND1"] = dR["N2m"]
    dvdw["HIE"]["CE1"] = dR["CA"]
    dvdw["HIE"]["NE2"] = dR["N2m"]
    dvdw["HIE"]["CD2"] = dR["CA"]
    dvdw["HIE"]["H"] = dR["H"]
    dvdw["HIE"]["HA"] = dR["H1"]
    dvdw["HIE"]["HB2"] = dR["HC"]
    dvdw["HIE"]["HB3"] = dR["HC"]
    dvdw["HIE"]["HE1"] = dR["H5"]
    dvdw["HIE"]["HE2"] = dR["H"]
    dvdw["HIE"]["HD2"] = dR["H4"]

    dvdw["HIS"] = {}
    dvdw["HIS"]["N"] = dR["N2m"]
    dvdw["HIS"]["CA"] = dR["CT"]
    dvdw["HIS"]["C"] = dR["C"]
    dvdw["HIS"]["O"] = dR["O"]
    dvdw["HIS"]["CB"] = dR["CT"]
    dvdw["HIS"]["CG"] = dR["CA"]
    dvdw["HIS"]["ND1"] = dR["N2m"]
    dvdw["HIS"]["CE1"] = dR["CA"]
    dvdw["HIS"]["NE2"] = dR["N2m"]
    dvdw["HIS"]["CD2"] = dR["CA"]
    dvdw["HIS"]["H"] = dR["H"]
    dvdw["HIS"]["HA"] = dR["H1"]
    dvdw["HIS"]["HB2"] = dR["HC"]
    dvdw["HIS"]["HB3"] = dR["HC"]
    dvdw["HIS"]["HE1"] = dR["H5"]
    dvdw["HIS"]["HD1"] = dR["H"]
    dvdw["HIS"]["HD2"] = dR["H4"]

    dvdw["MET"] = {}
    dvdw["MET"]["N"] = dR["N2m"]
    dvdw["MET"]["CA"] = dR["CT"]
    dvdw["MET"]["C"] = dR["C"]
    dvdw["MET"]["O"] = dR["O"]
    dvdw["MET"]["CB"] = dR["CT"]
    dvdw["MET"]["CG"] = dR["CT"]
    dvdw["MET"]["SD"] = dR["S"]
    dvdw["MET"]["CE"] = dR["CT"]
    dvdw["MET"]["H"] = dR["H"]
    dvdw["MET"]["HA"] = dR["H1"]
    dvdw["MET"]["HB2"] = dR["HC"]
    dvdw["MET"]["HB3"] = dR["HC"]
    dvdw["MET"]["HG2"] = dR["H1"]
    dvdw["MET"]["HG3"] = dR["H1"]
    dvdw["MET"]["HE2"] = dR["H1"]
    dvdw["MET"]["HE3"] = dR["H1"]
    dvdw["MET"]["HE1"] = dR["H1"]



    dvdw["PHE"] = {}
    dvdw["PHE"]["N"] = dR["N2m"]
    dvdw["PHE"]["CA"] = dR["CT"]
    dvdw["PHE"]["C"] = dR["C"]
    dvdw["PHE"]["O"] = dR["O"]
    dvdw["PHE"]["CB"] = dR["CT"]
    dvdw["PHE"]["CG"] = dR["CA"]
    dvdw["PHE"]["CD1"] = dR["CA"]
    dvdw["PHE"]["CD2"] = dR["CA"]
    dvdw["PHE"]["CE1"] = dR["CA"]
    dvdw["PHE"]["CE2"] = dR["CA"]
    dvdw["PHE"]["CZ"] = dR["CA"]
    dvdw["PHE"]["H"] = dR["H"]
    dvdw["PHE"]["HA"] = dR["H1"]
    dvdw["PHE"]["HB2"] = dR["HC"]
    dvdw["PHE"]["HB3"] = dR["HC"]
    dvdw["PHE"]["HD1"] = dR["HA"]
    dvdw["PHE"]["HD2"] = dR["HA"]
    dvdw["PHE"]["HE1"] = dR["HA"]
    dvdw["PHE"]["HE2"] = dR["HA"]
    dvdw["PHE"]["HZ"] = dR["HA"]
   

    

    dvdw["TYR"] = {}
    dvdw["TYR"]["N"] = dR["N2m"]
    dvdw["TYR"]["CA"] = dR["CT"]
    dvdw["TYR"]["C"] = dR["C"]
    dvdw["TYR"]["O"] = dR["O"]
    dvdw["TYR"]["CB"] = dR["CT"]
    dvdw["TYR"]["CG"] = dR["CA"]
    dvdw["TYR"]["CD1"] =  dR["CA"]
    dvdw["TYR"]["CD2"] =  dR["CA"]
    dvdw["TYR"]["CE1"] = dR["CA"]
    dvdw["TYR"]["CE2"] = dR["CA"]
    dvdw["TYR"]["CZ"] = dR["CA"]
    dvdw["TYR"]["OH"] = dR["OH"]
    dvdw["TYR"]["H"] = dR["H"]
    dvdw["TYR"]["HA"] = dR["H1"]
    dvdw["TYR"]["HB2"] = dR["HC"]
    dvdw["TYR"]["HB3"] = dR["HC"]
    dvdw["TYR"]["HD1"] = dR["HA"]
    dvdw["TYR"]["HD2"] = dR["HA"]
    dvdw["TYR"]["HE1"] = dR["HA"]
    dvdw["TYR"]["HE2"] = dR["HA"]
    dvdw["TYR"]["HH"] = dR["HO"]



    
    dvdw["TRP"] = {}
    dvdw["TRP"]["N"] = dR["N2m"]
    dvdw["TRP"]["CA"] = dR["CT"]
    dvdw["TRP"]["C"] = dR["C"]
    dvdw["TRP"]["O"] = dR["O"]
    dvdw["TRP"]["CB"] = dR["CT"]
    dvdw["TRP"]["CG"] = dR["CA"]
    dvdw["TRP"]["CD1"] = dR["CA"]
    dvdw["TRP"]["CD2"] = dR["CA"]
    dvdw["TRP"]["NE1"] = dR["N2m"]
    dvdw["TRP"]["CE2"] = dR["CA"]
    dvdw["TRP"]["CE3"] = dR["CA"]
    dvdw["TRP"]["CZ2"] = dR["CA"]
    dvdw["TRP"]["CZ3"] = dR["CA"]
    dvdw["TRP"]["CH2"] = dR["CA"]
    dvdw["TRP"]["H"] = dR["H"]
    dvdw["TRP"]["HA"] = dR["H1"]
    dvdw["TRP"]["HB2"] = dR["HC"]
    dvdw["TRP"]["HB3"] = dR["HC"]
    dvdw["TRP"]["HD1"] = dR["H4"]
    dvdw["TRP"]["HE1"] = dR["H"]
    dvdw["TRP"]["HE3"] = dR["HA"]
    dvdw["TRP"]["HZ2"] = dR["HA"]
    dvdw["TRP"]["HZ3"] = dR["HA"]
    dvdw["TRP"]["HH2"] = dR["HA"]

 




    # epsilon

    depsilon = {}
    depsilon["GLY"] = {}
    depsilon["GLY"]["N"] = dE["N2m"]
    depsilon["GLY"]["CA"] = dE["CT"]
    depsilon["GLY"]["C"] = dE["C"]
    depsilon["GLY"]["O"] = dE["O"]
    depsilon["GLY"]["H"] = dE["H"]
    depsilon["GLY"]["HA2"] = dE["H1"]
    depsilon["GLY"]["HA3"] = dE["H1"]
    
    depsilon["ALA"] = {}
    depsilon["ALA"]["N"] = dE["N2m"]
    depsilon["ALA"]["CA"] = dE["CT"]
    depsilon["ALA"]["C"] = dE["C"]
    depsilon["ALA"]["O"] = dE["O"]
    depsilon["ALA"]["CB"] = dE["CT"]
    depsilon["ALA"]["H"] = dE["H"]
    depsilon["ALA"]["HB1"] = dE["HC"]
    depsilon["ALA"]["HB2"] = dE["HC"]
    depsilon["ALA"]["HB3"] = dE["HC"]
    depsilon["ALA"]["HA"] = dE["H1"]

    depsilon["ASP"] = {}
    depsilon["ASP"]["N"] = dE["N2m"]
    depsilon["ASP"]["CA"] = dE["CT"]
    depsilon["ASP"]["C"] = dE["C"]
    depsilon["ASP"]["O"] = dE["O"]
    depsilon["ASP"]["CB"] = dE["CT"]
    depsilon["ASP"]["CG"] = dE["C"]
    depsilon["ASP"]["OD1"] = dE["O2"]
    depsilon["ASP"]["OD2"] = dE["O2"]
    depsilon["ASP"]["H"] = dE["H"]
    depsilon["ASP"]["HA"] = dE["H1"]
    depsilon["ASP"]["HB2"] = dE["HC"]
    depsilon["ASP"]["HB3"] = dE["HC"]


    depsilon["GLU"] = {}
    depsilon["GLU"]["N"] = dE["N2m"]
    depsilon["GLU"]["CA"] = dE["CT"]
    depsilon["GLU"]["C"] = dE["C"]
    depsilon["GLU"]["O"] = dE["O"]
    depsilon["GLU"]["CB"] = dE["CT"]
    depsilon["GLU"]["CG"] = dE["CT"]
    depsilon["GLU"]["CD"] = dE["C"]
    depsilon["GLU"]["OE1"] = dE["O2"]
    depsilon["GLU"]["OE2"] = dE["O2"]
    depsilon["GLU"]["H"] = dE["H"]
    depsilon["GLU"]["HA"] = dE["H1"]
    depsilon["GLU"]["HB2"] = dE["HC"]
    depsilon["GLU"]["HB3"] = dE["HC"]
    depsilon["GLU"]["HG2"] = dE["HC"]
    depsilon["GLU"]["HG3"] = dE["HC"]


    depsilon["LEU"] = {}
    depsilon["LEU"]["N"] = dE["N2m"]
    depsilon["LEU"]["CA"] = dE["CT"]
    depsilon["LEU"]["C"] = dE["C"]
    depsilon["LEU"]["O"] = dE["O"]
    depsilon["LEU"]["CB"] = dE["CT"]
    depsilon["LEU"]["CG"] = dE["CT"]
    depsilon["LEU"]["CD1"] = dE["CT"]
    depsilon["LEU"]["CD2"] = dE["CT"]
    depsilon["LEU"]["H"] = dE["H"]
    depsilon["LEU"]["HA"] = dE["H1"]
    depsilon["LEU"]["HB2"] = dE["HC"]
    depsilon["LEU"]["HB3"] = dE["HC"]
    depsilon["LEU"]["HG"] = dE["HC"]
    depsilon["LEU"]["HD11"] = dE["HC"]
    depsilon["LEU"]["HD12"] = dE["HC"]
    depsilon["LEU"]["HD13"] = dE["HC"]
    depsilon["LEU"]["HD21"] = dE["HC"]
    depsilon["LEU"]["HD22"] = dE["HC"]
    depsilon["LEU"]["HD23"] = dE["HC"]
    
    depsilon["ASN"] = {}
    depsilon["ASN"]["N"] = dE["N2m"]
    depsilon["ASN"]["CA"] = dE["CT"]
    depsilon["ASN"]["C"] = dE["C"]
    depsilon["ASN"]["O"] = dE["O"]
    depsilon["ASN"]["CB"] = dE["CT"]
    depsilon["ASN"]["CG"] = dE["C"]
    depsilon["ASN"]["ND2"] = dE["N2m"]
    depsilon["ASN"]["OD1"] = dE["O"]
    depsilon["ASN"]["H"] = dE["H"]
    depsilon["ASN"]["HA"] = dE["H1"]
    depsilon["ASN"]["HB2"] = dE["HC"]
    depsilon["ASN"]["HB3"] = dE["HC"]
    depsilon["ASN"]["HD21"] = dE["H"]
    depsilon["ASN"]["HD22"] = dE["H"]


    depsilon["GLN"] = {}
    depsilon["GLN"]["N"] = dE["N2m"]
    depsilon["GLN"]["CA"] = dE["CT"]
    depsilon["GLN"]["C"] = dE["C"]
    depsilon["GLN"]["O"] = dE["O"]
    depsilon["GLN"]["CB"] = dE["CT"]
    depsilon["GLN"]["CG"] = dE["CT"]
    depsilon["GLN"]["CD"] = dE["C"]
    depsilon["GLN"]["NE2"] = dE["N2m"]
    depsilon["GLN"]["OE1"] = dE["O"]
    depsilon["GLN"]["H"] = dE["H"]
    depsilon["GLN"]["HA"] = dE["H1"]
    depsilon["GLN"]["HB2"] = dE["HC"]
    depsilon["GLN"]["HB3"] = dE["HC"]
    depsilon["GLN"]["HG2"] = dE["HC"]
    depsilon["GLN"]["HG3"] = dE["HC"]
    depsilon["GLN"]["HE21"] = dE["H"]
    depsilon["GLN"]["HE22"] = dE["H"]


    depsilon["ILE"] = {}
    depsilon["ILE"]["N"] = dE["N2m"]
    depsilon["ILE"]["CA"] = dE["CT"]
    depsilon["ILE"]["C"] = dE["C"]
    depsilon["ILE"]["O"] = dE["O"]
    depsilon["ILE"]["CB"] = dE["CT"]
    depsilon["ILE"]["CG1"] = dE["CT"]
    depsilon["ILE"]["CG2"] = dE["CT"]
    depsilon["ILE"]["CD1"] = dE["CT"]
    depsilon["ILE"]["H"] = dE["H"]
    depsilon["ILE"]["HA"] = dE["H1"]
    depsilon["ILE"]["HB"] = dE["HC"]
    depsilon["ILE"]["HG12"] = dE["HC"]
    depsilon["ILE"]["HG13"] = dE["HC"]
    depsilon["ILE"]["HG21"] = dE["HC"]
    depsilon["ILE"]["HG22"] = dE["HC"]
    depsilon["ILE"]["HG23"] = dE["HC"]
    depsilon["ILE"]["HD11"] = dE["HC"]
    depsilon["ILE"]["HD12"] = dE["HC"]
    depsilon["ILE"]["HD13"] = dE["HC"]

    depsilon["VAL"] = {}
    depsilon["VAL"]["N"] = dE["N2m"]
    depsilon["VAL"]["CA"] = dE["CT"]
    depsilon["VAL"]["C"] = dE["C"]
    depsilon["VAL"]["O"] = dE["O"]
    depsilon["VAL"]["CB"] = dE["CT"]
    depsilon["VAL"]["CG1"] = dE["CT"]
    depsilon["VAL"]["CG2"] = dE["CT"]
    depsilon["VAL"]["H"] = dE["H"]
    depsilon["VAL"]["HA"] = dE["H1"]
    depsilon["VAL"]["HB"] = dE["HC"]
    depsilon["VAL"]["HG11"] = dE["HC"]
    depsilon["VAL"]["HG12"] = dE["HC"]
    depsilon["VAL"]["HG13"] = dE["HC"]
    depsilon["VAL"]["HG21"] = dE["HC"]
    depsilon["VAL"]["HG22"] = dE["HC"]
    depsilon["VAL"]["HG23"] = dE["HC"]

    
    depsilon["SER"] = {}
    depsilon["SER"]["N"] = dE["N2m"]
    depsilon["SER"]["CA"] = dE["CT"]
    depsilon["SER"]["C"] = dE["C"]
    depsilon["SER"]["O"] = dE["O"]
    depsilon["SER"]["CB"] = dE["CT"]
    depsilon["SER"]["OG"] = dE["OH"]
    depsilon["SER"]["H"] = dE["H"]
    depsilon["SER"]["HA"] = dE["H1"]
    depsilon["SER"]["HB2"] = dE["H1"]
    depsilon["SER"]["HB3"] = dE["H1"]
    depsilon["SER"]["HG"] = dE["HO"]
 

    
    depsilon["THR"] = {}
    depsilon["THR"]["N"] = dE["N2m"]
    depsilon["THR"]["CA"] = dE["CT"]
    depsilon["THR"]["C"] = dE["C"]
    depsilon["THR"]["O"] = dE["O"]
    depsilon["THR"]["CB"] = dE["CT"]
    depsilon["THR"]["OG1"] = dE["OH"]
    depsilon["THR"]["CG2"] = dE["CT"]
    depsilon["THR"]["H"] = dE["H"]
    depsilon["THR"]["HA"] = dE["H1"]
    depsilon["THR"]["HB"] = dE["H1"]
    depsilon["THR"]["HG1"] = dE["HO"]
    depsilon["THR"]["HG21"] = dE["HC"]
    depsilon["THR"]["HG22"] = dE["HC"]
    depsilon["THR"]["HG23"] = dE["HC"]



    depsilon["CYS"] = {}
    depsilon["CYS"]["N"] = dE["N2m"]
    depsilon["CYS"]["CA"] = dE["CT"]
    depsilon["CYS"]["C"] = dE["C"]
    depsilon["CYS"]["O"] = dE["O"]
    depsilon["CYS"]["CB"] = dE["CT"]
    depsilon["CYS"]["SG"] = dE["SH"]
    depsilon["CYS"]["H"] = dE["H"]
    depsilon["CYS"]["HA"] = dE["H1"]
    depsilon["CYS"]["HB1"] = dE["H1"]
    depsilon["CYS"]["HB2"] = dE["H1"]
    depsilon["CYS"]["HG"] = dE["HS"]


    depsilon["PRO"] = {}
    depsilon["PRO"]["N"] = dE["N2m"]
    depsilon["PRO"]["CA"] = dE["CT"]
    depsilon["PRO"]["C"] = dE["C"]
    depsilon["PRO"]["O"] = dE["O"]
    depsilon["PRO"]["CB"] = dE["CT"]
    depsilon["PRO"]["CG"] = dE["CT"]
    depsilon["PRO"]["CD"] = dE["CT"]
    depsilon["PRO"]["HA"] = dE["H1"]
    depsilon["PRO"]["HB2"] = dE["HC"]
    depsilon["PRO"]["HB3"] = dE["HC"]
    depsilon["PRO"]["HG2"] = dE["HC"]
    depsilon["PRO"]["HG3"] = dE["HC"]
    depsilon["PRO"]["HD2"] = dE["H1"]
    depsilon["PRO"]["HD3"] = dE["H1"]
    


    depsilon["ARG"] = {}
    depsilon["ARG"]["N"] = dE["N2m"]
    depsilon["ARG"]["CA"] = dE["CT"]
    depsilon["ARG"]["C"] = dE["C"]
    depsilon["ARG"]["O"] = dE["O"]
    depsilon["ARG"]["CB"] = dE["CT"]
    depsilon["ARG"]["CG"] = dE["CT"]
    depsilon["ARG"]["CD"] = dE["CT"]
    depsilon["ARG"]["NE"] = dE["N2m"]
    depsilon["ARG"]["CZ"] = dE["CA"]
    depsilon["ARG"]["NH1"] = dE["N2m"]
    depsilon["ARG"]["NH2"] = dE["N2m"]
    depsilon["ARG"]["H"] = dE["H"]
    depsilon["ARG"]["HA"] = dE["H1"]
    depsilon["ARG"]["HB2"] = dE["HC"]
    depsilon["ARG"]["HB3"] = dE["HC"]
    depsilon["ARG"]["HG2"] = dE["HC"]
    depsilon["ARG"]["HG3"] = dE["HC"]
    depsilon["ARG"]["HD2"] = dE["H1"]
    depsilon["ARG"]["HD3"] = dE["H1"]
    depsilon["ARG"]["HE"] = dE["H"]
    depsilon["ARG"]["HH11"] = dE["H"]
    depsilon["ARG"]["HH12"] = dE["H"]
    depsilon["ARG"]["HH21"] = dE["H"]  
    depsilon["ARG"]["HH22"] = dE["H"]


    depsilon["LYS"] = {}
    depsilon["LYS"]["N"] = dE["N2m"]
    depsilon["LYS"]["CA"] = dE["CT"]
    depsilon["LYS"]["C"] = dE["C"]
    depsilon["LYS"]["O"] = dE["O"]
    depsilon["LYS"]["CB"] = dE["CT"]
    depsilon["LYS"]["CG"] = dE["CT"]
    depsilon["LYS"]["CD"] = dE["CT"] 
    depsilon["LYS"]["CE"] = dE["CT"]
    depsilon["LYS"]["NZ"] = dE["N3n"] 
    depsilon["LYS"]["H"] = dE["H"]
    depsilon["LYS"]["HA"] = dE["H1"]
    depsilon["LYS"]["HB2"] = dE["HC"]
    depsilon["LYS"]["HB3"] = dE["HC"]
    depsilon["LYS"]["HG2"] = dE["HC"]
    depsilon["LYS"]["HG3"] = dE["HC"]
    depsilon["LYS"]["HD2"] = dE["HC"]
    depsilon["LYS"]["HD3"] = dE["HC"]
    depsilon["LYS"]["HE2"] = dE["HP"]
    depsilon["LYS"]["HE3"] = dE["HP"]
    depsilon["LYS"]["HZ2"] = dE["H"]
    depsilon["LYS"]["HZ1"] = dE["H"]   
    depsilon["LYS"]["HZ3"] = dE["H"]


    depsilon["HIE"] = {}
    depsilon["HIE"]["N"] = dE["N2m"]
    depsilon["HIE"]["CA"] = dE["CT"]
    depsilon["HIE"]["C"] = dE["C"]
    depsilon["HIE"]["O"] = dE["O"]
    depsilon["HIE"]["CB"] = dE["CT"]
    depsilon["HIE"]["CG"] = dE["CA"]
    depsilon["HIE"]["ND1"] = dE["N2m"]
    depsilon["HIE"]["CE1"] = dE["CA"]
    depsilon["HIE"]["NE2"] = dE["N2m"]
    depsilon["HIE"]["CD2"] = dE["CA"]
    depsilon["HIE"]["H"] = dE["H"]
    depsilon["HIE"]["HA"] = dE["H1"]
    depsilon["HIE"]["HB2"] = dE["HC"]
    depsilon["HIE"]["HB3"] = dE["HC"]
    depsilon["HIE"]["HE1"] = dE["H5"]
    depsilon["HIE"]["HE2"] = dE["H"]
    depsilon["HIE"]["HD2"] = dE["H4"]

    depsilon["HIS"] = {}
    depsilon["HIS"]["N"] = dE["N2m"]
    depsilon["HIS"]["CA"] = dE["CT"]
    depsilon["HIS"]["C"] = dE["C"]
    depsilon["HIS"]["O"] = dE["O"]
    depsilon["HIS"]["CB"] = dE["CT"]
    depsilon["HIS"]["CG"] = dE["CA"]
    depsilon["HIS"]["ND1"] = dE["N2m"]
    depsilon["HIS"]["CE1"] = dE["CA"]
    depsilon["HIS"]["NE2"] = dE["N2m"]
    depsilon["HIS"]["CD2"] = dE["CA"]
    depsilon["HIS"]["H"] = dE["H"]
    depsilon["HIS"]["HA"] = dE["H1"]
    depsilon["HIS"]["HB2"] = dE["HC"]
    depsilon["HIS"]["HB3"] = dE["HC"]
    depsilon["HIS"]["HE1"] = dE["H5"]
    depsilon["HIS"]["HD1"] = dE["H"]
    depsilon["HIS"]["HD2"] = dE["H4"]

    depsilon["MET"] = {}
    depsilon["MET"]["N"] = dE["N2m"]
    depsilon["MET"]["CA"] = dE["CT"]
    depsilon["MET"]["C"] = dE["C"]
    depsilon["MET"]["O"] = dE["O"]
    depsilon["MET"]["CB"] = dE["CT"]
    depsilon["MET"]["CG"] = dE["CT"]
    depsilon["MET"]["SD"] = dE["S"]
    depsilon["MET"]["CE"] = dE["CT"]
    depsilon["MET"]["H"] = dE["H"]
    depsilon["MET"]["HA"] = dE["H1"]
    depsilon["MET"]["HB2"] = dE["HC"]
    depsilon["MET"]["HB3"] = dE["HC"]
    depsilon["MET"]["HG2"] = dE["H1"]
    depsilon["MET"]["HG3"] = dE["H1"]
    depsilon["MET"]["HE2"] = dE["H1"]
    depsilon["MET"]["HE3"] = dE["H1"]
    depsilon["MET"]["HE1"] = dE["H1"]



    depsilon["PHE"] = {}
    depsilon["PHE"]["N"] = dE["N2m"]
    depsilon["PHE"]["CA"] = dE["CT"]
    depsilon["PHE"]["C"] = dE["C"]
    depsilon["PHE"]["O"] = dE["O"]
    depsilon["PHE"]["CB"] = dE["CT"]
    depsilon["PHE"]["CG"] = dE["CA"]
    depsilon["PHE"]["CD1"] = dE["CA"]
    depsilon["PHE"]["CD2"] = dE["CA"]
    depsilon["PHE"]["CE1"] = dE["CA"]
    depsilon["PHE"]["CE2"] = dE["CA"]
    depsilon["PHE"]["CZ"] = dE["CA"]
    depsilon["PHE"]["H"] = dE["H"]
    depsilon["PHE"]["HA"] = dE["H1"]
    depsilon["PHE"]["HB2"] = dE["HC"]
    depsilon["PHE"]["HB3"] = dE["HC"]
    depsilon["PHE"]["HD1"] = dE["HA"]
    depsilon["PHE"]["HD2"] = dE["HA"]
    depsilon["PHE"]["HE1"] = dE["HA"]
    depsilon["PHE"]["HE2"] = dE["HA"]
    depsilon["PHE"]["HZ"] = dE["HA"]
   

    

    depsilon["TYR"] = {}
    depsilon["TYR"]["N"] = dE["N2m"]
    depsilon["TYR"]["CA"] = dE["CT"]
    depsilon["TYR"]["C"] = dE["C"]
    depsilon["TYR"]["O"] = dE["O"]
    depsilon["TYR"]["CB"] = dE["CT"]
    depsilon["TYR"]["CG"] = dE["CA"]
    depsilon["TYR"]["CD1"] =  dE["CA"]
    depsilon["TYR"]["CD2"] =  dE["CA"]
    depsilon["TYR"]["CE1"] = dE["CA"]
    depsilon["TYR"]["CE2"] = dE["CA"]
    depsilon["TYR"]["CZ"] = dE["CA"]
    depsilon["TYR"]["OH"] = dE["OH"]
    depsilon["TYR"]["H"] = dE["H"]
    depsilon["TYR"]["HA"] = dE["H1"]
    depsilon["TYR"]["HB2"] = dE["HC"]
    depsilon["TYR"]["HB3"] = dE["HC"]
    depsilon["TYR"]["HD1"] = dE["HA"]
    depsilon["TYR"]["HD2"] = dE["HA"]
    depsilon["TYR"]["HE1"] = dE["HA"]
    depsilon["TYR"]["HE2"] = dE["HA"]
    depsilon["TYR"]["HH"] = dE["HO"]



    
    depsilon["TRP"] = {}
    depsilon["TRP"]["N"] = dE["N2m"]
    depsilon["TRP"]["CA"] = dE["CT"]
    depsilon["TRP"]["C"] = dE["C"]
    depsilon["TRP"]["O"] = dE["O"]
    depsilon["TRP"]["CB"] = dE["CT"]
    depsilon["TRP"]["CG"] = dE["CA"]
    depsilon["TRP"]["CD1"] = dE["CA"]
    depsilon["TRP"]["CD2"] = dE["CA"]
    depsilon["TRP"]["NE1"] = dE["N2m"]
    depsilon["TRP"]["CE2"] = dE["CA"]
    depsilon["TRP"]["CE3"] = dE["CA"]
    depsilon["TRP"]["CZ2"] = dE["CA"]
    depsilon["TRP"]["CZ3"] = dE["CA"]
    depsilon["TRP"]["CH2"] = dE["CA"]
    depsilon["TRP"]["H"] = dE["H"]
    depsilon["TRP"]["HA"] = dE["H1"]
    depsilon["TRP"]["HB2"] = dE["HC"]
    depsilon["TRP"]["HB3"] = dE["HC"]
    depsilon["TRP"]["HD1"] = dE["H4"]
    depsilon["TRP"]["HE1"] = dE["H"]
    depsilon["TRP"]["HE3"] = dE["HA"]
    depsilon["TRP"]["HZ2"] = dE["HA"]
    depsilon["TRP"]["HZ3"] = dE["HA"]
    depsilon["TRP"]["HH2"] = dE["HA"]

    return dvdw, depsilon



