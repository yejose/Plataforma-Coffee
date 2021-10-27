import sqlite3
from sqlite3.dbapi2 import Error
from datetime import date

def conectar():
    dbname = "Plataforma.db"
    conn = sqlite3.connect(dbname)
    return conn

def addBilling(caID, bAddress, bDate):

    try:

        conn = conectar()
        conn.execute("insert into Billing (caID, bAddress, bDate) values (?,?,?);", (caID, bAddress, bDate))
        conn.commit()
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def carritoConsultarEmail(uEmail):

    try:
        conn = conectar()
        cursor = conn.execute("select caID, caDate from Car WHERE uEmail=?;", (uEmail,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        print("Query enviado")
        if len(resultados) == 0: #Retorna False si no encuentra el registro
            flag = False
            return flag

        return resultados

    except Error as error:
        print(error)
        return False