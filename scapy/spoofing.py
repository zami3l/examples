#!/usr/bin/python3
# coding : utf-8

from scapy.all import *
from pathlib import Path
import sys, toml, os.path

#Emplacement du fichier de configuration
pathConfig = Path('./conf.toml')

#Arguments
if len(sys.argv) == 7:

    query =     Ether(src=sys.argv[2], dst=sys.argv[4])/ \
                IP(src=sys.argv[1], dst=sys.argv[3])/ \
                TCP(dport=sys.argv[5], flags=sys.argv[6])

#Fichier de configuration
elif os.path.exists(pathConfig):

    config = toml.load(pathConfig) 

    query =     Ether(src=config['SRC']['mac'], dst=config['DST']['mac'])/ \
                IP(src=config['SRC']['ip'], dst=config['DST']['ip'])/ \
                TCP(dport=config['DST']['port'], flags=config['GEN']['flags'])

#Instruction
else:

    print('Utilisation : py spoofing.py [IP SRC] [MAC SRC] [IP DEST] [MAC DEST] [PORT DEST] [FLAGS]')
    sys.exit()

print('Requête générée : \n')
query.show()

#Envoi de la requête
sendp(query)