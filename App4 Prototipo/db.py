import sqlite3
from sqlite3.dbapi2 import Error
from datetime import date

def conectar():
    dbname = "Plataforma.db"
    conn = sqlite3.connect(dbname)
    return conn
    

def addProductos(pName, pDescription, pPrice, pAmount, pColor):

    try:
        today = date.today()#AÑADE LA FECHA ACTUAL
        fecha = today.strftime("%d/%m/%Y")

        conn = conectar()
        conn.execute("insert into Product(pName, pPrice, pAmount, pDescription, pColor, pDate) values (?,?,?,?,?,?);", (pName, pPrice, pAmount, pDescription, pColor, fecha))   
        conn.commit() 
        print("Query enviado")   
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def compararProductos(pName):

    try:
        conn = conectar()
        cursor = conn.execute("select * from Product WHERE pName=?;", (str(pName),))
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

def consultarProductos(pID):

    try:
        conn = conectar()
        cursor = conn.execute("select * from Product WHERE pID=?;", (pID,))
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

def consultarTodosProductos():

    try:
        conn = conectar()
        cursor = conn.execute("select * from Product;")
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        
        if len(resultados) == 0:
            
            resultados = False
            return resultados
        else:
            return resultados

    except Error as error:
        print(error)
        return False

def actualizarProductos(pID, pName, pDescription, pPrice, pAmount):
    

    try:

        conn = conectar()
        conn.execute("update Product SET pName=?, pDescription=?, pPrice=?, pAmount=? WHERE pID=?;", (pName, pDescription, pPrice, pAmount, pID,))
        
        print("Envio el update")
        conn.commit()
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def deleteProductos(pID):

    #DELETE FROM table_name WHERE condition;
    try:
        
        conn = conectar()
        cursor = conn.execute("select * from Product where pID=?;", (pID,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()

        if len(resultados) > 0:
            
            conn = conectar()
            conn.execute("delete from Product where pID=?;", (pID,))
            conn.commit()
            conn.execute("delete from Comment where pID=?;", (pID,))
            conn.commit()
            conn.execute("delete from Rate where pID=?;", (pID,))
            conn.commit()
            print("Envio el update")
            conn.close()

            resultado = True
            return resultado



        elif len(resultados) == 0 or resultados == None:
            resultado = False
            return resultado

    except Error as error:
        print(error)
        resultados = False
        return resultados


