import sqlite3
from sqlite3.dbapi2 import Error
from datetime import date

def conectar():
    dbname = "Plataforma.db"
    conn = sqlite3.connect(dbname)
    return conn

def addComentario(uEmail, pID, cComment):

    try:
        today = date.today()
        fecha = today.strftime("%d/%m/%Y")

        conn = conectar()
        conn.execute("insert into Comment(pID, uEmail, cComment, cDate) values (?,?,?,?);", (pID, uEmail, cComment, fecha))
        conn.commit()
        print("Query enviado")
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def consultarTodosComentarios(pID):

    try:
        conn = conectar()
        cursor = conn.execute("select * from Comment WHERE pID=?;", (pID,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        
        if len(resultados) == 0:
            
            resultados = False #No habia nada en la tabla
            return resultados

        else:
            
            return resultados #Habia algo en la tabla

    except Error as error:
        print(error)
        return False

def actualizarComentario(cComment, cID):
    
    try:
        conn = conectar()
        conn.execute("update Comment SET cComment=? WHERE cID=?;", (cComment, cID))
        conn.commit()
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def consultarComentario(cComment):

    try:
        conn = conectar()
        cursor = conn.execute("select * from Comment WHERE cID=?;", (cComment,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        if len(resultados) == 0: #Retorna False si no encuentra el registro
            flag = False
            return flag

        return resultados

    except Error as error:
        print(error)
        return False

def consultarComentariosUsuario(uEmail):

    try:
        conn = conectar()
        cursor = conn.execute("select * from Comment WHERE uEmail=?;", (uEmail,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        
        if len(resultados) == 0: #Retorna False si no encuentra el registro
            flag = False
            return flag

        return resultados

    except Error as error:
        print(error)
        return False

def consultarComentariosTodos():

    try:
        conn = conectar()
        cursor = conn.execute("select * from Comment")
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()

        if len(resultados) == 0:
            return False

        return resultados

    except Error as error:
        print(error)
        return False

def eliminarComentario(cID):

    try:
        
        conn = conectar()
        cursor = conn.execute("select * from Comment where cID=?;", (cID,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()

        if len(resultados) > 0:           

            conn = conectar()
            conn.execute("delete from Comment where cID=?;", (cID,))
            conn.commit()            
            conn.close()
            print("Envio el update")

            resultado = True
            return resultado

        elif len(resultados) == 0 or resultados == None:
            resultado = False
            return resultado

    except Error as error:
        print(error)
        resultados = False
        return resultados
