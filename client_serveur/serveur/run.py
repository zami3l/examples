#Importation
import socket

#Declaration et Initialisation
ip = 'localhost'
port = 26001
message_recu = bytes
nb_tentative = 0

#Declaration du socket
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Lancement de l'ecoute
connexion.bind((ip, port))
connexion.listen(5)

#Autorisation d'une demande de connexion
echange_client, info_client = connexion.accept()

print('Un client vient de se connecter.')

#Demande au client de saisir le mot de passe
echange_client.send(b"Veuillez saisir le mot de passe : ")

#Verification du mot de passe saisie
while message_recu != "123456789":
    if (nb_tentative >= 1):
        print("Le client a saisi un mot de passe incorrect. Nombre de tentative : ", nb_tentative)
        echange_client.send(b"Le mot de passe saisi est incorrect, ressayez :")

    #Reception du mot de passe envoyé par le client
    message_recu = echange_client.recv(1024).decode()
    print("Le client vient d'envoyer le mot de passe suivant : ", message_recu)
    nb_tentative += 1

#Le mot de passe saisie est correct
echange_client.send(b"OK")
print('Le client a saisi le bon mot de passe.')
print('Fermeture de la connexion')

#On ferme la connexion avec le client et l'ecoute
echange_client.close()
connexion.close()