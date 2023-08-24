# Apartado en el que se importan todos los modulos necesarios para el proyecto.
from flask import Flask, render_template, request, redirect, url_for, jsonify
from random import sample
import os
import database as db

# En este apartado realizamos la configuración de las rutas en flask.
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

# En este apartado inicializamos la configuración de la ruta.
app = Flask(__name__, template_folder = template_dir)

# Definimos la función denominada "idAleatorio", la cual nos retornara un numero 
# generado al azar, dentro de los valores 1 al 9, con una extención o longitud de 9 digitos o 9 caracteres
def idAleatorio():
    # Caracteres que puede poseer el int aleatorio.
    id_aleatorio = "123456789"
    # Logintud determinada para el int aleatorio.
    longitud         = 9
    # Utilizamos la función upper para combertir los caracteres en mayuscula.
    secuencia        = id_aleatorio.upper()
    # Definimos la variable "resultado_aleatorio", que con la función sample 
    # y los parametros de secuencia y longitud, generamos el int aleatorio.
    resultado_aleatorio  = sample(secuencia, longitud)
    # Volvemos a definir a la varibale "id_aleatorio", pero esta vez le 
    # insertamos el valor optenido de "resultado_aleatorio". 
    id_aleatorio     = "".join(resultado_aleatorio)
    # Finalmente retornamos de nuestra función el resultado con el valor aleatorio.
    return id_aleatorio

# Definimos la función que retornara los datos de los usuarios.
def datosUsuarios():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario.
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()  
    #Almacenamos los datos o contenido obtenido de la consulta en la variable dataUser.
    dataUser=insertObject  
    #Retorna la variable dataUser
    return dataUser


# Tenemos la ruta principal donde se visualizaran los procesos almacenados en la BD.
@app.route("/")
def home():
    cursor = db.database.cursor()
    query = """
    SELECT p.*, GROUP_CONCAT(u.id) AS id_usuario, GROUP_CONCAT(u.fullname) AS nombre_usuario
    FROM procesos p
    LEFT JOIN asignaciones a ON p.id_proceso = a.id_proceso
    LEFT JOIN users u ON a.id = u.id
    GROUP BY p.id_proceso;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    dataUser = datosUsuarios()

    # Procesa los resultados para formar una estructura de datos más adecuada
    processed_data = []
    for row in data:
        proceso = {
            "id_proceso": row[0],  # Usar el índice numérico correspondiente
            "Titulo": row[1],      # Usar el índice numérico correspondiente
            "Descripcion": row[2], # Usar el índice numérico correspondiente
            "Fecha_creacion": row[3], # Usar el índice numérico correspondiente
            "Fecha_terminación": row[4], # Usar el índice numérico correspondiente
            "nombre_usuario": row[6].split(",") if row[6] is not None else [],
            "id_usuario": row[5].split(",") if row[5] is not None else [],
        }
        processed_data.append(proceso)

    cursor.close()  # Cierra el cursor aquí
    return render_template("index.html", data=processed_data, datosU=dataUser)


# Ruta para guardar usuarios en la Base de datos.
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
    return redirect(url_for('home'))


# Ruta para eliminar los procesos registrados en la base de datos.
@app.route('/delete/<string:idP>')
def delete(idP):
    dato = (idP)
    cursor = db.database.cursor()
    sql ="DELETE FROM procesos WHERE id_proceso= {}"
    cursor.execute(sql.format(dato))
    db.database.commit()
    return redirect(url_for('home'))


# Ruta para eliminar las asignaciones en los procesos registrados en la base de datos.
@app.route('/deleteAsignacion', methods=['POST'])
def deleteAsignados():
    data = request.json
    idU = data.get("id_asignado")
    idP = data.get("id_proceso")

    cursor = db.database.cursor()
    sql = """DELETE FROM asignaciones
             WHERE id = %s AND id_proceso = %s"""
             
    cursor.execute(sql, (idU, idP))
    db.database.commit()
    return jsonify({"status": "success", "message": idP})


# Ruta para realizar la actualización de los datos de los procesos.
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


# Condicional para dar inicialización al proyecto.
if __name__ == '__main__':   
    app.run(debug=True, port=8000)

