#!/usr/bin/env python
# coding: utf-8

import os, sys, fnmatch

def existPackage(namePackage):

        if os.system("pacman -Qs {} > /dev/null".format(namePackage)) != 0:

            print("\nLe paquet [libheif] n'est pas présent sur votre système.")
            print("L'utilisation de la commande : < sudo pacman -S {} > permet de corriger le problème.\n".format(namePackage))

            sys.exit()

def createFolder(folderReception):

    if os.path.isdir(folderReception):

        os.rename(folderReception, folderReception + "_old")
        os.mkdir(folderReception)

    else:

        os.mkdir(folderReception)

def heicToJpg(pathFolder, pathFolderReception):

    print("\nCréation du dossier de réception [{}] terminée.\n".format(pathFolderReception))
    createFolder(pathFolderReception)

    print("Début de conversion HEIC vers JPG :\n")

    for files in os.listdir(pathFolder):

        if fnmatch.fnmatch(files, '*.HEIC'):

            print("Conversion du fichier [{}] -> [{}.JPG]".format(files, files[-8:-5]))
            os.system("heif-convert -q 100 \"{}/{}\" \"{}/{}.jpg\"".format(pathFolder, files, pathFolderReception, files[-8:-5]))
    
    print("\nConversion terminée.\n")

if __name__ == "__main__":

    #Vérification de l'existence du paquet sur le système
    existPackage("libheif")

    if len(sys.argv) == 3:

        #Lancement de la conversion HEIC -> JPG
        heicToJpg(sys.argv[1], sys.argv[2])       

    else:

        print('Utilisation : py convert.py [Path du dossier HEIC] [Path dossier de sortie]')
        sys.exit()
