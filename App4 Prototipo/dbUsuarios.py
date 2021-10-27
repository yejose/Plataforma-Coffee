import sqlite3
from sqlite3.dbapi2 import Error
from datetime import date
import random
import string

def createPassword(length):
    
    letters = string.ascii_lowercase
    numbers = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_dig = ''.join(random.choice(numbers) for i in range(length))
    password = result_str+result_dig
    return password
    

def conectar():
    dbname = "Plataforma.db"
    conn = sqlite3.connect(dbname)
    return conn

def addUsuarios(uEmail, uName, uLastname, uPhone, uProfile, uPass):

    try:
        today = date.today()
        fecha = today.strftime("%d/%m/%Y")


        conn = conectar()
        conn.execute("insert into User(uEmail, uName, uLastname, uPhone, uPass, uDate, uProfile) values (?,?,?,?,?,?,?);", (uEmail, uName, uLastname, uPhone, uPass, fecha, uProfile))
        conn.commit()
        print("Query enviado")
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def signupUsuarios(uEmail, uName, uLastname, uPhone, uPass):


    try:
        today = date.today()
        fecha = today.strftime("%d/%m/%Y")
        uProfile = "Usuario"

        conn = conectar()
        conn.execute("insert into User(uEmail, uName, uLastname, uPhone, uPass, uDate, uProfile) values (?,?,?,?,?,?,?);", (uEmail, uName, uLastname, uPhone, uPass, fecha, uProfile))
        conn.commit()
        print("Query enviado")
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def consultarTodosUsuarios():

    try:
        conn = conectar()
        cursor = conn.execute("select * from User;")
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

def consultarUsuarios(uEmail):

    try:
        conn = conectar()
        cursor = conn.execute("select * from User WHERE uEmail=?;", (uEmail,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()     

        if len(resultados) == 0: #No encontro el registro y envia un booleano 
            flag = False
            return flag

        else: #Encontro el registro y envia una lista
            return resultados

    except Error as error:
        print(error)
        return False

def actualizarUsuarios(uName, uEmail, uLastname, uPhone):

    try:

        conn = conectar()
        conn.execute("update User SET uName=?, uLastname=?, uPhone=? WHERE uEmail=?;", (uName, uLastname, uPhone, uEmail,))        
        print("Envio el update")
        conn.commit()
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def actualizarPassword(uEmail, uPassword):

    try:

        conn = conectar()
        conn.execute("update User SET uPass=? WHERE uEmail=?;", (uPassword, uEmail))
        print("Envio el query")
        conn.commit()
        conn.close()
        return True

    except Error as error:
        print(error)
        return False

def deleteUsuarios(uEmail):

    try: #Realiza una busqueda del elemento
        conn = conectar()
        cursor = conn.execute("select * from User where uEmail=?;", (uEmail,))
        resultados = cursor.fetchall()
        conn.commit()
        conn.close()

        if len(resultados) > 0: #Si el registro es encontrado aqui se hace el delete

            conn = conectar()
            conn.execute("delete from User where uEmail=?;", (uEmail,))
            conn.commit()
            conn.execute("delete from Comment where uEmail=?;", (uEmail,))
            conn.commit()
            conn.execute("delete from Rate where uEmail=?;", (uEmail,))
            conn.commit()
            conn.execute("delete from Wish where uEmail=?;", (uEmail,))
            conn.commit()
            print("Envio el update")
            conn.close()
            resultado = True
            return resultado

        elif len(resultados) == 0 or resultados == None: #No lo encuentra
            resultado = False
            return resultado

    except Error as error: #Query fallado
        print(error)
        resultados = False
        return resultados