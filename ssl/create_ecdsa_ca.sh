#!/bin/bash

set -x

if [ -z "$1" ]; then 
	echo "$0 <NAME ROOT CA>"
	exit 1
fi

NAME_ROOT_CA=$1
KEY_TYPE="secp521r1"
CRT_SUBJ="/C=FR/O=LAN/OU=Root\ CA/CN=GlobalSign\ Root\ CA"

openssl ecparam -genkey -name ${KEY_TYPE} -out ${NAME_ROOT_CA}.key
openssl req -x509 -new -sha512 -nodes -key ${NAME_ROOT_CA}.key -days 36500 -out ${NAME_ROOT_CA}.crt -subj "${CRT_SUBJ}"
