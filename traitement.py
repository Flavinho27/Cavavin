import cgi
import sqlite3

# recuperation des donnees du formulaire
formulaire = cgi.FieldStorage()

NomVin = formulaire.getvalue("nNomVin")
NomAppellation = formulaire.getvalue("nNomAppellation")
ChoixCouleur = formulaire.getvalue("nChoixCouleur")
NbreBouteilles = formulaire.getvalue("nNbreBouteilles")


Appellation = formulaire.getvalue("nAppellation")
Region = formulaire.getvalue("nRegion")
Pays = formulaire.getvalue("nPays")
Mets1 = formulaire.getvalue("nMets1")
Mets2 = formulaire.getvalue("nMets2")
Mets3 = formulaire.getvalue("nMets3")
Mets4 = formulaire.getvalue("nMets4")
Mets5 = formulaire.getvalue("nMets5")

Update = formulaire.getvalue("nUpdate")
IdVin = formulaire.getvalue("nIdVin")
NbreUpdate = formulaire.getvalue("nNbreUpdate")

SupprAppell = formulaire.getvalue("nSupprAppell")

Mets = []
Mets.append(str(Mets1))
Mets.append(str(Mets2))
Mets.append(str(Mets3))
Mets.append(str(Mets4))
Mets.append(str(Mets5))

AllMets = ""

for met in Mets:
	if met == "None":
		pass
	else:
		AllMets = AllMets + str(met) + " "
# enlever les espace du debut et de la fin
AllMets = AllMets.strip()


DonneesVin = (NomVin, NomAppellation, ChoixCouleur, NbreBouteilles)
DonneesAppellation = (Appellation, Region, Pays, AllMets)
DonneesUpdate = (Update, IdVin, NbreUpdate)

insert_vin = True
insert_appellation = True
insert_update = True
insert_suppr_appell = True

# on regarde si tout le formulaire est bien rempli
for label in DonneesVin:
	if label != None:
		pass
	else:
		insert_vin = False
		break

# on regarde si tout le formulaire est bien rempli
for label in DonneesAppellation:
	if label != None:
		pass
	else:
		insert_appellation = False
		break

# on regarde si tout le formulaire est bien rempli
for label in DonneesUpdate:
	if label != None:
		pass
	else:
		insert_update = False
		break

#on regarde si tout le formulaire est bien rempli
if SupprAppell != None:
	pass
else:
	insert_suppr_appell = False

connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()

# selection de tous les attributs de la table illustrateur
curseur.execute("""CREATE TABLE IF NOT EXISTS VINS(
	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, appellation TEXT, couleur TEXT, bouteilles TEXT)""")

curseur.execute("""CREATE TABLE IF NOT EXISTS APPELLATIONS(
	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, appellation TEXT, region TEXT, pays TEXT, mets TEXT)""")


if insert_vin:
	liste_DonneesVin = list(DonneesVin)

	for i in range(len(liste_DonneesVin)):
		# enlever les espaces en trop (du debut et de la fin)
		liste_DonneesVin[i] = liste_DonneesVin[i].strip()

	DonneesVin = tuple(liste_DonneesVin)

	# insertion des données du formulaire dans la base
	requete = "INSERT INTO VINS(nom, appellation, couleur, bouteilles) VALUES(?, ?, ?, ?)"

	curseur.execute(requete, DonneesVin)

	# commit pour enregistrer la commande
	connexion.commit()

if insert_appellation:
	liste_DonneesAppellation = list(DonneesAppellation)

	for i in range(len(liste_DonneesAppellation)):
		# enlever les espaces en trop (du debut et de la fin)
		liste_DonneesAppellation[i] = liste_DonneesAppellation[i].strip()

	DonneesAppellation = tuple(liste_DonneesAppellation)

	# insertion des données du formulaire dans la base
	requete = "INSERT INTO APPELLATIONS(appellation, region, pays, mets) VALUES(?, ?, ?, ?)"

	curseur.execute(requete, DonneesAppellation)

	# commit pour enregistrer la commande
	connexion.commit()

if insert_update:
	
	
	requete_ajout = """UPDATE VINS
		SET bouteilles = (SELECT bouteilles FROM VINS WHERE id = """+ str(IdVin) +""")+""" + str(NbreUpdate) + """ WHERE id = """ + str(IdVin)

	requete_suppr = """UPDATE VINS
		SET bouteilles = (SELECT bouteilles FROM VINS WHERE id = """+ str(IdVin) +""")-""" + str(NbreUpdate) + """ WHERE id = """ + str(IdVin)
	# insertion des données du formulaire dans la base

	if Update == 'ajout':
		curseur.execute(requete_ajout)
	elif Update == 'suppr':
		curseur.execute(requete_suppr)

	requete_bout = """DELETE FROM VINS WHERE bouteilles <= 0"""
	curseur.execute(requete_bout)

	# commit pour enregistrer la commande
	connexion.commit()

if insert_suppr_appell:
	# insertion des données du formulaire dans la base

	requete = "DELETE FROM APPELLATIONS WHERE appellation = '" + str(SupprAppell) + "'"

	curseur.execute(requete)

	# commit pour enregistrer la commande
	connexion.commit()


curseur.close()
connexion.close()

from formulaires import *
