import sqlite3
from sqlite3.dbapi2 import Error
from datetime import date

def conectar():
    dbname = "Plataforma.db"
    conn = sqlite3.connect(dbname)
    return conn

def addCalificacion(pID, uEmail, rRate):

    try:
        
        conn = conectar()
        conn.execute("insert into Rate(pID, uEmail, rRate) values (?,?,?);", (pID, uEmail, rRate))   
        conn.commit() 
        print("Query enviado")   
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def calificacionRepetida(uEmail, pID):

    
    try:
        conn = conectar()
        cursor = conn.execute("select * from Rate WHERE uEmail=? AND pID=?;", (uEmail, pID))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        print("Query enviado")
        if len(resultados) == 0: #Retorna False si no encuentra el registro
            return False
        
        elif len(resultados) > 0:
            return True

    except Error as error:
        print(error)
        return False

def searchCalifcaciones(pID):

    try:
        conn = conectar()
        cursor = conn.execute("select * from Rate WHERE pID=?;", (pID,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        print("Query enviado")       
        return len(resultados)
    
    except Error as error:
        print(error)
        return False

def promedioCalificaciones(pID):

    try:
        conn = conectar()
        cursor = conn.execute("select rRate from Rate WHERE pID=?;", (pID,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        print("Query enviado")
        if len(resultados) > 0:
            suma = 0
            for i in resultados:
                suma += i[0]
            average = suma/len(resultados)
            average = float(f"{average:.2f}")
            return average
        
        elif len(resultados) == 0:
            return 0
    
    except Error as error:
        print(error)
        return False
