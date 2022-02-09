import sqlite3

# connexion à la base
connexion = sqlite3.connect("base_vins.db")
curseur = connexion.cursor()
# selection de tous les attributs de la table illustrateur
curseur.execute("""CREATE TABLE IF NOT EXISTS VINS(
	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, appellation TEXT, couleur TEXT, bouteilles TEXT)""")

curseur.execute("""CREATE TABLE IF NOT EXISTS APPELLATIONS(
	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, appellation TEXT, region TEXT, pays TEXT, mets TEXT)""")

# indiquer au navigateur que l'on code en HTML
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<html>
<head>
	<title>Ma Cave</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/consultation.css">
	<link rel="shortcut icon" href="img/vin.ico">
</head>
<body>
	<div id="background">
		<img src="img/background.jpg" alt="background">
	</div>
	<main>
		<a href="index.py"><img id="back_button" src="img/back.png" alt="Bouton retour"></a>"""

print(html)

print(f"		<div class='divBouTotal'>")

totalCouleur = [[], ["Bouteilles Total", "Rouge", "Blanc", "Rose"], {"Bouteilles Total": "id='total'", "Rouge": "id='rouge'", "Blanc": "id='blanc'", "Rose": "id='rose'"}]

curseur.execute("""SELECT SUM(bouteilles) FROM VINS""")

for tuple in curseur:
	liste = list(tuple)
	for champ in liste:
		totalCouleur[0].append(champ)

curseur.execute("""SELECT SUM(bouteilles) FROM VINS WHERE couleur = 'rouge'""")

for tuple in curseur:
	liste = list(tuple)
	for champ in liste:
		totalCouleur[0].append(champ)

curseur.execute("""SELECT SUM(bouteilles) FROM VINS WHERE couleur = 'blanc'""")

for tuple in curseur:
	liste = list(tuple)
	for champ in liste:
		totalCouleur[0].append(champ)

curseur.execute("""SELECT SUM(bouteilles) FROM VINS WHERE couleur = 'rose'""")

for tuple in curseur:
	liste = list(tuple)
	for champ in liste:
		totalCouleur[0].append(champ)


# boucle pour l'affichage du nombre de bouteilles
for i in range(4):
	if totalCouleur[0][i] != None:
		# id couleur pour l'identifiant en /*css*/
		id_couleur = totalCouleur[1][i]
		print(f"			<p " + str(totalCouleur[2][id_couleur]) + ">" + str(totalCouleur[1][i]) + " : <span class='nbreBouteilles'>" + str(totalCouleur[0][i]) + "</span></p>")
	else:
		id_couleur = totalCouleur[1][i]
		print(f"			<p " + str(totalCouleur[2][id_couleur]) + ">" + str(totalCouleur[1][i]) + " : <span class='nbreBouteilles'>" + str(0) + "</span></p>")

print(f"		</div>")

html = """
		<section id="ma_cave">

			<!--Tableau des vins-->
			<table border="4" id="t_vins">
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
				</thead>"""

print(html)

curseur.execute("""SELECT * FROM VINS""")

print(f"				<tbody>")
# creation du tableau
for tuple in curseur:
	c = 0
	print(f"					<tr>")
	liste = list(tuple)
	for champ in liste:
		c += 1
		# si le champ concerne le nombre de bouteilles
		if c == 5:
			if "-" in str(champ):
				print(f"						<td>" + str(0) + "</td>")
			else:
				print(f"						<td>" + str(champ) + "</td>")
		else:
			print(f"						<td>" + str(champ) + "</td>")
	print(f"					</tr>")
print(f"				</tbody>")
print(f"			</table>")
#fin du tableau

html = """
			<!--Tableau des appellations-->
			<table border="4" id="t_appellations">
				<colgroup>
					<col class="tous" span="4">
				</colgroup>
				<thead>
					<tr>
						<th class="titre" colspan="5">APPELLATIONS</th>
					</tr>
					<tr>
						<th id="identifiant">Identifiant</th>
						<th id="nom_appellation">Appellation</th>
						<th id="region">Région</th>
						<th id="pays">Pays</th>
						<th id="mets">Mets (5 max)</th>
					</tr>
				</thead>"""

print(html)

curseur.execute("""SELECT * FROM APPELLATIONS""")

print(f"				<tbody>")
# creation du tableau
for tuple in curseur:
	print(f"					<tr>")
	liste = list(tuple)
	for champ in liste:
		print(f"						<td>" + str(champ) + "</td>")
	print(f"					</tr>")
print(f"				</tbody>")
print(f"			</table>")
#fin du tableau

html = """
		</section>
	</main>
</body>
</html>"""

print(html)

# on se deconnecte de la base
curseur.close()
connexion.close()
