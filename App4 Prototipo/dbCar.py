import sqlite3
from sqlite3.dbapi2 import Error
from datetime import date

def conectar():
    dbname = "Plataforma.db"
    conn = sqlite3.connect(dbname)
    return conn

def carritoCrearPrimeraVez(uEmail, caStatus):

    try:
        today = date.today()#AÑADE LA FECHA ACTUAL
        fecha = today.strftime("%d/%m/%Y")

        conn = conectar()
        conn.execute("insert into Car (uEmail, caDate, caStatus) values (?,?,?);", (uEmail, fecha, caStatus))   
        conn.commit() 
        print("Query enviado")   
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def carritoCrear(pID, uEmail, caAmount, caStatus):

    try:
        today = date.today()#AÑADE LA FECHA ACTUAL
        fecha = today.strftime("%d/%m/%Y")

        conn = conectar()
        conn.execute("insert into Car (pID, uEmail, caAmount, caDate, caStatus) values (?,?,?,?,?);", (pID, uEmail, caAmount, fecha, caStatus))   
        conn.commit() 
        print("Query enviado")   
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def carritoNoCrear(pID, caAmount, caID):

    try:
        conn = conectar()
        conn.execute("update Car set pID=?, caAmount=? WHERE caID=?;", (pID, caAmount, caID))
        conn.commit()
        print("Query enviado")
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def carritoConsultar(caID):

    try:
        conn = conectar()
        cursor = conn.execute("select * from Car WHERE caID=?;", (caID,))
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

def carritoStatus(caID):

    try:
        conn = conectar()
        cursor = conn.execute("select caStatus from Car WHERE caID=?;", (caID,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        return resultados

    except Error as error:
        print(error)
        return False

def carritoIDs(caID):
    try:
        conn = conectar()
        cursor = conn.execute("select pID from Car WHERE caID=?;", (caID,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()
        return resultados

    except Error as error:
        print(error)
        return False

def carritoTodo():

    try:
        conn = conectar()
        cursor = conn.execute("select * from Car;")
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

def carritoTodoID():

    try:
        conn = conectar()
        cursor = conn.execute("select caID from Car;")
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

def carritoEmail(uEmail):

    try:
        conn = conectar()
        cursor = conn.execute("SELECT MAX(caID) FROM Car where uEmail=?;", (uEmail,))
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

def carritoUpdate(caID):

    try:
        conn = conectar()
        conn.execute("update Car SET caStatus=1 WHERE caID=?;", (caID,))
        conn.commit()
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def carritoUpdateFecha(caID):

    try:
        today = date.today()#AÑADE LA FECHA ACTUAL
        fecha = today.strftime("%d/%m/%Y")

        conn = conectar()
        conn.execute("update Car SET caDate=? WHERE caID=?;", (fecha, caID))
        conn.commit()
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def carritoVaciar(caID):

    try:
        conn = conectar()
        conn.execute("update Car set pID=?, caAmount=? WHERE caID=?;", (None, None, caID ))
        conn.commit()
        conn.close()
        return True
    
    except Error as error:
        print(error)
        return False

def carritoAmounts(caID):

    try:
        conn = conectar()
        cursor = conn.execute("select caAmount from Car WHERE caID=?;", (caID,))
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
        
