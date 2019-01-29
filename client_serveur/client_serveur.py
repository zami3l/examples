#Importation
import sys
import socket
import hashlib
import os
import time

#Fonction : Vérification du checksum
def checksum():
    checksum = hashlib.sha1(open(sys.argv[0], 'rb').read()).hexdigest()
    return checksum

#Si client
if (sys.argv[1] == "client"):
    #Declaration
    ip = '0.0.0.0'
    port = 26001

    #Declaration du socket
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Demande de connection
    connexion.connect((ip, port))

    #Retour du serveur
    echange_serveur = connexion.recv(1024).decode()
    
    #Envoi du checksum au serveur pour vérification
    if (echange_serveur == "Connexion etablie"):
        print("\nUne connexion avec un serveur a été établi.\n")
        print("Envoi du checksum au serveur...\n")
        connexion.send(checksum().encode())

    #Retour du serveur pour le checksum
    echange_serveur = connexion.recv(1024).decode()

    if (echange_serveur == "Checksum correct"):
        print("Le checksum est correct. Fermeture de la connexion...\n")
    elif (echange_serveur == "Checksum incorrect"):
        print("Le checksum est incorrect. Fermeture de la connexion...\n")

    time.sleep(60)

    connexion.close()

#Si Serveur
elif (sys.argv[1] == "serveur"):
    #Declaration et Initialisation
    ip = ''
    port = 26001

    #Declaration du socket
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Lancement de l'ecoute
    connexion.bind((ip, port))
    connexion.listen(5)

    print("\nLe serveur est prêt.\n")

    #Autorisation d'une demande de connexion
    connexion_client, info_client = connexion.accept()

    print('Un client vient de se connecter.\n')

    #Validation
    connexion_client.send(b"Connexion etablie")

    #Vérification du checksum
    print("Vérification du checksum client :")

    #Reception du checksum client
    echange_client = connexion_client.recv(1024).decode()

    print("Checksum serveur : ", checksum())
    print("Checksum client : {} \n".format(echange_client))

    if (checksum() == echange_client):
        print("Le checksum du client est correct.\n")
        connexion_client.send(b"Checksum correct")

    else:
        print("Checksum incorrect. Fermeture de la connexion...\n")
        connexion_client.send(b"Checksum incorrect")

    time.sleep(60)

    #On ferme la connexion avec le client et l'ecoute
    connexion_client.close()
    connexion.close()

else:
    print("Erreur, veuillez choisir le mode client ou serveur.")