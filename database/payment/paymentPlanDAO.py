import psycopg2
import json

from database.payment.paymentPlanTableDTO import paymentPlanTable


with open('env/databaseConfig.json',"r") as f:
   secretConfig = json.load(f)

"""
Controlador de las tablas (Crear y borrar tablas)

"""

def ObtenerCursor( ) :
    """
    Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones
    """
    DATABASE = secretConfig.get("DATABASE")
    USER = secretConfig.get("USER")
    PASSWORD = secretConfig.get("PASSWORD")
    HOST = secretConfig.get("HOST")
    PORT = secretConfig.get("PORT")
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()

def Crear( creador : paymentPlanTable ):
    """ Guarda un Usuario en la base de datos """

    try:

        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = ObtenerCursor()
        cursor.execute(f"""
        create table paymentplan (
            'card_number {creador.card_number} FOREIGN KEY',
            'purchase_date {creador.purchase_date}',
            'purchase_amount {creador.purchase_amount}',  
            'payment_date {creador.payment_date}',  
            'payment_amount{creador.payment_amount}', 
            'interest_amount {creador.interest_amount}', 
            'capital_amount {creador.capital_amount}', 
            'balance {creador.balance}'
        )
        """)

        # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
        # pero si necesitan commit() para hacer los cambios persistentes
        cursor.connection.commit()
    except  :
        cursor.connection.rollback() 
        raise Exception("No fue posible crear la tabla : " + creador.card_number )