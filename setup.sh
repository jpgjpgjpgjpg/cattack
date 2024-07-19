#!/bin/bash

#Instalação do TOR/Requirements

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update
    sudo apt-get install -y tor
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install tor
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Por favor, instale o Tor manualmente no Windows."
else
    echo "Sistema operacional não suportado para instalação automática do Tor."
    exit 1
fi

pip install -r requirements.txt
