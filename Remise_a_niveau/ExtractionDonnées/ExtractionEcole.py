import sqlite3

# Connexion à la base de données
conn = sqlite3.connect(r'C:\Users\anthi\Dropbox\EFREI\M1\Remise_a_niveau\ecole.db')  # Assure-toi que le fichier ecole.db est au bon endroit
cursor = conn.cursor()

# Requête pour sélectionner tous les élèves
cursor.execute("SELECT * FROM eleves;")
eleves = cursor.fetchall()

# Requête pour sélectionner tous les enseignants
cursor.execute("SELECT * FROM enseignants;")
enseignants = cursor.fetchall()

# Affichage des résultats
print("Liste des eleves :")
for eleve in eleves:
    print(eleve)

print("\nListe des enseignants :")
for enseignant in enseignants:
    print(enseignant)

associations = []

# Parcours des élèves et enseignants pour associer par numero_classe
for eleve in eleves:
    for enseignant in enseignants:
        # Convertir les numéros de classe en entier avant la comparaison
        if int(eleve[7]) == int(enseignant[8]):  # Correction ici, eleve[7] et enseignant[8]
            associations.append((eleve[1], eleve[2], enseignant[1], enseignant[2])) # (prenom_eleve, nom_eleve, prenom_enseignant, nom_enseignant)

# Affichage des associations
print("\nAssociations élève - enseignant :")
for assoc in associations:
    print(f"L'élève {assoc[0]} {assoc[1]} est associé à l'enseignant {assoc[2]} {assoc[3]}")

compteur = {}
for eleve in eleves:
    for enseignant in enseignants:
        if int(eleve[7]) == int(enseignant[8]):  # Si le numero_classe de l'élève correspond à celui de l'enseignant
            if enseignant[1] not in compteur:  # Si l'enseignant n'est pas encore dans le dictionnaire
                compteur[enseignant[1]] = 1  # Initialiser le compteur pour cet enseignant
            else:
                compteur[enseignant[1]] += 1  # Incrémenter le compteur pour cet enseignant

# Affichage du nombre d'élèves pour chaque enseignant
print("\nNombre d'élèves par enseignant :")
for enseignant, nombre in compteur.items():
    print(f"L'enseignant {enseignant} a {nombre} élève(s).")

# Fermer la connexion
conn.close()