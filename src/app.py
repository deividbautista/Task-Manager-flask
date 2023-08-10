from flask import Flask, render_template, request, redirect, url_for
from random import sample
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)


def idAleatorio():
    # Caracteres que puede poseer el string aleatorio.
    id_aleatorio = "0123456789"
    # Logintud determinada para el estring aleatorio.
    longitud         = 10
    # Utilizamos la función upper para combertir los caracteres en mayuscula.
    secuencia        = id_aleatorio.upper()
    # Definimos la variable "resultado_aleatorio", que con la función sample 
    # y los parametros de secuencia y longitud, generamos el string aleatorio.
    resultado_aleatorio  = sample(secuencia, longitud)
    # Volvemos a definir a la varibale "id_aleatorio", pero esta vez le 
    # concatenamos el valor optenido de "resultado_aleatorio". 
    id_aleatorio     = "".join(resultado_aleatorio)
    # Finalmente retornamos de nuestra función el resultado con el string aleatorio.
    return id_aleatorio

def datosUsuarios():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()  

    dataUser=insertObject  
    return dataUser


#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    # cursor.execute("SELECT * FROM procesos")
    query = """
    SELECT p.*, GROUP_CONCAT(u.fullname) AS users
    FROM procesos p
    LEFT JOIN asignaciones a ON p.id_proceso = a.id_proceso
    LEFT JOIN users u ON a.id = u.id
    GROUP BY p.id_proceso
    """
    cursor.execute(query)
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()   
    dataUser = datosUsuarios()
    
    return render_template('index.html', data=insertObject, datosU=dataUser )



#Ruta para guardar usuarios en la Base de datos
@app.route('/proceso', methods=['POST'])
def addUser():
    Titulo = request.form['Titulo']
    Descripcion = request.form['Descripcion']
    Fecha = request.form['fecha']
    id_proceso = idAleatorio()
    asignados = request.form.getlist('usuarios_seleccionados')

    if Titulo and Descripcion:
        cursor = db.database.cursor()
        sql = "INSERT INTO procesos (id_proceso, Titulo, Descripcion, Fecha_terminación) VALUES (%s, %s, %s, %s)"
        data = (id_proceso, Titulo, Descripcion, Fecha)
        cursor.execute(sql, data)
        db.database.commit()

    if len (asignados) > 0:
        for Numid in asignados:
            cursor = db.database.cursor()
            sql = "INSERT INTO asignaciones (id, id_proceso) VALUES (%s, %s)"
            data = (Numid, id_proceso)
            cursor.execute(sql, data)
            db.database.commit()
            print(Numid)
    return redirect(url_for('home'))



@app.route('/delete/<string:idP>')
def delete(idP):
    dato = (idP)
    cursor = db.database.cursor()
    sql ="DELETE FROM procesos WHERE id_proceso= {}"
    cursor.execute(sql.format(dato))
    db.database.commit()
    return redirect(url_for('home'))


@app.route('/edit/<string:id_proceso>', methods=['POST'])
def edit(id_proceso):
    Titulo = request.form['Titulo']
    Descripcion = request.form['Descripcion']

    if Titulo and Descripcion:
        cursor = db.database.cursor()
        sql="""UPDATE procesos SET Titulo = '{0}', Descripcion = '{1}' WHERE id_proceso = {2}"""
        # Usamos el execute para poder realizar la consulta anteriormente mostrada.
        data = (Titulo, Descripcion, id_proceso)
        cursor.execute(sql.format(data[0],data[1],data[2]))
        db.database.commit()
        
    return redirect(url_for('home'))


if __name__ == '__main__':   
    app.run(debug=True, port=4000)

