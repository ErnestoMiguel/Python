import sqlite3

#*********Creacion y Conexion con la base de datos*******
def connect_db(db):
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    return conexion, cursor

def create_db():
    conexion, cursor = connect_db('Candidatos.db')
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Candidatos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT NOT NULL,
                Edad INTEGER NOT NULL,
                Genero TEXT NOT NULL,
                Direccion TEXT NOT NULL,
                Telefono TEXT NOT NULL,
                Acerca TEXT
            )
    """
    )
    conexion.commit()
    conexion.close()

def insert_data(nombre, edad, genero, direccion, telefono, acerca):
    conexion, cursor = connect_db("Candidatos.db")
    cursor.execute("""
        INSERT INTO Candidatos(Nombre, Edad, Genero, Direccion, Telefono, Acerca)
        VALUES (?,?,?,?,?,?)
    """,(nombre, edad, genero, direccion, telefono, acerca)
    )
    conexion.commit()
    conexion.close()

#*********************************************************