import psycopg2
import json

from creditCardTableDTO import creditCardTableDTO


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


def Crear( creador : creditCardTableDTO ):
    """ Guarda una tarjeta de crédito en la base de datos """

    try:

        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = ObtenerCursor()
        cursor.execute(f"""
        create table creditcard (
            'card_number {creador.card_number}',   
            'owner_id {creador.owner_id}',  
            'owner_name {creador.owner_name}',  
            'bank_name {creador.bank_name}',  
            'due_date{creador.due_date}', 
            'franchise {creador.franchise}', 
            'payment_day {creador.payment_day}', 
            'monthly_fee {creador.monthly_fee}',
            'interest_rate {creador.interest_rate}'
        )
        """)

        # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
        # pero si necesitan commit() para hacer los cambios persistentes
        cursor.connection.commit()
    except  :
        cursor.connection.rollback() 
        raise Exception("No fue posible crear la tabla : " + creador.card_number )


def CreateTable():
    """
    Crea la tabla de usuarios, en caso de que no exista
    """    
    sql = ""
    with open("sql/creditcardCreate.sql","r") as f:
        sql = f.read()

    cursor = ObtenerCursor()
    try:
        cursor.execute( sql )
        cursor.connection.commit()
    except:
        # SI LLEGA AQUI, ES PORQUE LA TABLA YA EXISTE
        cursor.connection.rollback()



def Insertar( creditcard: creditCardTableDTO ):
    """ Guarda una tarjeta de credito en la base de datos """

    try:

        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = ObtenerCursor()
        cursor.execute(f"""
        insert into creditcard (
            card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate
        )
        values 
        (
            '{creditcard.card_number}',  '{creditcard.owner_id}', '{creditcard.owner_name}', '{creditcard.bank_name}', '{creditcard.due_date}', '{creditcard.franchise}', '{creditcard.payment_day}', '{creditcard.monthly_fee}', '{creditcard.interest_rate}'
        );
                       """)


        # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
        # pero si necesitan commit() para hacer los cambios persistentes
        cursor.connection.commit()
    except  :
        cursor.connection.rollback() 
        raise Exception("No fue posible insertar la tarjeta de crédito : " + creditcard.card_number )


def Actualizar( creditcard : creditCardTableDTO ):
    """
    Actualiza los datos de una tarjeta de crédito en la base de datos

    El atributo card_number nunca se debe cambiar, porque es la clave primaria
    """
    cursor = ObtenerCursor()
    cursor.execute(f"""
        update creditcard
        set 
            card_number='{creditcard.card_number}',
            owner_id='{creditcard.owner_id}',
            owner_name='{creditcard.owner_name}',
            bank_name='{creditcard.bank_name}',
            due_date='{creditcard.due_date}',
            franchise='{creditcard.franchise}',
            payment_day='{creditcard.payment_day}'
            monthly_fee='{creditcard.monthly_fee}',
            interest_rate='{creditcard.interest_rate}',
        where card_number='{creditcard.card_number}'
    """)
    # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
    # pero si necesitan commit() para hacer los cambios persistentes
    cursor.connection.commit()


def is_expired(creditcard : creditCardTableDTO):
    pass

def DropTable():
    """
    Borra (DROP) la tabla en su totalidad
    """    
    sql = "drop table creditcard;"
    cursor = ObtenerCursor()
    cursor.execute( sql )
    
def deleteRows():
    """
    Borra todas las filas de la tabla (DELETE)
    ATENCION: EXTREMADAMENTE PELIGROSO.

    Si lo llama en produccion, pierde el empleo
    """
    sql = "delete from creditcard;"
    cursor = ObtenerCursor()
    cursor.execute( sql )

def delete( creditcard : creditCardTableDTO):
    """ Elimina la fila que contiene una tarjeta de credito en la BD """
    sql = f"delete from creditcard where card_number = '{creditcard.card_number}'"
    cursor = ObtenerCursor()
    cursor.execute( sql )
    cursor.connection.commit()


