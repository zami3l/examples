#!/usr/bin/python3
# coding : utf-8

import sys, socket, time, string

#Constante IRC
SERVER = "<Server>"
PORT = "<Port>"
CHANNEL = "<#Channel>"

NICK = "<Pseudo>"
IDENT = "<Pseudo>"
REALNAME = "<Pseudo>"

def init():
    global IRC

    #Declaration du socket
    IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    IRC.connect((SERVER, PORT))

    #Attente synchro
    time.sleep(1)

    #Envoi des informations
    IRC.send(bytes("NICK %s\r\n" % NICK, 'UTF-8'))
    IRC.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, SERVER, REALNAME), 'UTF-8'))

def cut(line):
    return str.split(str.rstrip(line))

#Fonction pour envoyer un message privée
def msgPrive(cible, message):
    IRC.send(bytes('PRIVMSG ' + cible + ' ' + message + '\r\n', 'UTF-8'))

#Fonction pour changer de channel
def changeChannel(channel):
    IRC.send(bytes('JOIN %s\r\n' % channel, 'UTF-8'))

if __name__ == '__main__':

    #Initialisation
    init()

    #Buffer de réception
    readBuffer = ''

    while 1:
        readBuffer = readBuffer + IRC.recv(1024).decode('UTF-8')
        temp = str.split(readBuffer, '\n')
        readBuffer = temp.pop()

        for line in temp:
            line = cut(line)

            #Timeout
            if(line[0] == "PING"):
                IRC.send(bytes("PONG %s\r\n" % line[1], 'UTF-8'))
