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
	<link rel="stylesheet" type="text/css" href="css/index.css">
	<link rel="shortcut icon" href="img/vin.ico">
</head>
<body>
	<main>
		<div id="accueil">
			<img id="logo" src="img/logo.jpg" alt="logo">
			<h1>Gestion de ma Cave</h1>
			<footer><p class="footer">Copyright &copy; - Flavien</p></footer>
		</div>

		<div id="menu">
			<section id="all_buttons">
				<div id="first" class="divButton">
					<a href="formulaires.py">Formulaires de mise à jour</a>
				</div>
				<div id="second" class="divButton">
					<a href="consultation.py">Consulter ma cave</a>
				</div>
				<div id="third" class="divButton">
					<a href="particulier.py">Consultation spécifique</a>
				</div>
			</section>
		</div>
	</main>
</body>
</html>"""

print(html)

# on se deconnecte de la base
curseur.close()
connexion.close()
