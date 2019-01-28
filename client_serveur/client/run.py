#Importation
import socket

#Declaration
ip = '0.0.0.0'
port = 26001

#Declaration du socket
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Demande de connection
connexion.connect((ip, port))

#Retour du serveur
echange_serveur = connexion.recv(1024).decode()
print(echange_serveur)

#Saisi et Envoi du message au serveur
while echange_serveur != "OK":
    message = input('')
    message = message.encode()
    connexion.send(message)
    echange_serveur = connexion.recv(1024).decode()
    print(echange_serveur)

#On ferme la connexion
connexion.close()
