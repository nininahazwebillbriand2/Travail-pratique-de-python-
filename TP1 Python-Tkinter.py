import tkinter as tk
from tkinter import messagebox 

fenetre = tk.Tk() # créer la fenêtre principale
fenetre.title("Ma première application Tkinter") # Définir le titre de la fenêtre
fenetre.geometry("400x300") # Définir la taille de la fenêtre
fenetre.mainloop() # Lancer la boucle principale d'événements

import tkinter as tk

def action_bouton():
    print("Le bouton a été cliqué !")

fenetre = tk.Tk()
fenetre.title("Mon application avec widgets")
fenetre.geometry("400x300")

etiquette = tk.Label(fenetre, text = "Bonjour Tkinter !")
etiquette.pack(pady = 10)

bouton = tk.Button(fenetre, text = "Cliquez-moi")
bouton.pack(pady = 10)

fenetre.mainloop

import tkinter as tk

def afficher_texte():
    nom_saisi = champ_saisie.get()
    message_saisi = zone_texte.get("1.0", tk.END)
    print(f"Nom : {nom_saisi}")
    print(f"Message : {message_saisi}")
    messagebox.showinfo("Informations", f"Nom:{nom_saisi}\nMessage: {message_saisi}")

fenetre = tk.Tk()
fenetre.title("Saisie de texte")
fenetre.geometry("500x400")

label_nom = tk.Label(fenetre, text = "Entrez votre nom : ")
label_nom.pack(pady=5)
champ_saisie = tk.Entry(fenetre, width=40)
champ_saisie.pack()

label_message = tk.Label(fenetre, text = "Entrez votre message : ")
label_message.pack(pady=5)
zone_texte = tk.Text(fenetre, height=5, width=40)
zone_texte.pack()

bouton_afficher = tk.Button(fenetre, text = "Afficher", command=afficher_texte)
bouton_afficher.pack(pady=10)

fenetre.mainloop()
