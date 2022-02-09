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
	<link rel="stylesheet" type="text/css" href="css/particulier.css">
	<link rel="shortcut icon" href="img/vin.ico">
</head>
<body>
	<div id="background">
		<img src="img/background.jpg" alt="background">
	</div>
	<main>
		<a href="index.py"><img id="back_button" src="img/back.png" alt="Bouton retour"></a>

		<section id="particulier">

			<form method="post" action="/traitement_part.py" id="form_vin">
				<fieldset form="form_vin">
					<legend>Informations Vins</legend>
					<label for="nom_vin">Nom du Vin</label> : <input list="choix_vin" name="nInfoVin" id="nom_vin" placeholder="Nom du vin" required="">
					<datalist id="choix_vin">"""

print(html)

curseur.execute("""SELECT DISTINCT nom FROM VINS""")

for tuple in curseur:
	liste = list(tuple)
	for champ in liste:
		print(f"						<option value='" + str(champ) + "'>" + str(champ) + "</option>")
print(f"					</datalist>")


html = """					<br>
					<button type="submit">Voir Informations</button>
				</fieldset>
			</form>

			<form method="post" action="/traitement_part.py" id="form_region">
				<fieldset form="form_region">
					<legend>Vins et Appellations par Région</legend>
					<label for="nom_region">Région</label> : <input list="choix_region" name="nInfoRegion" id="nom_region" placeholder="Nom du vin" required="">
					<datalist id="choix_region">"""

print(html)

curseur.execute("""SELECT DISTINCT region FROM APPELLATIONS""")

for tuple in curseur:
	liste = list(tuple)
	for champ in liste:
		print(f"						<option value='" + str(champ) + "'>" + str(champ) + "</option>")
print(f"					</datalist>")

html = """					<br>
					<button type="submit">Voir Informations</button>
				</fieldset>
			</form>

			<form method="post" action="/traitement_part.py" id="form_region">
				<fieldset form="form_region">
					<legend>Vin(s) pour met donné</legend>
					<label for="met">Met</label> : <input list="choix_met" name="nVinMets" id="met" placeholder="Met" required="">
					<datalist id="choix_met">"""
print(html)

curseur.execute("""SELECT DISTINCT mets FROM APPELLATIONS""")

for tuple in curseur:
	liste = list(tuple)
	for champ in liste:
		print(f"						<option value='" + str(champ) + "'>" + str(champ) + "</option>")
print(f"					</datalist>")

html = """					<br>
					<button type="submit">Voir Informations</button>
				</fieldset>
			</form>

		</section>
	</main>
</body>
</html>"""

print(html)

# on se deconnecte de la base
curseur.close()
connexion.close()
