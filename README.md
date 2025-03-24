## GENERIC-ML
 
### SKELETON CODE FOR AZURE DEPLOYMENT - TESTED ON STUDENT DATA

## Run from terminal:

docker build -t testdockerdrew.azurecr.io/gen-ml:lastest

docker login testdockerdrew.azurecr.io

docker push testdockerdrew.azurecr.io/gen-ml:lastest
