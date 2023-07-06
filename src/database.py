import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crud-flask_2'
)

class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

#-----------------------------------------------------
#Apartado en el que se configura los datos del usuario.
#-----------------------------------------------------

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'crud-flask_2'

#-----------------------------------------------------
#Apartado de para definir la configuración general de la base de datos.
#-----------------------------------------------------

config={
    'development':DevelopmentConfig
}