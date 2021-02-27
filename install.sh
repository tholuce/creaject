#!/bin/bash

chmod +x create-web-app

mkdir -p /usr/src/createwebapp/
cp ./create-web-app /usr/src/createwebapp/
cp -r ./createwebcomp/ /usr/src/createwebapp/
ln -s /usr/src/createwebapp/create-web-app /usr/bin/create-web-app