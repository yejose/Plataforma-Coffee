import sqlite3
from sqlite3.dbapi2 import Error

def conectar():
    dbname = "Plataforma.db"
    conn = sqlite3.connect(dbname)
    return conn
    

def addWish(uEmail, pID):

    try:

        conn = conectar()
        conn.execute("insert into Wish (uEmail, pID) values (?, ?);", (uEmail, pID))   
        conn.commit() 
        print("Query enviado")   
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def consultarWish(uEmail):

    try:
        conn = conectar()
        cursor = conn.execute("select pID from Wish WHERE uEmail=?;", (uEmail,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        print("consultar wish:")
        print(resultados)
        if len(resultados) == 0: #Retorna False si no encuentra el registro
            return False

        return resultados

    except Error as error:
        print(error)
        return False

def consultarWishID(pID, uEmail):

    try:
        conn = conectar()
        cursor = conn.execute("select pID from Wish WHERE pID=? AND uEmail=?;", (pID, uEmail))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        print("resultados:", resultados)
        
        if len(resultados) == 0: #Retorna False si no encuentra el registro
            print("SIGUE EN TRY")
            return False

        return True

    except Error as error:
        print(error)
        return False

def eliminarWish(pID, uEmail):

    try:
        
        conn = conectar()
        cursor = conn.execute("select * from Wish where pID=? AND uEmail=?;", (pID,uEmail))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()

        if len(resultados) > 0:#Significa que encontro el registro de arriba       

            conn = conectar()
            conn.execute("delete from Wish where pID=? and uEmail=?;", (pID, uEmail)) #Procede a eliminarlo
            conn.commit()            
            conn.close()
            print("Envio el update")

            resultado = True #True = eliminado
            return resultado

        elif len(resultados) == 0 or resultados == None:
            resultado = False #False = no se encontro
            return resultado
    
    except Error as error:
        print(error)
        resultados = False
        return resultados
