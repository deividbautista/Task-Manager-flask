# Task-Manager-flask
In this repository the development of a task manager application is observed, making use of tools such as botpstrap 5, and libraries such as MySqlConnector. / En este repositorio se observa el desarrollo de una aplicación administradora de tareas, haciendo uso de herramientas como botpstrap 5, y bibliotecas como MySqlConnector.

## Requisitos previos
* Python [python download](https://www.python.org/downloads/release/python-31010/)
* pip [pip download](https://pip.pypa.io/en/stable/installation/)
---

```sh
# Otorgar permisos a windows en caso de ser solicitados
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process    
```
```sh
# Crear entorno virtual
virtualenv -p python3 env   
```
```sh
# Activar entorno virtual para instalar dependencias
env/Scripts/activate 
```
```sh
# Instalar las dependencias que necesitaremos en este proyecto
pip install -r dependencies.txt 
```
```sh
# Para correr el proyecto
python src/app.py 
```
