# Pasos para Levanar el Backend:
* Crear el entorno virtual:
    - Para crear el entorno virtual debe de terner instalado la libreria virtualenv, se instala con el comnado: "pip install virtualenv".
    - Una vez instalada con la consola navegue hacia la raiz del proyecto y escriba el siguiente comando: "virtualenv" para crear el entorno.

* Activar el entorno:
    - Para activar el entorno vaya a la siguiente ruta raiz del proyecto/carpeta del entorno/Scripts, utilizando la consola.
    - Luego de estar ahi escriba en la consola "activate" y vera a la izquiera del todo de la entrada de comandos algo como (entorno), esto es que esta activado.

* Crear las variables de entorno:
    - Para crear las variables de entorno debe de ir a la raiz del proyecto y crear un archivo .env y dentro pegar lo que esta en la seccion "variables de entorno" que esta debajo


* Levantar el servidor con el entorno ativado:
    - Dirijase a la raiz del proyecto nuevamente y ejecute el siguiente comando "python manage.py runserver".



### Variables de Entorno.

* SECRET_KEY=
* ENVIRONMENT=

* DOMAIN=
* PORT=

* DATABASE_URL=
* DATABASE_PORT=
* DATABASE_NAME=
* DATABASE_USER=
* DATABASE_PASSWORD=

* EMAIL_BACKEND=
* DEFAULT_FROM_EMAIL=
* EMAIL_HOST=
* EMAIL_HOST_USER=
* EMAIL_HOST_PASSWORD=
* EMAIL_PORT=
* EMAIL_USE_TLS=

ojo que sin esto el servidor no pincha.
