# Comandos
```bash
  pip --version
```
Si no tienes `pip` hay que instalarlo para continuar
```bash
  python -m venv venv
```
Miramos qué Python estamos usando:
```bash
  which python # o where python en Windows
```
Windows: 
```bash
  venv\Scripts\activate
```
Mac o Linux: 
```bash
  source venv/bin/activate
```

```bash
  pip list # pip 24...
```

```bash
  pip install django
```

```bash
  pip list
```
```
Package           Version
----------------- -------
asgiref           3.8.1
Django            5.0.6
pip               24.0
setuptools        65.5.0
sqlparse          0.5.0
typing_extensions 4.12.2
```

---

Creamos proyecto de Django:
```bash
  django-admin startproject <nombre_del_proyecto> .
```
Iniciar servidor:
```bash
  python manage.py runserver
```
Aplicar migraciones iniciales:
```bash
  python manage.py migrate
```

```bash
  python manage.py createsuperuser
```

Usando `runserver:`
Ir a `http://127.0.0.1:8000/admin/` y login 