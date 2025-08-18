import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Envoyer un e-mail avec Gmail")
window.geometry("500x400")
sender_label = tk.Label(window, text="Votre adresse e-mail Gmail :")
sender_label.pack(pady=5)
sender_entry = tk.Entry(window, width=50)
sender_entry.pack()

recipient_label = tk.Label(window, text="Adresse e-mail du destinataire : ")
recipient_label.pack(pady=5)
recipient_entry = tk.Entry(window, width=50)
recipient_entry.pack()

subject_label = tk.Label(window, text="Sujet : ")
subject_label.pack(pady=5)
subject_entry = tk.Entry(window, width=50)
subject_entry.pack()

message_label = tk.Label(window, text="Message : ")
message_label.pack(pady=5)
message_text = tk.Text(window, height=8, width=50)
message_text.pack()

# Bouton d'envoi

send_button = tk.Button(window, text="Envoyer", command=lambda: print("Bouton cliqué !"))
send_button.pack(pady=10)

window.mainloop()

import sqlite3

def setup_database():
    conn = sqlite3.connect('emails_envoyes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS emails (id INTEGER PRIMARY KEY AUTOINCREMENT, expediteur TEXT NOT NULL, destinataire TEXT NOT NULL, sujet TEXT NOT NULL, corps_message TEXT NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_email_to_db(sender, recipient, subject, body):
    conn = sqlite3.connect('emails_envoyes.db') 
    cursor = conn.cursor() 
    cursor.execute('''INSERT INTO emails (expediteur, destinataire, sujet, corps_message) VALUES (?, ?, ?, ?)''', (sender, recipient, subject, body))
    conn.commit()
    conn.close()

setup_database()

import smtplib
from email.mime.text import MIMEText

def send_email(): 
    """Gère l'envoi de l'e-mail et la sauvegarde.""" 
    sender_email = sender_entry.get() 
    recipient_email = recipient_entry.get() 
    subject = subject_entry.get() 
    email_body = message_text.get("1.0", tk.END).strip()
    sender_password = 'VOTRE_MOT_DE_PASSE_D_APPLICATION' 
 
    if not all([sender_email, recipient_email, subject, email_body, sender_password]): 
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.") 
        return 
 
    smtp_server = "smtp.gmail.com" 
    smtp_port = 587 
 
    try: 
        server = smtplib.SMTP(smtp_server, smtp_port) 
        server.starttls() 
        server.login(sender_email, sender_password)
        msg = MIMEText(email_body)
        msg['Subject'] = subject 
        msg['From'] = sender_email 
        msg['To'] = recipient_email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        save_email_to_db(sender_email, recipient_email, subject, email_body)
        messagebox.showinfo("Succès", "L'e-mail a été envoyé et sauvegardé !")

    except Exception as e: 
        messagebox.showerror("Erreur", f"Une erreur est survenue: {e}")
        
    finally: 
        if 'server' in locals(): 
            server.quit()

send_button.config(command=send_email)