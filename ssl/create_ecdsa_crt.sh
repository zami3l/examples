#!/bin/bash

# Mode DEBUG
#set -x

if [ -z "$1" ] || [ -z "$2" ]; then 
	echo "$0 <DOMAIN> <CERT CA>"
	exit 1
fi

NAME_DOMAIN=$1
NAME_ROOT_CA=$2
NAME_CRT=${NAME_DOMAIN//./-}
KEY_TYPE="secp521r1"
CRT_SUBJ="/C=FR/O=LAN/CN=${NAME_DOMAIN}"

echo -e "Creation private key"
openssl ecparam -genkey -name ${KEY_TYPE} -out ${NAME_CRT}.key

echo -e "Creation CSR"
openssl req -new -sha512 -key ${NAME_CRT}.key -nodes -out ${NAME_CRT}.csr -subj "${CRT_SUBJ}"

echo -e "Creation et signature du CRT"
openssl x509 -req -sha256 -days 36500 -in ${NAME_CRT}.csr -CA ${NAME_ROOT_CA}.crt -CAkey ${NAME_ROOT_CA}.key -CAcreateserial -out ${NAME_CRT}.crt

echo -e "Verification du certificat ${NAME_CRT}.crt avec l'autorite de certification"
openssl verify -CAfile ${NAME_ROOT_CA}.crt ${NAME_CRT}.crt
