dofapi
======

API no oficial para el Diario Oficial de la Federación http://dof.gob.mx/
-----

*Prueba de concepto*

**INSTALACIÓN**


pip install -r requirements.txt

editar el archivo scraper/settings.py con el path del usuario

**USO**

scrapy crawl dof

./manage.py runserver


* http://127.0.0.1:8000/api/v1/publicacion/?format=json

* http://127.0.0.1:8000/api/v1/publicacion/1/?format=json


