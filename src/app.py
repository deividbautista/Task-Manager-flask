from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM procesos")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar usuarios en la Base de datos
@app.route('/proceso', methods=['POST'])
def addUser():
    Titulo = request.form['Titulo']
    Descripcion = request.form['Descripcion']
    Fecha = request.form['fecha']

    if Titulo and Descripcion:
        cursor = db.database.cursor()
        sql = "INSERT INTO procesos (Titulo, Descripcion, Fecha_terminación) VALUES (%s, %s, %s)"
        data = (Titulo, Descripcion, Fecha)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))



@app.route('/delete/<string:idP>')
def delete(idP):
    print(idP)
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

