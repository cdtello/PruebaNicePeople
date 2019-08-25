Se desarrolla las pruebas solicitadas.

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
	
	