#!/usr/bin/env python
# coding: utf-8

import os, sys, fnmatch

def existPackage(namePackage):

        if os.system("pacman -Qs {} > /dev/null".format(namePackage)) != 0:

            print("\nLe paquet [libheif] n'est pas présent sur votre système.")
            print("L'utilisation de la commande : < sudo pacman -S {} > permet de corriger le problème.\n".format(namePackage))

            sys.exit()

def createFolder(path, nameFolder):
    
    folderReception = "{}/{}".format(path, nameFolder)

    if os.path.isdir(folderReception):

        os.rmdir(folderReception)
        os.mkdir(folderReception)

    else:

        os.mkdir(folderReception)

def heicToJpg(pathFolder, nameFolderReception):

    print("\nCréation du dossier de réception [{}] terminée.\n".format(nameFolderReception))
    createFolder(pathFolder, nameFolderReception)

    print("Début de conversion HEIC vers JPG :\n")
    for files in os.listdir(pathFolder):

        if fnmatch.fnmatch(files, '*.heic'):

            cmd = "heif-convert -q 100 {} {}.jpg".format(files, files[-7:])
            os.system(cmd)
    
    print("\nConversion terminée.\n")

if __name__ == "__main__":

    #Vérification de l'existence du paquet sur le système
    existPackage("libheif")

    if len(sys.argv) == 3:

        #Lancement de la conversion HEIC -> JPG
        heicToJpg(sys.argv[1], "result")       

    else:

        print('Utilisation : py convert.py [EMPLACEMENT DU DOSSIER] [NOM DU DOSSIER DE RECEPTION]')
        sys.exit()
