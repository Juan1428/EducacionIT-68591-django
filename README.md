# Curso EducaciónIT

## Creación del entorno virtual y activación

`python -m venv .venv`
`.\.venv\Scripts\activate`

## Instalación de Django

`pip install django`

## Creación de proyecto

`mkdir project`
`cd project`
`django-admin startproject config .`

## Ejecución del servidor

`python manage.py runserver`

## Aplicar migraciones (base de datos)

`python manage.py makemigrations`
`python manage.py migrate`

## Crear superusuario (para acceder como administrador)

`python manage.py createsuperuser`

## Crear repositorio
`git init`