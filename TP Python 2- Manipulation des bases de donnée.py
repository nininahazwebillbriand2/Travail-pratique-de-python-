import sqlite3

conn = sqlite3.connect('ma_base_de_donnees.db')
cursor = conn.cursor()
print("Connexion à la base de données avec succès.")

cursor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL, email TEXT UNIQUE NOT NULL)''')
conn.commit()
print("Table 'utilisateurs' créée avec succès.")

donnees_utilisateur = ('Jean Claude Kabayabaya', 'jc.kabayabaya@gmail.com')
cursor.execute("INSERT INTO utilisateurs (nom, email) VALUES(?, ?)", donnees_utilisateur)
conn.commit()
print("Utilisateur inséré avec succès.")
utilisateurs = [
    ('Marie Ciza', 'marie.ciza@gmail.com'),
    ('Albert Mukunzi', 'albert.mukunzi@gamil.com')
]

cursor.executemany("INSERT INTO utilisateurs (nom, email) VALUES (?, ?)", utilisateurs)
conn.commit()
print("Deux utilisateurs insérés avec succès.")

cursor.execute("SELECT id, nom, email FROM utilisateurs")
resultats = cursor.fetchall()

print("Liste de tous les utilisateurs : ")
for utilisateurs in resultats :
    print(utilisateurs)

nom_recherche = 'Jean Claude Kabayabaya'
cursor.execute("SELECT email FROM utilisateurs WHERE nom = ?", (nom_recherche,))
email_trouve = cursor.fetchone()

print(f"L'e-mail de {nom_recherche} est : {email_trouve[0]}")

nouveau_mail = 'j.claude@yahoo.fr'
nom_a_modifier = 'Jean Claude Kabayabaya'
cursor.execute("UPDATE utilisateurs SET email = ? WHERE nom = ?", (nouveau_mail, nom_a_modifier))
conn.commit()

print(f"E-mail de {nom_a_modifier} mis à jour.")

nom_a_supprimer = 'Marie Ciza'
cursor.execute("DELETE FROM utilisateurs WHERE nom=?", (nom_a_supprimer,))
conn.commit()

print(f"Utilisateur {nom_a_supprimer} supprimé.")

conn.close()

print("Connexion à la base de données fermée.")