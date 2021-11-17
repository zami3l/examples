#!/bin/bash

set -x

if [ -z "$1" ]; then 
	echo "$0 <NAME ROOT CA>"
	exit 1
fi

NAME_ROOT_CA=$1
KEY_SIZE="4096"
CRT_SUBJ="/C=FR/O=LAN/OU=Root\ CA/CN=GlobalSign\ Root\ CA"

openssl genrsa -out ${NAME_ROOT_CA}.key ${KEY_SIZE}
openssl req -x509 -new -sha512 -nodes -key ${NAME_ROOT_CA}.key -days 36500 -out ${NAME_ROOT_CA}.crt -subj "${CRT_SUBJ}"
