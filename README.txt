EASYCOOK "Recetas que nunca se Olvidan"

****************************************
****************************************
La aplicacion fue desarrollada en:
Python 2.7
Django 1.7
HTML5, CSS3, JAVASCRIPT
ES RESPONSIVE
SE DISEÑARON Y SE USARON TEMPLATES
SE UTILIZARON ALGUNOS PLUGINS
SE REALIZA MAQUETACION
SE UTILIZA BOOTSTRAP PARA LAS PLANTILLAS DE LA APLICACION
****************************************
****************************************
REQUISITOS PARA SU CORRECTO FUNCIONAMIENTO.
1.Crear base de datos:
	NAME: easycook
        USER: postgres
        PASSWORD: root
        PORT: 5432

2. Hacer Migracion de Modelos:
	Por Consola Dirigirse a la ruta: Prueba\venv\Scripts
	Ejecutar activate
	Ejecutar manage.py makemigrations
	Ejecutar manage.py migrate
3. Crear Super Usuario:
	Ejecutar manage.py createsuperuser
	***El super usuario es para poder crear Recetas.
4. Ejecutar Aplicacion:
	manage.py runserver

En la aplicacion los usuarios podran ver las recetas como se solicitaron en el requerimiento.
El SuperUsuario es el unico que puede Crear,Eliminar,Actualizar las recetas.
	
	