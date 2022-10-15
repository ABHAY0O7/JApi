#!/bin/bash

echo start

echo please install python3, python3-pip, python3-django if not present

name=$1
base=$2 

echo $name $base

python3 -m venv env

echo Created virtual enviornment

. env/bin/activate

echo Activated virtual enviornment

pip3 install django

echo Installed django successfully

pip3 install djangorestframework

echo Installed djangorestframework successfully

django-admin startproject $name

echo Started project $name

mv env/ $name/

echo Moved virtual enviornment to $name folder

cd $name/

echo Changed directory to $name folder

python3 manage.py startapp $base

echo Started new App $base

echo "urlpatterns=[]" > $base/urls.py

python3 manage.py makemigrations

echo Converted python models to SQL classes

python3 manage.py migrate

echo Created database Successfully

echo DONE!
