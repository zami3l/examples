#!/usr/bin/python3
# coding : utf-8

from scapy.all import *
import sys

if len(sys.argv) != 7:
    print('Utilisation : py spoofing.py [IP SRC] [MAC SRC] [IP DEST] [MAC DEST] [PORT DEST] [FLAGS]')
else:
    result = Ether(src=sys.argv[2], dst=sys.argv[4])/IP(src=sys.argv[1], dst=sys.argv[3])/TCP(dport=sys.argv[5], flags=sys.argv[6])