import sqlite3

#Metodo para conectar con la base de datos
def connect_db(db):
    try:
        return sqlite3.connect(db)
    except sqlite3.Error as er:
        print(f"Ha Ocurrido un error de tipo {er}")

#Metodo para crear la base de datos
def create_db(db="Ejemplo.db"):
    try:
        with connect_db(db) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Products(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Prod_name VARCHAR(50),
                        Price DECIMAL(10,2),
                        Section VARCHAR(20)
                        )
            """
            )
            conexion.commit()
    except sqlite3.Error as er:
        print(f"Ha Ocurrido un error de tipo {er}")

#Metodo para insertar datos introducidos por el usuario desde un GUI por ejemplo
def insert_data(prod_name, price, section, db="Ejemplo.db"):
    try:
        with connect_db(db) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Products(Prod_name, Price, Section)
                        VALUES(?,?,?)
                            """,(prod_name, price, section)
            )
            conexion.commit()
    except sqlite3.Error as er:
        print(f"Error de tipo {er}")

#Metodo para la insercion de datos mutiples datos a la vez desde una tupla
def insert_mult_data(tuple, db="Ejemplo.db"):
    try:
        with connect_db(db) as conexion:
            cursor = conexion.cursor()
            cursor.executemany("""
                INSERT INTO Products(Prod_name, Price, Section)
                               Values(?,?,?)
            """,tuple
            )
            conexion.commit()
    except sqlite3.Error as er:
        print(f"Ha Ocurrido un error de tipo {er}")

#Tupla random para usar la funcion insert_mult_data
tuple = [
    ("Arroz 5kg", 250, "Granos"),
    ("Pollo", 144.9, "Carnicos"),
    ("Shampoo", 100, "Aseo Personal")
]

#Metodo para consultar todos los datos de nuestra base de datos
def full_query(db="Ejemplo.db"):
    try:
        with connect_db(db) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Products")
            return cursor.fetchall()
    except sqlite3.Error as er:
        print(f"Ha Ocurrido un error de tipo {er}")
