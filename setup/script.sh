#!/bin/zsh

REPO_URL="<URL_DEL_REPOSITORIO>"
PROJECT_DIR="<nombre_del_directorio_del_proyecto>"

echo "Clonando el repositorio..."
git clone $REPO_URL

echo "Entrando en el directorio del proyecto..."
cd $PROJECT_DIR

echo "Creando entorno virtual..."
python3 -m venv venv

echo "Activando entorno virtual..."
source venv/bin/activate .

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Aplicando migraciones..."
python manage.py migrate

echo "Ejecutando el servidor..."
python manage.py runserver

# Mantener el entorno virtual activo
$SHELL
