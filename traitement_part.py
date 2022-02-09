import cgi
import sqlite3

# connexion à la base
connexion = sqlite3.connect("base_vins.db")
curseur = connexion.cursor()

# recuperation des donnees du formulaire
formulaire = cgi.FieldStorage()

InfoVin = formulaire.getvalue("nInfoVin")
InfoRegion = formulaire.getvalue("nInfoRegion")
VinMets = formulaire.getvalue("nVinMets")

insert_info_vin = True
insert_info_region = True
insert_vin_mets = True

# on regarde si tout le formulaire est bien rempli
if InfoVin != None:
	pass
else:
	insert_info_vin = False

if InfoRegion != None:
	pass
else:
	insert_info_region = False

if VinMets != None:
	pass
else:
	insert_vin_mets = False


print("Content-type: text/html; charset=utf-8\n")

if insert_info_vin:

	html = """<!DOCTYPE html>
<html>
<head>
	<title>Ma Cave</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/traitement_part.css">
	<link rel="shortcut icon" href="img/vin.ico">
</head>
<body>
	<div id="background">
		<img src="img/background.jpg" alt="background">
	</div>
	<main>
		<a href="particulier.py"><img id="back_button" src="img/back.png" alt="Bouton retour"></a>

		<table border="4">
			<thead>
				<tr>
					<th class="titre" colspan="5">VINS</th>
				</tr>
				<tr>
					<th id="identifiant">Identifiant</th>
					<th id="nom_vin">Nom</th>
					<th id="appellation">Appellation</th>
					<th id="couleur">Couleur</th>
					<th id="bouteilles">Bouteilles</th>
				</tr>
			</thead>
			<tbody>"""

	print(html)

	requete = "SELECT * FROM VINS WHERE nom = '" + str(InfoVin) + "'"

	curseur.execute(requete)

	for tuple in curseur:
		c = 0
		print(f"				<tr>")
		liste = list(tuple)
		for champ in liste:
			c += 1
			if str(champ) == str(InfoVin) or c == 3:
				print(f"					<td class='tdSpecial'>" + str(champ) + "</td>")
			else:
				print(f"					<td>" + str(champ) + "</td>")
		print(f"				</tr>")
	print(f"			</tbody>")
	print(f"		</table>")

	html = """
		<table border="4">
			<thead>
				<tr>
					<th class="titre" colspan="5">APPELLATIONS</th>
				</tr>
				<tr>
					<th id="identifiant">Identifiant</th>
					<th id="nom_appellation">Appellation</th>
					<th id="Region">Region</th>
					<th id="Pays">Pays</th>
					<th id="Mets">Mets (5 max)</th>
				</tr>
			</thead>
			<tbody>"""

	print(html)

	select_appell = "(SELECT appellation FROM VINS WHERE nom = '" + str(InfoVin) + "')"
	requete = "SELECT * FROM APPELLATIONS WHERE appellation = " + select_appell

	curseur.execute(requete)

	for tuple in curseur:
		c = 0
		print(f"				<tr>")
		liste = list(tuple)
		for champ in liste:
			c += 1
			if c == 2 or c == 3:
				print(f"					<td class='tdSpecial'>" + str(champ) + "</td>")
			else:
				print(f"					<td>" + str(champ) + "</td>")
		print(f"				</tr>")
	print(f"			</tbody>")
	print(f"		</table>")


	html = """
	</main>
</body>
</html>"""

	print(html)

elif insert_info_region:
	html = """<!DOCTYPE html>
<html>
<head>
	<title>Ma Cave</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/traitement_part.css">
	<link rel="shortcut icon" href="img/vin.ico">
</head>
<body>
	<div id="background">
		<img src="img/background.jpg" alt="background">
	</div>
	<main>
		<a href="particulier.py"><img id="back_button" src="img/back.png" alt="Bouton retour"></a>

		<table border="4">
			<thead>
				<tr>
					<th class="titre" colspan="5">VINS</th>
				</tr>
				<tr>
					<th id="identifiant">Identifiant</th>
					<th id="nom_vin">Nom</th>
					<th id="appellation">Appellation</th>
					<th id="couleur">Couleur</th>
					<th id="bouteilles">Bouteilles</th>
				</tr>
			</thead>
			<tbody>"""

	print(html)

	requete = """SELECT DISTINCT VINS.id, VINS.nom, VINS.appellation, VINS.couleur, VINS.bouteilles
		FROM VINS
		JOIN APPELLATIONS ON APPELLATIONS.appellation = VINS.appellation
		WHERE region = '""" + str(InfoRegion) + "'"

	curseur.execute(requete)

	for tuple in curseur:
		c = 0
		print(f"				<tr>")
		liste = list(tuple)
		for champ in liste:
			c += 1
			if c == 2 or c == 3:
				print(f"					<td class='tdSpecial'>" + str(champ) + "</td>")
			else:
				print(f"					<td>" + str(champ) + "</td>")
		print(f"				</tr>")

	html = """			</tbody>
		</table>

		<table border="4">
			<thead>
				<tr>
					<th class="titre" colspan="5">APPELLATIONS</th>
				</tr>
				<tr>
					<th id="identifiant">Identifiant</th>
					<th id="nom_appellation">Appellation</th>
					<th id="region">Région</th>
					<th id="pays">Pays</th>
					<th id="mets">Mets (5max)</th>
				</tr>
			</thead>
			<tbody>"""

	print(html)

	requete = "SELECT * FROM APPELLATIONS WHERE region = '" + str(InfoRegion) + "'"

	curseur.execute(requete)

	for tuple in curseur:
		c = 0
		print(f"				<tr>")
		liste = list(tuple)
		for champ in liste:
			c += 1
			if str(champ) == str(InfoRegion) or c == 2:
				print(f"					<td class='tdSpecial'>" + str(champ) + "</td>")
			else:
				print(f"					<td>" + str(champ) + "</td>")
		print(f"				</tr>")

	html = """			</tbody>
		</table>
	</main>
</body>
</html>"""

	print(html)

elif insert_vin_mets:
	html = """<!DOCTYPE html>
<html>
<head>
	<title>Ma Cave</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/traitement_part.css">
	<link rel="shortcut icon" href="img/vin.ico">
</head>
<body>
	<div id="background">
		<img src="img/background.jpg" alt="background">
	</div>
	<main>
		<a href="particulier.py"><img id="back_button" src="img/back.png" alt="Bouton retour"></a>"""

	print(html)

	requete = """SELECT DISTINCT VINS.nom
		FROM VINS
		JOIN APPELLATIONS ON VINS.appellation = APPELLATIONS.appellation
		WHERE mets LIKE '%""" + str(VinMets) + "%'"

	curseur.execute(requete)

	print(f"		<h1>Liste de Vins pour accompagner: <span class='liste'>" + str(VinMets) + "</span></h1>")

	# debut de la liste des vins pour les mets donnes
	print(f"		<ul>")

	c = 0
	for tuple in curseur:
		liste = list(tuple)
		for champ in liste:
			c += 1
			print(f"			<li><span class='label'>Vin</span> : " + str(champ) + "</li>")
	if c == 0:
		print(f"			<li>Désolé ! Il n'y a pas de Vin dans la base correspondant au Met donnés</li>")
	print(f"		</ul>")

	html = """
	</main>
</body>
</html>"""

	print(html)


else:
	html = """<!DOCTYPE html>
<html>
<head>
	<title>Formulaires</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/traitement_part.css">
	<link rel="shortcut icon" href="img/vin.ico">
</head>
<body>
	<div id="background">
		<img src="img/background.jpg" alt="background">
	</div>
	<main>
		<a href="index.py"><img id="back_button" src="img/back.png" alt="Bouton retour"></a>

		<h1 id="erreur">Vous avez mal rempli le formulaire<br>
		Recommencez</h1>
	</main>
</body>
</html>"""

	print(html)

curseur.close()
connexion.close()
