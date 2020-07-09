## Página Feria Empresarial
#Proyecto 2016 de Re-Diseño de la página web de la Feria Empresarial.


#Como Instalar:

* Clonar el repositorio utilizando github.
* Ejecutar lo siguiente para instalar las dependencias:
```
python -m pip install -r requeriments.txt
```
* Crear la migración de django utilizando:
```
python manage.py makemigrations
```
* Migrar la base de datos con:
```
python manage.py migrate
```
* En pagina/settings.py cambiar:
```
debug = True
```

#Como Ejecutarlo:

* Ejecutar XAMPP, correr Apache y MySQL.
* Para cargar la BD, desde consola CMD en Windows en la carpeta "PaginaFeria/src" ejecutar:
```
python manage.py migrate
``` 
* Para ejecutar la aplicación: 
``` 
python manage.py runserver 
```
* Dirigirse a 127.0.0.1:8000


