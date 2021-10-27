from flask import Flask, request, sessions, url_for, session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
import db, dbUsuarios, dbComentarios, dbCalificaciones, dbWish, dbCar, dbBilling
from flask import Flask, request
from flask_bcrypt import Bcrypt
from datetime import date


#listo
app = Flask(__name__, template_folder="templates")
bcrypt = Bcrypt(app)


#list
@app.route('/products', methods=('GET', 'POST'))
def products():

    if 'user' in session and session['rol'] == "Superadministrador":
        
        if request.method == 'POST':
            print("RECIBIO POST")

            a = request.form
            print(a)

            if 'add_pName' in a.keys():
                print("Ingresa formulario 1")

                pName = request.form.get("add_pName")
                pDescription = request.form.get("add_pDescription")
                pPrice = request.form.get("add_pPrice")
                pAmount = request.form.get("add_pAmount")
                pColor = request.form.get("add_pColor")           

                errors = False

                comparar_pID = db.compararProductos(pName) #Booleano = No hay otro Producto igual
                if isinstance(comparar_pID, bool) == True:
                    print("NO ENCONTRO PRODUCTOS IGUALES")

                    db.addProductos(pName, pDescription, pPrice, pAmount, pColor)
                    tabla = db.consultarTodosProductos()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)
                    if isinstance(tabla, bool) == False: #Tabla llena
                        return render_template("products_sadmin.html", variable_jinja=tabla, username=resultados[0][1])
                    elif tabla == False: #Valida si la tabla esta vacia
                        return render_template("products_sadmin.html", username=resultados[0][1])

                elif isinstance(comparar_pID, bool) == False: #No Booleano = habia otro Producto igual
                    print("ENCONTRO OTRO PRODUCTO IGUAL")
                    tabla = db.consultarTodosProductos()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)
                    if isinstance(tabla, bool) == False: #Tabla llena
                        return render_template("products_sadmin.html", variable_jinja=tabla, error_add_pName="Un producto de nombre similar ya se encuentra registrado.", username=resultados[0][1])
                    elif tabla == False: #Valida si la tabla esta vacia
                        return render_template("products_sadmin.html", username=resultados[0][1])   
                
                # elif errors == True:
                #     print("Hubieron errores en el formulario")               
                

            elif 'search_pID' in a.keys():
                        
                search_pID = request.form.get("search_pID")
                resultado = db.consultarProductos(search_pID)
                correo = session.get('user')
                resultados = dbUsuarios.consultarUsuarios(correo)

                if resultado == False: #No encontro nada
                    print("No encontro la ID")
                    tabla = db.consultarTodosProductos()
                    if isinstance(tabla, bool) == False:
                        return render_template("products_sadmin.html", error_search_pID="No se encontro la ID.", variable_jinja=tabla, username=resultados[0][1])
                    elif tabla == False:
                        return render_template("products_sadmin.html", error_search_pID="No hay productos para buscar.", username=resultados[0][1])
                else:
                    print("Encontro la ID")
                    tabla = db.consultarTodosProductos()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)        
                    return render_template("products_sadmin.html", upgrade_pID=resultado[0][0], upgrade_pName=resultado[0][1], upgrade_pPrice=resultado[0][2], upgrade_pAmount=resultado[0][3], upgrade_pDescription=resultado[0][4], variable_jinja=tabla, username=resultados[0][1])

            elif 'upgrade_pID' in a.keys():

                upgrade_pID = request.form.get("upgrade_pID")
                upgrade_pName = request.form.get("upgrade_pName")
                upgrade_pDescription = request.form.get("upgrade_pDescription")
                upgrade_pPrice = request.form.get("upgrade_pPrice")
                upgrade_pAmount = request.form.get("upgrade_pAmount")
                resultado = db.actualizarProductos(upgrade_pID, upgrade_pName, upgrade_pDescription, upgrade_pPrice, upgrade_pAmount)
                tabla = db.consultarTodosProductos()
                correo = session.get('user')
                resultados = dbUsuarios.consultarUsuarios(correo)
                return render_template("products_sadmin.html", variable_jinja=tabla, Confirmation="Producto actualizado.", username=resultados[0][1])

            elif 'delete_pID' in a.keys():

                delete_pID = request.form.get("delete_pID")
                print("Entro boton Eliminar")
                print(delete_pID)
                resultado = db.deleteProductos(delete_pID)
                correo = session.get('user')
                resultados = dbUsuarios.consultarUsuarios(correo)
                if resultado == True: #Codear logica para borrar comentarios y comentarios
                    tabla = db.consultarTodosProductos()
                    if isinstance(tabla, bool) == False:                    
                        return render_template("products_sadmin.html", variable_jinja=tabla, confirmation_delete="Producto eliminado.", username=resultados[0][1])
                    elif tabla == False:
                        return render_template("products_sadmin.html", confirmation_delete="Producto eliminado.", username=resultados[0][1])                  
                        

                elif resultado == False:
                    print("Entra al False")
                    tabla = db.consultarTodosProductos()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)
                    if isinstance(tabla, bool) == False:
                        return render_template("products_sadmin.html", variable_jinja=tabla, error_delete_pID="Producto no existente.", username=resultados[0][1])
                    elif tabla == False:
                        return render_template("products_sadmin.html", error_delete_pID="No hay productos para Eliminar.", username=resultados[0][1])
                

        elif request.method == 'GET':

            tabla = db.consultarTodosProductos()
            correo = session.get("user")
            resultados = dbUsuarios.consultarUsuarios(correo)
            if isinstance(tabla, bool) == False:
                return render_template("products_sadmin.html", variable_jinja=tabla, error_add_pName="", username=resultados[0][1])
            elif tabla == False:
                return render_template("products_sadmin.html", error_add_pName="", username=resultados[0][1])
    
    elif 'user' in session and session['rol'] == "Administrador":

        if request.method == 'POST':
            print("RECIBIO POST")

            a = request.form
            print(a)

            if 'add_pName' in a.keys():
                print("Ingresa formulario 1")

                pName = request.form.get("add_pName")
                pDescription = request.form.get("add_pDescription")
                pPrice = request.form.get("add_pPrice")
                pAmount = request.form.get("add_pAmount")
                pColor = request.form.get("add_pColor")           

                errors = False

                comparar_pID = db.compararProductos(pName) #Booleano = No hay otro Producto igual
                if isinstance(comparar_pID, bool) == True:
                    print("NO ENCONTRO PRODUCTOS IGUALES")

                    db.addProductos(pName, pDescription, pPrice, pAmount, pColor)
                    tabla = db.consultarTodosProductos()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)
                    if isinstance(tabla, bool) == False: #Tabla llena
                        return render_template("products_admin.html", variable_jinja=tabla, username=resultados[0][1])
                    elif tabla == False: #Valida si la tabla esta vacia
                        return render_template("products_admin.html", username=resultados[0][1])

                elif isinstance(comparar_pID, bool) == False: #No Booleano = habia otro Producto igual
                    print("ENCONTRO OTRO PRODUCTO IGUAL")
                    tabla = db.consultarTodosProductos()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)
                    if isinstance(tabla, bool) == False: #Tabla llena
                        return render_template("products_admin.html", variable_jinja=tabla, error_add_pName="Un producto de nombre similar ya se encuentra registrado.", username=resultados[0][1])
                    elif tabla == False: #Valida si la tabla esta vacia
                        return render_template("products_admin.html", username=resultados[0][1])   
                
                # elif errors == True:
                #     print("Hubieron errores en el formulario")               
                

            elif 'search_pID' in a.keys():
                        
                search_pID = request.form.get("search_pID")
                resultado = db.consultarProductos(search_pID)
                correo = session.get('user')
                resultados = dbUsuarios.consultarUsuarios(correo)

                if resultado == False: #No encontro nada
                    print("No encontro la ID")
                    tabla = db.consultarTodosProductos()
                    if isinstance(tabla, bool) == False:
                        return render_template("products_admin.html", error_search_pID="No se encontro la ID.", variable_jinja=tabla, username=resultados[0][1])
                    elif tabla == False:
                        return render_template("products_admin.html", error_search_pID="No hay productos para buscar.", username=resultados[0][1])
                else:
                    print("Encontro la ID")
                    tabla = db.consultarTodosProductos()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)        
                    return render_template("products_admin.html", upgrade_pID=resultado[0][0], upgrade_pName=resultado[0][1], upgrade_pPrice=resultado[0][2], upgrade_pAmount=resultado[0][3], upgrade_pDescription=resultado[0][4], variable_jinja=tabla, username=resultados[0][1])

            elif 'upgrade_pID' in a.keys():

                upgrade_pID = request.form.get("upgrade_pID")
                upgrade_pName = request.form.get("upgrade_pName")
                upgrade_pDescription = request.form.get("upgrade_pDescription")
                upgrade_pPrice = request.form.get("upgrade_pPrice")
                upgrade_pAmount = request.form.get("upgrade_pAmount")
                resultado = db.actualizarProductos(upgrade_pID, upgrade_pName, upgrade_pDescription, upgrade_pPrice, upgrade_pAmount)
                tabla = db.consultarTodosProductos()
                correo = session.get('user')
                resultados = dbUsuarios.consultarUsuarios(correo)
                return render_template("products_admin.html", variable_jinja=tabla, Confirmation="Producto actualizado.", username=resultados[0][1])

            elif 'delete_pID' in a.keys():

                delete_pID = request.form.get("delete_pID")
                print("Entro boton Eliminar")
                print(delete_pID)
                resultado = db.deleteProductos(delete_pID)
                correo = session.get('user')
                resultados = dbUsuarios.consultarUsuarios(correo)
                if resultado == True: #Codear logica para borrar comentarios y comentarios
                    tabla = db.consultarTodosProductos()
                    if isinstance(tabla, bool) == False:                    
                        return render_template("products_admin.html", variable_jinja=tabla, confirmation_delete="Producto eliminado.", username=resultados[0][1])
                    elif tabla == False:
                        return render_template("products_admin.html", confirmation_delete="Producto eliminado.", username=resultados[0][1])                  
                        

                elif resultado == False:
                    print("Entra al False")
                    tabla = db.consultarTodosProductos()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)
                    if isinstance(tabla, bool) == False:
                        return render_template("products_admin.html", variable_jinja=tabla, error_delete_pID="Producto no existente.", username=resultados[0][1])
                    elif tabla == False:
                        return render_template("products_admin.html", error_delete_pID="No hay productos para Eliminar.", username=resultados[0][1])
                

        elif request.method == 'GET':

            tabla = db.consultarTodosProductos()
            correo = session.get("user")
            resultados = dbUsuarios.consultarUsuarios(correo)
            if isinstance(tabla, bool) == False:
                return render_template("products_admin.html", variable_jinja=tabla, error_add_pName="", username=resultados[0][1])
            elif tabla == False:
                return render_template("products_admin.html", error_add_pName="", username=resultados[0][1])

    return "<h1>Contenido inexistente</h1>"

#RUTA USUARIO

@app.route('/users', methods=('GET', 'POST'))
def users():
    print("Entro a la ruta")
    
    if 'user' in session and session['rol'] == "Superadministrador":   

        if request.method == 'POST':
            print("ENTRA AL POST")
            a = request.form
            print("formulario enviado:")
            print(a)

            if 'add_uName' in a.keys(): #Formulario Agregar
                print("Ingresa a formulario 1")

                uName = request.form.get("add_uName")
                uLastname = request.form.get("add_uLastname")
                uEmail = request.form.get("add_uEmail")
                uPhone = request.form.get("add_uPhone")
                uProfile = request.form.get("add_uProfile")
                uPassword = request.form.get("add_uPassword")
                pw_hash = bcrypt.generate_password_hash(uPassword)

                errors = False 

                if errors == False: #Valida si hubieron errores de  sintaxis del lado del servidor
                    print(uProfile)
                    comparar_uEmail = dbUsuarios.consultarUsuarios(uEmail) #Booleano = No hay otro Email igual
                    if isinstance(comparar_uEmail, bool) == True:
                        print("NO ENCONTRO EMAILS IGUALES")

                        dbUsuarios.addUsuarios(uEmail, uName, uLastname, uPhone, uProfile, pw_hash)
                        tabla = dbUsuarios.consultarTodosUsuarios()
                        correo = session.get("user")
                        resultados = dbUsuarios.consultarUsuarios(correo)
                        if isinstance(tabla, bool) == False: #Tabla llena
                            return render_template("users_sadmin.html", variable_jinja=tabla, username=resultados[0][1])
                        elif tabla == False: #Valida si la tabla esta vacia
                            return render_template("users_sadmin.html", username=resultados[0][1])
                        
                    elif isinstance(comparar_uEmail, bool) == False: #No Booleano = habia otro Email igual
                        print("ENCONTRO OTRO EMAIL IGUAL")
                        tabla = dbUsuarios.consultarTodosUsuarios()
                        correo = session.get("user")
                        resultados = dbUsuarios.consultarUsuarios(correo)
                        if isinstance(tabla, bool) == False: #Tabla llena
                            return render_template("users_sadmin.html", variable_jinja=tabla, error_add_uEmail="Este correo ya se encuentra registrado.", username=resultados[0][1])
                        elif tabla == False: #Valida si la tabla esta vacia
                            return render_template("users_sadmin.html", username=resultados[0][1])           

                elif errors == True:
                    #Hubieron errores de sintaxis
                    print("errors ="+errors)


            elif 'search_uEmail' in a.keys():
                
                search_uEmail = request.form.get("search_uEmail")
                print(search_uEmail)
                resultado = dbUsuarios.consultarUsuarios(search_uEmail)
                correo = session.get('user')
                resultados = dbUsuarios.consultarUsuarios(correo)

                print("::::::::BLOQUE A EVALUAR:::::::")
                print(correo)
                print(search_uEmail)
                print("::::::::BLOQUE A EVALUAR:::::::")

                if correo == search_uEmail:
               
                        tabla = dbUsuarios.consultarTodosUsuarios()
                        
                        if isinstance(tabla, bool) == False: #No habian registros                   
                            return render_template("users_sadmin.html", error_search_uEmail="No puedes editarte a ti mismo desde esta pagina, dirigete a tu Perfil para realizar la respectiva edicion", variable_jinja=tabla, username=resultados[0][1])
                        elif tabla == False: #Habian registros
                            return render_template("users_sadmin.html", error_search_uEmail="No puedes editarte a ti mismo desde esta pagina, dirigete a tu Perfil para realizar la respectiva edicion", username=resultados[0][1])

                else:

                    if resultado == False: #No encontro el Email

                        print("No se encontro el Email")
                        tabla = dbUsuarios.consultarTodosUsuarios()
                        
                        if isinstance(tabla, bool) == False: #No habian registros                   
                            return render_template("users_sadmin.html", error_search_uEmail="No se encontro el Email", variable_jinja=tabla, username=resultados[0][1])
                        elif tabla == False: #Habian registros
                            return render_template("users_sadmin.html", error_search_uEmail="No hay usuarios para buscar", username=resultados[0][1])                            
                    
                    else:
                        print("Encontro el Email")
                        print(resultado[0][0])
                        tabla = dbUsuarios.consultarTodosUsuarios()
                        correo = session.get('user')
                        resultados = dbUsuarios.consultarUsuarios(correo)              
                        return render_template("users_sadmin.html", upgrade_uEmail=resultado[0][0], upgrade_uName=resultado[0][1], upgrade_uLastname=resultado[0][2], upgrade_uPhone=resultado[0][3], variable_jinja=tabla, username=resultados[0][1])

            elif 'upgrade_uEmail' in a.keys():

                print("Entro a boton Actualizar")

                upgrade_uEmail = request.form.get("upgrade_uEmail")
                upgrade_Lastname = request.form.get("upgrade_uLastname")
                upgrade_uPhone = request.form.get("upgrade_uPhone")
                upgrade_uName = request.form.get("upgrade_uName")

                print(upgrade_uEmail)
                print(session.get("user"))

                if session.get("user") == upgrade_uEmail: #Evalua que el superadministrador no se edite a si mismo desde gestion de usuarios

                    tabla = dbUsuarios.consultarTodosUsuarios() 
                    print("TABLA:::::")
                    print(tabla)
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo) 
                    return render_template("users_sadmin.html", variable_jinja=tabla, error_search_uEmail="No puedes editarte a ti mismo desde esta pagina, dirigete a tu Perfil para poder editarlo", username= resultados[0][1])

                else:

                    resultado = dbUsuarios.actualizarUsuarios(upgrade_uName, upgrade_uEmail, upgrade_Lastname, upgrade_uPhone)
                    print(resultado)#Imprimimos si la base de datos encontro el Email o no
                    tabla = dbUsuarios.consultarTodosUsuarios() 
                    print("TABLA:::::")
                    print(tabla)
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo) 
                    return render_template("users_sadmin.html", variable_jinja=tabla, Confirmation="Usuario actualizado.", username= resultados[0][1])
                
            elif 'delete_uEmail' in a.keys():

                delete_uEmail = request.form.get("delete_uEmail")
                print("Entro boton Eliminar")
                print(delete_uEmail)

                correo = session.get("user")
                if correo == delete_uEmail:

                    tabla = dbUsuarios.consultarTodosUsuarios()
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo)
                    print(tabla)
                    if isinstance(tabla, bool) == False: 
                        return render_template("users_sadmin.html", variable_jinja=tabla, error_delete_uEmail="No puedes Eliminar tu usuario desde esta pagina, dirigete hacia tu Perfil para realizar el respectivo proceso.", username=resultados[0][1])
                    elif tabla == False: 
                        return render_template("users_sadmin.html", error_delete_uEmail="No puedes Eliminar tu usuario desde esta pagina, dirigete hacia tu Perfil para realizar el respectivo proceso.", username=resultados[0][1])
                   
                else:
                    
                    resultado = dbUsuarios.deleteUsuarios(delete_uEmail)
                    print(resultado)
                    if resultado == True: #Encontro el registro y lo elimino
                        print("Entra al True")

                        tabla = dbUsuarios.consultarTodosUsuarios()
                        correo = session.get('user')
                        resultados = dbUsuarios.consultarUsuarios(correo)
                        print(tabla)
                        if isinstance(tabla, bool) == False: 
                            return render_template("users_sadmin.html", variable_jinja=tabla, confirmation_delete="Usuario eliminado.", username=resultados[0][1])
                        elif tabla == False: 
                            return render_template("users_sadmin.html", confirmation_delete="Usuario eliminado.", username=resultados[0][1])
                    
                    elif resultado == False: #No encontro el registro
                        print("Entra al False")
                        tabla = dbUsuarios.consultarTodosUsuarios()
                        correo = session.get('user')
                        resultados = dbUsuarios.consultarUsuarios(correo)
                        if isinstance(tabla, bool) == False: #Habian datos en la tabla
                            return render_template("users_sadmin.html", variable_jinja=tabla, error_delete_uEmail="Usuario no existente.", username=resultados[0][1])
                        elif tabla == False: #No habian datos en la tabla
                            return render_template("users_sadmin.html", error_delete_uEmail="No hay usuarios para Eliminar.", username=resultados[0][1])
        

        if request.method == 'GET':
            print("Entra al GET")
            
            tabla = dbUsuarios.consultarTodosUsuarios()
            correo = session.get('user')
            resultados = dbUsuarios.consultarUsuarios(correo)
            if tabla == False:
                return render_template("users_sadmin.html", variable_jinja=tabla, username=resultados[0][1])
            else:
                
                return render_template("users_sadmin.html", variable_jinja=tabla, username=resultados[0][1])
    
    return "<h1>Contenido inexistente</h1>"

app.secret_key = "abc1234"

@app.route('/login', methods=('GET', 'POST'))
def login():

    session.pop("user", None)

    print("ingreso a la ruta login")
    if request.method == 'POST':
        print("ingreso al formulario login")
        uEmail = request.form.get("login_uEmail")
        uPassword = str(request.form.get("login_uPassword"))
        
        errors = False
        if errors == False:

            print("entró al false del login")
            resultados = dbUsuarios.consultarUsuarios(uEmail)
          
            if isinstance(resultados, bool) == True: 
                print("NO ENCONTRO EMAIL")
                return render_template("login.html", error_login_uEmail="Este correo no se encuentra registrado.")
    
            elif isinstance(resultados, bool) == False:
                print("ENCONTRÓ EMAIL EN LA BD y la contraseña")
                print(resultados)
                
                # if uPassword == resultados[0][4]:
                print(resultados[0][4])
                pwHash = resultados[0][4]
                
                print(pwHash)
                print(uPassword)

                respuesta = bcrypt.check_password_hash(pwHash, uPassword)
                print(respuesta)
                if respuesta == True:
                    
                    print("CONTRASEÑAS SON IGUALES")
                    session['user'] = resultados[0][0]
                    session['rol'] = resultados[0][6]
                    print(session)
                    return redirect('/home')    

                else:
                    return render_template("login.html", error_login_uPassword="La contraseña es incorrecta.")
                
                

        elif errors == True:
            print("errors ="+errors)

    return render_template("login.html")

@app.route('/home', methods=('GET', 'POST'))
def home():

    print("Ingreso a /home")

    
    if 'user' in session and session['rol'] == "Usuario":
        print("INGRESO COMO USUARIO")
        productos = db.consultarTodosProductos()

        # if request.method == 'POST':
            
        #     a = request.form
            
        #     if 'search_bar' in a.keys():
            
        #         busqueda = request.form.get("search_bar")
        #         print(busqueda)
        #         return "<h1>Revisar consola</h1>"
        
        if request.method == 'GET':
            print("ENTRO A GET")
            correo = session.get('user')
            resultados = dbUsuarios.consultarUsuarios(correo)

            if isinstance(productos, bool) == True:
                print("No detecto productos en la base de datos")
                return render_template("home_user.html", productos_jinja=productos, Mensaje_respuesta="No hay productos registrados.", username=resultados[0][1])

            elif isinstance(productos, bool) == False:

                return render_template("home_user.html", productos_jinja=productos, Mensaje_respuesta="Estos son nuestros productos.", username=resultados[0][1])

    elif 'user' in session and session['rol'] == "Superadministrador":

        print("INGRESO COMO USUARIO")
        productos = db.consultarTodosProductos()
        
        if request.method == 'GET':
            print("ENTRO A GET")
            correo = session.get('user')
            resultados = dbUsuarios.consultarUsuarios(correo)
            print(resultados)

            if isinstance(productos, bool) == True:
                print("No detecto productos en la base de datos")
                return render_template("home_sadmin.html", productos_jinja=productos, Mensaje_respuesta="No hay productos registrados.", username=resultados[0][1])

            elif isinstance(productos, bool) == False:

                return render_template("home_sadmin.html", productos_jinja=productos, Mensaje_respuesta="Estos son nuestros productos.", username=resultados[0][1])   

    elif 'user' in session and session['rol'] == "Administrador":

        print("INGRESO COMO USUARIO")
        productos = db.consultarTodosProductos()
        
        if request.method == 'GET':
            print("ENTRO A GET")
            correo = session.get('user')
            resultados = dbUsuarios.consultarUsuarios(correo)
            print(resultados)

            if isinstance(productos, bool) == True:
                print("No detecto productos en la base de datos")
                return render_template("home_admin.html", productos_jinja=productos, Mensaje_respuesta="No hay productos registrados.", username=resultados[0][1])

            elif isinstance(productos, bool) == False:

                return render_template("home_admin.html", productos_jinja=productos, Mensaje_respuesta="Estos son nuestros productos.", username=resultados[0][1])  

    return redirect('/login')
    
@app.route('/signup', methods=('GET', 'POST'))
def signup():

    session.clear()
    # session.Abandon()

    if request.method == 'POST':
        # a = request.form
        # print("formulario enviado:")
        # print(a)

        # if 'signup_uName' in a.keys():
        print("Ingresa formulario")
     
        uName = request.form.get("signup_uName")
        uLastname = request.form.get("signup_uLastname")
        uEmail = request.form.get("signup_uEmail")
        uPhone = request.form.get("signup_uPhone")
        uPassword = request.form.get("signup_uPassword")
        pw_hash = bcrypt.generate_password_hash(uPassword)

        errors = False

        if errors == False:

            comparar_uEmail = dbUsuarios.consultarUsuarios(uEmail)
            if isinstance(comparar_uEmail, bool) == True:
                print("NO ENCONTRO EMAILS IGUALES")

                dbUsuarios.signupUsuarios(uEmail, uName, uLastname, uPhone, pw_hash)
                dbCar.carritoCrearPrimeraVez(uEmail, 0)

                return redirect('/home')

            elif isinstance(comparar_uEmail, bool) == False:
                print("ENCONTRO OTRO EMAIL IGUAL")
                return render_template("signup.html", error_signup_uEmail="Este correo ya se encuentra registrado.")

        elif errors == True:
            print("errors ="+errors)

    elif request.method == 'GET':

        pass

    return render_template("signup.html")

@app.route('/plato/<pID>', methods=('GET', 'POST'))
def plato(pID):

    if 'user' in session and session['rol'] == "Usuario":

        if request.method == 'POST':

            print("RECIBIO POST") 
            ID_respaldo = request.args['pID']
            print(ID_respaldo)     

            a = request.form
            print(a)

            if 'car_pID' in a.keys():
                
                #Agarro datos del formulario del plato para llevarlos al carrito
                caAmount = request.form.get("add_caAmount")
                caAmount = int(caAmount[0])+1

                capID = request.args['pID'] #ID del producto actual
                correo = session.get("user") #ID del usuario actual
                print(caAmount, capID, correo)
                ultimo_carrito = dbCar.carritoEmail(correo) #ID del ultimo carrito del usuario actual
                caID = ultimo_carrito[0][0] #ID del carrito

                confirmar_repite = dbCar.carritoConsultar(caID) #Se trae todo el carrito anterior para comparar sus pIDs
                print(confirmar_repite)

                if confirmar_repite[0][1]== None or confirmar_repite[0][1] == "": #Si entra es nuevo

                    print("detecto que el carrito es nuevo")
                    status_anterior = dbCar.carritoStatus(caID) 
                    status = status_anterior[0][0]
                    print(status)

                    if int(status) == 0: #El carrito anterior no ha sido cancelado
                        print("entra a estatus 0")
                        capID = str(capID)
                        caAmount = str(caAmount)
                        confirmacion = dbCar.carritoNoCrear(capID, caAmount, caID)
                        print(confirmacion)
                        
                        ID = request.args['pID']
                        correo = session.get("user")
                        print(ID)
                        resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
                        tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
                        calificaciones = dbCalificaciones.searchCalifcaciones(ID)
                        consulta = dbWish.consultarWishID(ID, correo)
                        cantidad = resultados[0][3]
                        if cantidad > 5:
                            cantidad = 5
                        print(consulta)
                        if consulta == False:
                            if isinstance(resultados, bool) == False: #Existe el producto

                                if isinstance(tabla, bool) == False: #Encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("Encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                elif isinstance(tabla, bool) == True: #No encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("No encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                            elif isinstance(resultados, bool) == True: #No existe el producto

                                correo = session.get('user')
                                resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                print("El producto no existe")
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                        elif consulta == True:

                            if isinstance(resultados, bool) == False: #Existe el producto

                                if isinstance(tabla, bool) == False: #Encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("Encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                elif isinstance(tabla, bool) == True: #No encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("No encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                            elif isinstance(resultados, bool) == True: #No existe el producto

                                correo = session.get('user')
                                resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                print("El producto no existe")
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")                        

                    
                    elif int(status) == 1: #El carrito ha sido cancelado (opcion poco probable)
                        print("entra a estatus 1")
                        status_nuevo = 0
                        capID = str(capID)
                        caAmount = str(caAmount)
                        confirmacion = dbCar.carritoCrear(capID, correo, caAmount, status_nuevo)
                        print(confirmacion)
                        
                        ID = request.args['pID']
                        correo = session.get("user")
                        print(ID)
                        resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
                        tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
                        calificaciones = dbCalificaciones.searchCalifcaciones(ID)
                        consulta = dbWish.consultarWishID(ID, correo)
                        cantidad = resultados[0][3]
                        if cantidad > 5:
                            cantidad = 5
                        print(consulta)
                        if consulta == False:
                            if isinstance(resultados, bool) == False: #Existe el producto

                                if isinstance(tabla, bool) == False: #Encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("Encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                elif isinstance(tabla, bool) == True: #No encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("No encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                            elif isinstance(resultados, bool) == True: #No existe el producto

                                correo = session.get('user')
                                resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                print("El producto no existe")
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                        elif consulta == True:

                            if isinstance(resultados, bool) == False: #Existe el producto

                                if isinstance(tabla, bool) == False: #Encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("Encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                elif isinstance(tabla, bool) == True: #No encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("No encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                            elif isinstance(resultados, bool) == True: #No existe el producto

                                correo = session.get('user')
                                resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                print("El producto no existe")
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                              
                else:
                    print("NO es nuevo")
                    #Aqui evaluamos si se repite
                    #No se repite, ahora se añade un carrito, para ello necesitamos saber el estatus del ultimo carrito

                    #     print("Evaluar estatus del carrito anterior, añadir o crear en carrito y renderizar vista de plato nuevamente sin mensaje de error")
                    status_anterior = dbCar.carritoStatus(caID) 
                    status = status_anterior[0][0] #Status del ultimo carrito
                    print("DATOS DEL ULTIMO CARRITO:")
                    print(caID, status)
                    
                    if int(status) == 0: #El carrito anterior no ha sido cancelado

                        flag = False
                        pID_comparar = confirmar_repite[0][1].split("-")                
                        if capID in pID_comparar:
                            flag = True
                        
                        if flag == True: #Evalua si se repite
                        #     #Si es true se recarga la vista con mensaje de error
                            
                            ID = request.args['pID']
                            correo = session.get("user")
                            print(ID)
                            resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
                            tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
                            calificaciones = dbCalificaciones.searchCalifcaciones(ID)
                            consulta = dbWish.consultarWishID(ID, correo)
                            cantidad = resultados[0][3]
                            if cantidad > 5:
                                cantidad = 5
                            print(consulta)
                            if consulta == False:
                                if isinstance(resultados, bool) == False: #Existe el producto

                                    if isinstance(tabla, bool) == False: #Encontro comentarios
                                        correo = session.get('user')
                                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                        print("Encontro comentarios relacionados al producto")
                                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Warning="Producto ya se encuentra en carrito")
                                    elif isinstance(tabla, bool) == True: #No encontro comentarios
                                        correo = session.get('user')
                                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                        print("No encontro comentarios relacionados al producto")
                                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Warning="Producto ya se encuentra en carrito")

                                elif isinstance(resultados, bool) == True: #No existe el producto

                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                    print("El producto no existe")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Warning="Producto ya se encuentra en carrito")

                            elif consulta == True:

                                if isinstance(resultados, bool) == False: #Existe el producto

                                    if isinstance(tabla, bool) == False: #Encontro comentarios
                                        correo = session.get('user')
                                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                        print("Encontro comentarios relacionados al producto")
                                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Warning="Producto ya se encuentra en carrito")
                                    elif isinstance(tabla, bool) == True: #No encontro comentarios
                                        correo = session.get('user')
                                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                        print("No encontro comentarios relacionados al producto")
                                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Warning="Producto ya se encuentra en carrito")

                                elif isinstance(resultados, bool) == True: #No existe el producto

                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                    print("El producto no existe")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Warning="Producto ya se encuentra en carrito")
                               
                        elif flag == False:
                        
                            datos_carrito_anterior = dbCar.carritoConsultar(caID) #Se trae los datos (productos y cantidades) del ultimo carrito para poder hacer el update
                            print(datos_carrito_anterior)
                            capID = "-"+str(capID)
                            caAmount = "-"+str(caAmount)
                            pID_actualizado = str(datos_carrito_anterior[0][1]) + capID #Agrega el nuevo producto a la lista de productos del carrito antigua                         
                            caAmount_actualizado = datos_carrito_anterior[0][3] + caAmount
                            print(pID_actualizado)
                            print(caAmount_actualizado)
                            confirmacion = dbCar.carritoNoCrear(pID_actualizado, caAmount_actualizado, caID)
                            print(confirmacion)
                            
                            ID = request.args['pID']
                            correo = session.get("user")
                            print(ID)
                            resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
                            tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
                            calificaciones = dbCalificaciones.searchCalifcaciones(ID)
                            consulta = dbWish.consultarWishID(ID, correo)
                            cantidad = resultados[0][3]
                            if cantidad > 5:
                                cantidad = 5
                            print(consulta)
                            if consulta == False:
                                if isinstance(resultados, bool) == False: #Existe el producto

                                    if isinstance(tabla, bool) == False: #Encontro comentarios
                                        correo = session.get('user')
                                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                        print("Encontro comentarios relacionados al producto")
                                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                    elif isinstance(tabla, bool) == True: #No encontro comentarios
                                        correo = session.get('user')
                                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                        print("No encontro comentarios relacionados al producto")
                                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                                elif isinstance(resultados, bool) == True: #No existe el producto

                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                    print("El producto no existe")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                            elif consulta == True:

                                if isinstance(resultados, bool) == False: #Existe el producto

                                    if isinstance(tabla, bool) == False: #Encontro comentarios
                                        correo = session.get('user')
                                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                        print("Encontro comentarios relacionados al producto")
                                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                    elif isinstance(tabla, bool) == True: #No encontro comentarios
                                        correo = session.get('user')
                                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                        print("No encontro comentarios relacionados al producto")
                                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                                elif isinstance(resultados, bool) == True: #No existe el producto

                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                    print("El producto no existe")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                            
                        
                    
                    elif int(status) == 1: #El carrito ha sido cancelado
                        #Aqui el carrito solo ingresa una vez, se ponen los primeros valores y se crea un carrito en estatus 0, por tanto no vuelve a pasar por aqui
                        #Por aca tampoco se repite el carrito puesto que aqui es donde se ingresa el primer producto, no hay repetidos
                        status_nuevo = 0
                        capID = str(capID)
                        caAmount = str(caAmount)
                        confirmacion = dbCar.carritoCrear(capID, correo, caAmount, status_nuevo)
                        print(confirmacion)
                        
                        ID = request.args['pID']
                        correo = session.get("user")
                        print(ID)
                        resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
                        tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
                        calificaciones = dbCalificaciones.searchCalifcaciones(ID)
                        consulta = dbWish.consultarWishID(ID, correo)
                        cantidad = resultados[0][3]
                        if cantidad > 5:
                            cantidad = 5
                        print(consulta)
                        if consulta == False:
                            if isinstance(resultados, bool) == False: #Existe el producto

                                if isinstance(tabla, bool) == False: #Encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("Encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])
                                elif isinstance(tabla, bool) == True: #No encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("No encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])

                            elif isinstance(resultados, bool) == True: #No existe el producto

                                correo = session.get('user')
                                resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                print("El producto no existe")
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                        elif consulta == True:

                            if isinstance(resultados, bool) == False: #Existe el producto

                                if isinstance(tabla, bool) == False: #Encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("Encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                elif isinstance(tabla, bool) == True: #No encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                                    print("No encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")

                            elif isinstance(resultados, bool) == True: #No existe el producto

                                correo = session.get('user')
                                resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                                print("El producto no existe")
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0], Confirmation="Producto agregado al carrito")
                                  
                
                return "<h1>Revisa la consola</h1>"

            elif 'add_rRate' in a.keys():

                platoID = request.args['pID']
                rRate = request.form.get("add_rRate")
                uEmail = session.get('user')

                print(platoID)
                print(rRate)
                print("Entra a la parte de Rate")
                existencia = dbCalificaciones.calificacionRepetida(uEmail, platoID)
                print(existencia)
                consulta = dbWish.consultarWishID(platoID, uEmail)
                print(consulta)
                if consulta == False:

                    if existencia == False:

                        resultado = dbCalificaciones.addCalificacion(platoID, uEmail, rRate)
                        if resultado == True:
                            print("Calificacion añadida")
                            #Retornar misma pagina con mismos elementos y calificacion total actualizada
                            tabla = dbComentarios.consultarTodosComentarios(platoID) #Caja de comentarios
                            resultados = db.consultarProductos(platoID) #Elementos de la pagina
                            cantidad = resultados[0][3]
                            if cantidad > 5:
                                cantidad = 5
                            calificaciones = dbCalificaciones.searchCalifcaciones(platoID) #Total de calificaciones
                            print(calificaciones)
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo) 
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)
                                                  

                            if isinstance(tabla, bool) == True: #Imprimir sin tabla
                                
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio= resultados_extra2, wish=False, wish_pID=resultados[0][0])

                            elif isinstance(tabla, bool) == False: #Imprimir con tabla
                                                    
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio= resultados_extra2, wish=False, wish_pID=resultados[0][0])

                        elif resultado == False:
                            print("Calificacion NO añadida")
                            tabla = dbComentarios.consultarTodosComentarios(platoID)
                            resultados = db.consultarProductos(platoID)
                            cantidad = resultados[0][3]
                            if cantidad > 5:
                                cantidad = 5
                            calificaciones = dbCalificaciones.searchCalifcaciones(platoID)
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)
                            print(resultados)
                            if isinstance(tabla, bool) == True: #Imprimir sin tabla
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, error_add_cComment="Algo ha fallado al momento de calificar, Intente mas tarde.", calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])

                            elif isinstance(tabla, bool) == False: #Imprimir con tabla
                                                    
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, error_add_cComment="Algo ha fallado al momento de calificar, Intente mas tarde.", calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])
                            #Retornar misma pagina con mismos elementos pero mensaje de error debajo calificacion

                    elif existencia == True:

                        tabla = dbComentarios.consultarTodosComentarios(platoID)
                        resultados = db.consultarProductos(platoID)
                        cantidad = resultados[0][3]
                        if cantidad > 5:
                            cantidad = 5
                        calificaciones = dbCalificaciones.searchCalifcaciones(platoID)
                        correo = session.get('user')
                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)   
                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], error_add_rRate="Ya has calificado este plato.", calificaciones_promedio= resultados_extra2, wish=False, wish_pID=resultados[0][0])

                elif consulta == True:

                    if existencia == False:

                        resultado = dbCalificaciones.addCalificacion(platoID, uEmail, rRate)
                        if resultado == True:
                            print("Calificacion añadida")
                            #Retornar misma pagina con mismos elementos y calificacion total actualizada
                            tabla = dbComentarios.consultarTodosComentarios(platoID) #Caja de comentarios
                            resultados = db.consultarProductos(platoID) #Elementos de la pagina
                            cantidad = resultados[0][3]
                            if cantidad > 5:
                                cantidad = 5
                            calificaciones = dbCalificaciones.searchCalifcaciones(platoID) #Total de calificaciones
                            print(calificaciones)
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo) 
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)                       

                            if isinstance(tabla, bool) == True: #Imprimir sin tabla
                                
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio= resultados_extra2, wish=True, wish_pID=resultados[0][0])

                            elif isinstance(tabla, bool) == False: #Imprimir con tabla
                                                    
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio= resultados_extra2, wish=True, wish_pID=resultados[0][0])

                        elif resultado == False:
                            print("Calificacion NO añadida")
                            tabla = dbComentarios.consultarTodosComentarios(platoID)
                            resultados = db.consultarProductos(platoID)
                            cantidad = resultados[0][3]
                            if cantidad > 5:
                                cantidad = 5
                            calificaciones = dbCalificaciones.searchCalifcaciones(platoID)
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)
                            print(resultados)
                            if isinstance(tabla, bool) == True: #Imprimir sin tabla
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, error_add_cComment="Algo ha fallado al momento de calificar, Intente mas tarde.", calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])

                            elif isinstance(tabla, bool) == False: #Imprimir con tabla
                                                    
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, error_add_cComment="Algo ha fallado al momento de calificar, Intente mas tarde.", calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])
                            #Retornar misma pagina con mismos elementos pero mensaje de error debajo calificacion

                    elif existencia == True:

                        tabla = dbComentarios.consultarTodosComentarios(platoID)
                        resultados = db.consultarProductos(platoID)
                        cantidad = resultados[0][3]
                        if cantidad > 5:
                            cantidad = 5
                        calificaciones = dbCalificaciones.searchCalifcaciones(platoID)
                        correo = session.get('user')
                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                        
                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)

                        if isinstance(tabla, bool) == True:

                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], error_add_rRate="Ya has calificado este plato.", calificaciones_promedio= resultados_extra2, wish=True, wish_pID=resultados[0][0])

                        elif isinstance(tabla, bool) == False:
                         
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], error_add_rRate="Ya has calificado este plato.", calificaciones_promedio= resultados_extra2, wish=True, wish_pID=resultados[0][0])



            elif 'add_cComment' in a.keys():
                
                cComment = request.form.get("add_cComment")
                platoID = request.form.get("add_pID")
                correo = session.get("user")

                print(cComment, platoID)
                respuesta = dbComentarios.consultarComentario(cComment)
                consulta = dbWish.consultarWishID(ID_respaldo, correo)
                print(consulta)
                if consulta == False:
                
                    if isinstance(respuesta, bool)== False:

                        print("Detecto que el comentario ya existe")
                        tabla = dbComentarios.consultarTodosComentarios(platoID)
                        resultados = db.consultarProductos(platoID)
                        cantidad = resultados[0][3]
                        if cantidad > 5:
                            cantidad = 5
                        calificaciones = dbCalificaciones.searchCalifcaciones(platoID)
                        correo = session.get('user')
                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)
                        print(resultados)               
                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, error_add_cComment="Este comentario ya existe (Esto es una medida de seguridad contra el reenvio de formularios)", username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])

                    elif isinstance(respuesta, bool)==True:

                        print("Detecto que el comentario no existe")
                        correo = session.get('user')
                        confirmacion = dbComentarios.addComentario(correo, platoID, cComment)                
                        print(confirmacion)

                        if confirmacion == False:
                            print("entro a confirmacion false")
                            tabla = dbComentarios.consultarTodosComentarios()                
                            return redirect(url_for('plato', pID = platoID))                       

                        elif confirmacion == True: 
                            print("entro a confirmacion true")
                            tabla = dbComentarios.consultarTodosComentarios(platoID) #Evalua si tiene comentarios o no
                            resultados = db.consultarProductos(platoID)
                            cantidad = resultados[0][3]
                            if cantidad > 5:
                                cantidad = 5
                            calificaciones = dbCalificaciones.searchCalifcaciones(platoID)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)
                            print(resultados)
                            if isinstance(resultados, bool) == False: #Existe el producto

                                if isinstance(tabla, bool) == False: #Encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    print("Encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])

                                elif isinstance(tabla, bool) == True: #No encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    print("No encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])

                            elif isinstance(resultados, bool) == True: #No existe el producto

                                correo = session.get('user')
                                resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)                           
                                print("El producto no existe")
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])

                elif consulta == True:

                    if isinstance(respuesta, bool)== False:

                        print("Detecto que el comentario ya existe")
                        tabla = dbComentarios.consultarTodosComentarios(platoID)
                        resultados = db.consultarProductos(platoID)
                        cantidad = resultados[0][3]
                        if cantidad > 5:
                            cantidad = 5
                        calificaciones = dbCalificaciones.searchCalifcaciones(platoID)
                        correo = session.get('user')
                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)
                        print(resultados)               
                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, error_add_cComment="Este comentario ya existe (Esto es una medida de seguridad contra el reenvio de formularios)", username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])

                    elif isinstance(respuesta, bool)==True:

                        print("Detecto que el comentario no existe")
                        correo = session.get('user')
                        confirmacion = dbComentarios.addComentario(correo, platoID, cComment)                
                        print(confirmacion)

                        if confirmacion == False:
                            print("entro a confirmacion false")
                            tabla = dbComentarios.consultarTodosComentarios()                
                            return redirect(url_for('plato', pID = platoID))                       

                        elif confirmacion == True: 
                            print("entro a confirmacion true")
                            tabla = dbComentarios.consultarTodosComentarios(platoID) #Evalua si tiene comentarios o no
                            resultados = db.consultarProductos(platoID)
                            cantidad = resultados[0][3]
                            if cantidad > 5:
                                cantidad = 5
                            calificaciones = dbCalificaciones.searchCalifcaciones(platoID)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)
                            print(resultados)
                            if isinstance(resultados, bool) == False: #Existe el producto

                                if isinstance(tabla, bool) == False: #Encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    print("Encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])

                                elif isinstance(tabla, bool) == True: #No encontro comentarios
                                    correo = session.get('user')
                                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                    print("No encontro comentarios relacionados al producto")
                                    return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])

                            elif isinstance(resultados, bool) == True: #No existe el producto

                                correo = session.get('user')
                                resultados_extra = dbUsuarios.consultarUsuarios(correo)
                                resultados_extra2 = dbCalificaciones.promedioCalificaciones(platoID)                           
                                print("El producto no existe")
                                return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])


            elif 'wish_pID' in a.keys():

                print("Entro a wish_pID")

                wish_pID = request.form.get("wish_pID")
                print(wish_pID)
                correo = session.get("user")
                consulta = dbWish.consultarWishID(wish_pID, correo)
                
                print(consulta)
                if consulta == False: #Si no existe en la lista de deseos lo añade

                    resultado = dbWish.addWish(correo, wish_pID)
                    print("resultado:", resultado)
                    ID = request.args['pID']
                    print(ID)
                    resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
                    cantidad = resultados[0][3]
                    if cantidad > 5:
                        cantidad = 5
                    tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
                    calificaciones = dbCalificaciones.searchCalifcaciones(ID)
                    print(resultados)
                    print(tabla)
                    if isinstance(resultados, bool) == False: #Existe el producto

                        if isinstance(tabla, bool) == False: #Encontro comentarios
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                            print("Encontro comentarios relacionados al producto")
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation_wish="Producto agregado a la Lista de deseos.")
                        elif isinstance(tabla, bool) == True: #No encontro comentarios
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                            print("No encontro comentarios relacionados al producto")
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation_wish="Producto agregado a la Lista de deseos.")

                    elif isinstance(resultados, bool) == True: #No existe el producto

                        correo = session.get('user')
                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                        print("El producto no existe")
                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0], Confirmation_wish="Producto agregado a la Lista de deseos.")
                
                elif consulta == True:

                    ID = request.args['pID']
                    print(ID)
                    resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
                    cantidad = resultados[0][3]
                    if cantidad > 5:
                        cantidad = 5
                    tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
                    calificaciones = dbCalificaciones.searchCalifcaciones(ID)
                    print(resultados)
                    print(tabla)
                    if isinstance(resultados, bool) == False: #Existe el producto

                        if isinstance(tabla, bool) == False: #Encontro comentarios
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                            print("Encontro comentarios relacionados al producto")
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish_pID=resultados[0][0], wish=True)
                        elif isinstance(tabla, bool) == True: #No encontro comentarios
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                            print("No encontro comentarios relacionados al producto")
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish_pID=resultados[0][0], wish=True)

                    elif isinstance(resultados, bool) == True: #No existe el producto

                        correo = session.get('user')
                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                        print("El producto no existe")
                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish_pID=resultados[0][0])

            else:
                print("SE FUE PARA EL ELSE LUEGO DE POST")

                ID = request.args['pID']
                correo = session.get("user")
                print(ID)
                resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
                tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
                calificaciones = dbCalificaciones.searchCalifcaciones(ID)
                consulta = dbWish.consultarWishID(ID, correo)
                print("Encontro el wish:", consulta)
                cantidad = resultados[0][3]
                if cantidad > 5:
                    cantidad = 5
                print(consulta)
                if consulta == False:
                    if isinstance(resultados, bool) == False: #Existe el producto

                        if isinstance(tabla, bool) == False: #Encontro comentarios
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                            print("Encontro comentarios relacionados al producto")
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])
                        elif isinstance(tabla, bool) == True: #No encontro comentarios
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                            print("No encontro comentarios relacionados al producto")
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])

                    elif isinstance(resultados, bool) == True: #No existe el producto

                        correo = session.get('user')
                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                        print("El producto no existe")
                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=False, wish_pID=resultados[0][0])

                elif consulta == True:

                    if isinstance(resultados, bool) == False: #Existe el producto

                        if isinstance(tabla, bool) == False: #Encontro comentarios
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                            print("Encontro comentarios relacionados al producto")
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])
                        elif isinstance(tabla, bool) == True: #No encontro comentarios
                            correo = session.get('user')
                            resultados_extra = dbUsuarios.consultarUsuarios(correo)
                            resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                            print("No encontro comentarios relacionados al producto")
                            return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])

                    elif isinstance(resultados, bool) == True: #No existe el producto

                        correo = session.get('user')
                        resultados_extra = dbUsuarios.consultarUsuarios(correo)
                        resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)                    
                        print("El producto no existe")
                        return render_template("product_user.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=cantidad, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2, wish=True, wish_pID=resultados[0][0])


        elif request.method == 'GET':

            print("ENTRA AL GET")

    elif 'user' in session and session['rol'] == "Administrador":

        if request.method == 'POST':

            print("RECIBIO POST") 
            ID_respaldo = request.args['pID']
            print(ID_respaldo)     

            a = request.form
            print(a)

            ID = request.args['pID']
            print(ID)
            resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
            tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
            calificaciones = dbCalificaciones.searchCalifcaciones(ID)
            print(resultados)
            print(tabla)
            if isinstance(resultados, bool) == False: #Existe el producto

                if isinstance(tabla, bool) == False: #Encontro comentarios
                    correo = session.get('user')
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                    print("Encontro comentarios relacionados al producto")
                    return render_template("product_sadmin.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=resultados[0][3], comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2)
                elif isinstance(tabla, bool) == True: #No encontro comentarios
                    correo = session.get('user')
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                    print("No encontro comentarios relacionados al producto")
                    return render_template("product_sadmin.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=resultados[0][3], calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2)
    
    elif 'user' in session and session['rol'] == "Superadministrador":

        if request.method == 'POST':

            print("RECIBIO POST") 
            ID_respaldo = request.args['pID']
            print(ID_respaldo)     

            a = request.form
            print(a)

            ID = request.args['pID']
            print(ID)
            resultados = db.consultarProductos(ID) #Consulta el producto actual para poder recargarlo
            tabla = dbComentarios.consultarTodosComentarios(ID) #Consulta si existen comentarios para este producto
            calificaciones = dbCalificaciones.searchCalifcaciones(ID)
            print(resultados)
            print(tabla)
            if isinstance(resultados, bool) == False: #Existe el producto

                if isinstance(tabla, bool) == False: #Encontro comentarios
                    correo = session.get('user')
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                    print("Encontro comentarios relacionados al producto")
                    return render_template("product_sadmin.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=resultados[0][3], comments_jinja=tabla, calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2)
                elif isinstance(tabla, bool) == True: #No encontro comentarios
                    correo = session.get('user')
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                    resultados_extra2 = dbCalificaciones.promedioCalificaciones(ID)
                    print("No encontro comentarios relacionados al producto")
                    return render_template("product_sadmin.html", plato_pName=resultados[0][1], plato_pPrice=resultados[0][2], plato_pDescription=resultados[0][4], plato_pID= resultados[0][0], cantidad=resultados[0][3], calificaciones=calificaciones, username=resultados_extra[0][1], calificaciones_promedio=resultados_extra2)

    return "<h1>Contenido inexistente</h1>"

@app.route('/profile', methods=('GET', 'POST'))
def profile():

    print("Ingresa a profile")
   
    if 'user' in session and session['rol'] == "Usuario":

        print("Ingresa a user")

        if request.method == 'POST':
            print("RECIBIO POST")
            a = request.form
            print("FORMULARIO ENVIADO:")
            print(a)

            if 'upgrade_uName' in a.keys():
                print("Ingresa formulario 1")

                uName = request.form.get("upgrade_uName")
                uLastname = request.form.get("upgrade_uLastname")
                uPhone = request.form.get("upgrade_uPhone")
                correo = session.get('user')
                resultado = dbUsuarios.actualizarUsuarios(uName, correo, uLastname, uPhone)
                
                confirmacion = ""
                if resultado == True:
                    confirmacion = "Tu usuario ha sido actualizado."
                elif resultado == False:
                    confirmacion = "Algo ha fallado en la actualizacion de tu usuario."

                resultados = dbUsuarios.consultarUsuarios(correo)
                print(resultados)

                if isinstance(resultados, bool)==False:
                    return render_template("profile_user.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], confirmation_upgrade=confirmacion)
                elif isinstance(resultados, bool)==True:
                    return "<h1>Usuario no encontrado</h1>"
            
            elif 'upgrade_uPass' in a.keys():
                print("Ingresa formulario 2")

                uPass = str(request.form.get("upgrade_uPass"))
                print(uPass)
                resultados = dbUsuarios.consultarUsuarios(session.get('user'))
                print(resultados)
                pwHash = resultados[0][4]

                respuesta = bcrypt.check_password_hash(pwHash, uPass)
                
                if respuesta == True: #la contraseña coincide con la de la base de datos

                    uNewpass = request.form.get("upgrade_uNewpass")
                    pw_hash = bcrypt.generate_password_hash(uNewpass)
                    correo = session.get('user')
                    resultado = dbUsuarios.actualizarPassword(correo, pw_hash)
                    
                    confirmacion = ""
                    if resultado == True: #Se ha actualizado la contraseña
                        #Ahora renderizamos la pagina del perfil
                        confirmacion = "Tu contraseña ha sido actualizada."
                        resultados = dbUsuarios.consultarUsuarios(correo) #Se trae los contenidos del perfil nuevamente
                        print(resultados)

                        if isinstance(resultados, bool)==False:
                            return render_template("profile_user.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], confirmation_password=confirmacion)
                        elif isinstance(resultados, bool)==True:
                            return "<h1>Usuario no encontrado al momento de cargar contenidos de la pagina</h1>"

                    elif resultado == False:
                        confirmacion = "Algo ha fallado en la actualizacion de tu contraseña."
                        resultados = dbUsuarios.consultarUsuarios(correo) #Se trae los contenidos del perfil nuevamente
                        print(resultados)

                        if isinstance(resultados, bool)==False:
                            return render_template("profile_user.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], confirmation_password=confirmacion)
                        elif isinstance(resultados, bool)==True:
                            return "<h1>Usuario no encontrado al momento de cargar contenidos de la pagina</h1>"


                elif respuesta == False:
                    
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo) #Se trae los contenidos del perfil nuevamente
                    print(resultados)
                    confirmacion="Contraseña incorrecta, ingresa tu contraseña actual nuevamente."

                    if isinstance(resultados, bool)==False:
                        return render_template("profile_user.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], error_upgrade_uPass1=confirmacion)
                    elif isinstance(resultados, bool)==True:
                        return "<h1>Usuario no encontrado al momento de cargar contenidos de la pagina</h1>"

            elif len(a) == 0:

                print("Ingresa a formulario 3")
                correo = session.get('user')
                resultado = dbUsuarios.deleteUsuarios(correo)
                
                return redirect('/login')

        if request.method == 'GET':

            correo = session.get('user')
            print(correo)
            resultados = dbUsuarios.consultarUsuarios(correo)
            print(resultados)

            if isinstance(resultados, bool)==False:
                return render_template("profile_user.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3])
            elif isinstance(resultados, bool)==True:
                return "<h1>Usuario no encontrado</h1>"


     #admin...
     ###########################################################           
    elif 'user' in session and session['rol'] == "Administrador":

        print("Ingresa a user")

        if request.method == 'POST':
            print("RECIBIO POST")
            a = request.form
            print("FORMULARIO ENVIADO:")
            print(a)

        if request.method == 'GET':

            correo = session.get('user')
            print(correo)
            resultados = dbUsuarios.consultarUsuarios(correo)
            print(resultados)

            if isinstance(resultados, bool)==False:
                return render_template("profile_admin.html", username=resultados[0][1], upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3])
            elif isinstance(resultados, bool)==True:
                return "<h1>Usuario no encontrado</h1>"

     #superAdmin
     ##################################################################
    elif 'user' in session and session['rol'] == "Superadministrador":

        print("Ingresa a user")

        if request.method == 'POST':
            print("RECIBIO POST")
            a = request.form
            print("FORMULARIO ENVIADO:")
            print(a)

            if 'upgrade_uName' in a.keys():
                print("Ingresa formulario 1")

                uName = request.form.get("upgrade_uName")
                uLastname = request.form.get("upgrade_uLastname")
                uPhone = request.form.get("upgrade_uPhone")
                correo = session.get('user')
                resultado = dbUsuarios.actualizarUsuarios(uName, correo, uLastname, uPhone)
                
                confirmacion = ""
                if resultado == True:
                    confirmacion = "Tu usuario ha sido actualizado."
                elif resultado == False:
                    confirmacion = "Algo ha fallado en la actualizacion de tu usuario."

                resultados = dbUsuarios.consultarUsuarios(correo)
                print(resultados)

                if isinstance(resultados, bool)==False:
                    return render_template("profile_sadmin.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], confirmation_upgrade=confirmacion, username=resultados[0][1])
                elif isinstance(resultados, bool)==True:
                    return "<h1>Usuario no encontrado</h1>"
            
            elif 'upgrade_uPass' in a.keys():
                print("Ingresa formulario 2")

                uPass = str(request.form.get("upgrade_uPass"))
                print(uPass)
                resultados = dbUsuarios.consultarUsuarios(session.get('user'))
                print(resultados)
                pwHash = resultados[0][4]

                respuesta = bcrypt.check_password_hash(pwHash, uPass)
                
                if respuesta == True: #la contraseña coincide con la de la base de datos

                    uNewpass = request.form.get("upgrade_uNewpass")
                    pw_hash = bcrypt.generate_password_hash(uNewpass)
                    correo = session.get('user')
                    resultado = dbUsuarios.actualizarPassword(correo, pw_hash)
                    
                    confirmacion = ""
                    if resultado == True: #Se ha actualizado la contraseña
                        #Ahora renderizamos la pagina del perfil
                        confirmacion = "Tu contraseña ha sido actualizada."
                        resultados = dbUsuarios.consultarUsuarios(correo) #Se trae los contenidos del perfil nuevamente
                        print(resultados)

                        if isinstance(resultados, bool)==False:
                            return render_template("profile_sadmin.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], confirmation_password=confirmacion, username=resultados[0][1])
                        elif isinstance(resultados, bool)==True:
                            return "<h1>Usuario no encontrado al momento de cargar contenidos de la pagina</h1>"

                    elif resultado == False:
                        confirmacion = "Algo ha fallado en la actualizacion de tu contraseña."
                        resultados = dbUsuarios.consultarUsuarios(correo) #Se trae los contenidos del perfil nuevamente
                        print(resultados)

                        if isinstance(resultados, bool)==False:
                            return render_template("profile_sadmin.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], confirmation_password=confirmacion, username=resultados[0][1])
                        elif isinstance(resultados, bool)==True:
                            return "<h1>Usuario no encontrado al momento de cargar contenidos de la pagina</h1>"


                elif respuesta == False:
                    
                    correo = session.get('user')
                    resultados = dbUsuarios.consultarUsuarios(correo) #Se trae los contenidos del perfil nuevamente
                    print(resultados)
                    confirmacion="Contraseña incorrecta, ingresa tu contraseña actual nuevamente."

                    if isinstance(resultados, bool)==False:
                        return render_template("profile_sadmin.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], error_upgrade_uPass1=confirmacion, username=resultados[0][1])
                    elif isinstance(resultados, bool)==True:
                        return "<h1>Usuario no encontrado al momento de cargar contenidos de la pagina</h1>"

            elif len(a) == 0:

                print("Ingresa a formulario 3")
                correo = session.get('user')
                resultado = dbUsuarios.deleteUsuarios(correo)
                
                return redirect('/login')

        if request.method == 'GET':

            correo = session.get('user')
            print(correo)
            resultados = dbUsuarios.consultarUsuarios(correo)
            print(resultados)

            if isinstance(resultados, bool)==False:
                return render_template("profile_sadmin.html", upgrade_uEmail=resultados[0][0], upgrade_uName=resultados[0][1], upgrade_uLastname=resultados[0][2], upgrade_uPhone=resultados[0][3], username=resultados[0][1])
            elif isinstance(resultados, bool)==True:
                return "<h1>Usuario no encontrado</h1>"

    return "<h1>Contenido inexistente</h1>"

@app.route('/comments_user', methods=('GET', 'POST'))
def comments_user():

    if 'user' in session and session['rol'] == "Superadministrador":

        print("INGRESA SUPERADMIN A COMENTARIOS")
        if request.method == 'POST':
            
            print("RECIBE METODO POST")
            a = request.form
            print("FORMULARIO ENVIADO:")
            print(a)

            if 'delete_cID' in a.keys():

                print("Ingresa formulario 1")
                cID = request.form.get("delete_cID")
                print(cID)
                resultados = dbComentarios.eliminarComentario(cID)
                print(resultados)

                if resultados == True: #Se hizo la eliminacion y ahora debe recargar la pagina
                    correo = session.get('user')
                    resultados = dbComentarios.consultarComentariosTodos()
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)

                    return render_template("comments_sadmin.html", delete_confirm="El comentario ha sido eliminado.", variable_jinja=resultados, username=resultados_extra[0][1])
                
                elif resultados == False:

                    correo = session.get('user')
                    resultados = dbComentarios.consultarComentariosTodos()
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)

                    return render_template("comments_sadmin.html", error_delete_cID="No se encontro la ID.", variable_jinja=resultados, username=resultados_extra[0][1])

        if request.method == 'GET':
            
            correo = session.get('user')
            print(correo)
            resultados = dbComentarios.consultarComentariosTodos()
            resultados_extra = dbUsuarios.consultarUsuarios(correo)

            if isinstance(resultados, bool) == True:
                return render_template("comments_sadmin.html", username=resultados_extra[0][1])            
            elif isinstance(resultados, bool) == False:
                return render_template("comments_sadmin.html", variable_jinja=resultados, username=resultados_extra[0][1])
        
    if 'user' in session and session['rol'] == "Usuario":

        if request.method == 'POST':
            
            print("RECIBE METODO POST")
            a = request.form
            print("FORMULARIO ENVIADO:")
            print(a)

            if 'search_cID' in a.keys():

                print("Ingresa formulario 1")
                cID = request.form.get("search_cID")
                print(cID)
                resultados = dbComentarios.consultarComentario(cID)
                print(resultados)

                if isinstance(resultados, bool)==False:

                    resultados_extra = db.consultarProductos(resultados[0][1])
                    correo = session.get('user')
                    resultados = dbComentarios.consultarComentariosUsuario(correo)
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                    resultados_verdadero = dbComentarios.consultarComentario(cID)

                    print(resultados_verdadero)
                    return render_template("comments_user.html", upgrade_cID=resultados_verdadero[0][0], upgrade_pID=resultados_verdadero[0][1], upgrade_pName=resultados_extra[0][1], upgrade_cComment=resultados_verdadero[0][3], variable_jinja=resultados, username=resultados_extra[0][1])
                
                elif isinstance(resultados, bool)==True:
                    
                    correo = session.get('user')
                    resultados = dbComentarios.consultarComentariosUsuario(correo)
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                    return render_template("comments_user.html", error_search_cID="No se encontro la ID.", variable_jinja=resultados, username=resultados_extra[0][1])

            elif 'upgrade_cID' in a.keys():

                print("Ingresa formulario 2")
                cID = request.form.get("upgrade_cID")
                print(cID)
                upgrade_cComment = request.form.get("upgrade_cComment")
                print(upgrade_cComment)
                resultado = dbComentarios.actualizarComentario(upgrade_cComment, cID)
                if resultado == True:

                    correo = session.get('user')
                    resultados = dbComentarios.consultarComentariosUsuario(correo)
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)

                    return render_template("comments_user.html", confirmation_upgrade="El comentario ha sido actualizado.", variable_jinja=resultados, username = resultados_extra[0][1])

            elif 'delete_cID' in a.keys():

                print("Ingresa formulario 3")
                cID = request.form.get("delete_cID")
                print(cID)
                resultados = dbComentarios.eliminarComentario(cID)
                print(resultados)

                if resultados == True: #Se hizo la eliminacion y ahora debe recargar la pagina
                    correo = session.get('user')
                    resultados = dbComentarios.consultarComentariosUsuario(correo)
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)
                    if isinstance(resultados, bool) == True:

                        return render_template("comments_user.html", delete_confirm="El comentario ha sido eliminado.", username=resultados_extra[0][1])

                    elif isinstance(resultados, bool) == False:

                        return render_template("comments_user.html", delete_confirm="El comentario ha sido eliminado.", variable_jinja=resultados, username=resultados_extra[0][1])
                
                elif resultados == False:

                    correo = session.get('user')
                    resultados = dbComentarios.consultarComentariosUsuario(correo)
                    resultados_extra = dbUsuarios.consultarUsuarios(correo)

                    return render_template("comments_user.html", error_delete_cID="No se encontro la ID.", variable_jinja=resultados, username=resultados_extra[0][1])

        if request.method == 'GET':
            
            correo = session.get('user')
            print(correo)
            resultados = dbComentarios.consultarComentariosUsuario(correo)
            resultados_extra = dbUsuarios.consultarUsuarios(correo)
            if isinstance(resultados, bool) == True:

                return render_template("comments_user.html", username=resultados_extra[0][1])

            elif isinstance(resultados, bool) == False:

                return render_template("comments_user.html", variable_jinja=resultados, username=resultados_extra[0][1])
            
            print(resultados)
            return render_template("comments_user.html", variable_jinja=resultados, username=resultados_extra[0][1])

    return "<h1>Contenido inexistente</h1>"

@app.route('/wish', methods=('GET', 'POST'))
def wish():

    if 'user' in session and session['rol'] == "Usuario":

        if request.method == 'POST':
            print("ENTRO A WISH")
            
            #Revisar DELETE
            correo = session.get("user")
            pID = request.form.get("delete_pID")
            print(pID)
            resultados = dbWish.eliminarWish(pID, correo)
            print(resultados)

            if resultados == True: #Se encontro la ID y se elimino de Wish

                print("SE ENCONTRO LA ID")
                correo = session.get("user")
                print(correo)
                
                resultados = dbUsuarios.consultarUsuarios(correo)
                pID = dbWish.consultarWish(correo)
                if isinstance(pID, bool)==True:

                    return render_template("wish_user.html", username= resultados[0][1], Confirmation="Se ha removido el producto de tu Lista exitosamente.")
                elif isinstance(pID, bool)==False:
                
                    resultados_platos = []
                    for i in pID:

                        resultados_platos.append(db.consultarProductos(i[0]))
                        
                    print(resultados_platos)
                    print(resultados_platos[0][0])


                    return render_template("wish_user.html", username = resultados[0][1], variable_jinja=resultados_platos, Confirmation="Se ha removido el producto de tu Lista exitosamente.")
            
            elif resultados == False: #No se encontro la ID

                correo = session.get("user")
                resultados = dbUsuarios.consultarUsuarios(correo)
                pID = dbWish.consultarWish(correo)
                print(pID)
                resultados_platos = []
                for i in pID:

                    resultados_platos.append(db.consultarProductos(i[0]))
                    
                print(resultados_platos)
                print(resultados_platos[0][0])


                return render_template("wish_user.html", username = resultados[0][1], variable_jinja=resultados_platos, error_delete_pID="No se encontro la ID del producto en tu Lista de Deseos.")

        
        if request.method == 'GET':

            correo = session.get("user")
            resultados = dbUsuarios.consultarUsuarios(correo) #Consulta el nombre del usuario para imprimirlo arriba
            pID = dbWish.consultarWish(correo) #Consulta todos los productos en la lista del usuario conectado
            print(pID)
            resultados_platos = []
            if isinstance(pID, bool)==True:

                return render_template("wish_user.html", username = resultados[0][1])

            elif isinstance(pID, bool) == False:

                print("EVALUAR::::::::::::::")
                print(pID)

                for i in pID:

                    resultados_platos.append(db.consultarProductos(i[0])) #Consulta la informacion de cada uno de los productos por separado y los apendiza a una lista                
                print(resultados_platos)              

                return render_template("wish_user.html", username = resultados[0][1], variable_jinja=resultados_platos)
    
    return "<h1>Contenido inexistente</h1>"

Direccion = None
Carrito = None

@app.route('/car', methods=('GET', 'POST'))
def car():

    if 'user' in session and session['rol'] == "Usuario":
        
        # caID = 
        correo = session.get("user")
        usuario = dbUsuarios.consultarUsuarios(correo)
        user = usuario[0][1]
        pID_car = dbCar.carritoEmail(correo) #Me traigo la ID del ultimo carrito del usuario
        print("CARRITO ACTUAL")
        global Carrito
        Carrito = pID_car[0][0]
        print(pID_car)

        if pID_car[0][0] == None or pID_car[0][0] == "": #Si no hay carrito (osea, carrito eliminado)

            return render_template("car_user.html")
        
        else: #Existe carrito

            pIDs_car = dbCar.carritoIDs(pID_car[0][0]) #Me traigo las IDS de los producto del carrito
            if pIDs_car[0][0] == None: #Evaluo si el carrito esta vacio
                
                if request.method == 'POST':
                    
                    a = request.form
                    if request.form.get("delete_billing"):

                        return render_template("car_user.html", total=0, subtotal=0, delete_confirmation="No se encontraron productos en tu carrito para eliminar.", username=user)

                    if 'sale_bID' in a.keys(): #Evita que el usuario inicie proceso de compra sin tener productos

                        print("Detecto boton de comprar sin productos en el carrito")
                        return render_template("car_user.html", total=0, subtotal=0, error_pruchase="No se encontraron productos en tu carrito para comprar.", username=user)

                    elif 'upgrade_pID' in a.keys():
                        
                        return render_template("car_user.html", total=0, subtotal=0, error_add_bAddress="Añade productos a tu carrito antes de comenzar con la compra", username=user)

                return render_template("car_user.html", total=0, subtotal=0, username=user) #Carga la pagina sin productos del carrito


            else: #El carrito esta lleno

                productos = [] #Aqui concateno la informacion de todos los registros asociados a la ID del carrito del usuario
                lista_intermedia = pIDs_car[0][0].split("-") #Me traigo las ID del carrito
                print(lista_intermedia)
                count = -1
                for i in lista_intermedia:
                    count += 1
                    print("count:", count)
                    lista = []
                    resultado_info = db.consultarProductos(int(i)) #Me traigo toda la informacion de inventario del producto actual
                    resultado_car = dbCar.carritoConsultar(pID_car[0][0]) #Me traigo toda la informacion del carrito actual
                    print(resultado_car)
                    pIDs = resultado_car[0][1].split("-") #Separo todas las ID del carrito actual
                    pAmounts = resultado_car[0][3].split("-") #Separo todas las Cantidades del carrito actual
                    print(pIDs)
                    print(pAmounts)
                    lista.append(resultado_info[0][0]) #Apendizo informacion del producto
                    lista.append(resultado_info[0][1])
                    lista.append(resultado_info[0][2])
                    lista.append(resultado_info[0][4])
                    precio = resultado_info[0][2]
                    cantidad = pAmounts[count]
                    total = precio*float(cantidad)
                    lista.append(pIDs[count]) #Apendizo IDs a la par de su respectivo amount
                    lista.append(pAmounts[count])
                    lista.append(total)
                    productos.append(lista) #Apendizo a la lista principal que le mandare a Jinja

                #A este punto ya existe la tabla de carrito con toda la informacion, ahora oslo queda desplegarla

                if count > 0:
                    count = 0

                subtotal = 0
                for i in productos:
                    subtotal += i[6]
        
                total = subtotal + 10000.0
                print(productos)
                global Direccion
                print(Direccion)                       

                if request.method == 'POST':
                    print("Recibe POST")

                    a = request.form

                    if request.form.get("delete_billing"):
                                              
                        print("Entro a eliminar carrito")
                        dbCar.carritoVaciar(Carrito)
                        return render_template("car_user.html", subtotal=0, total=0, car_pID=pID_car[0][0], delete_confirmation="Carrito limpiado.", username=user)

                    if 'upgrade_pID' in a.keys():
                                      
                        Direccion = request.form.get("add_bAddress")
                        print(Direccion)

                        return render_template("car_user.html", variable_jinja=productos, subtotal=subtotal, total=total, car_pID=pID_car[0][0], sale_bID=pID_car[0][0], username=user)
                        

                    if 'sale_bID' in a.keys():                      
                                         
                        print(Direccion)
                        if Direccion == "" or Direccion == None:
                            
                            return render_template("car_user.html", variable_jinja=productos, subtotal=subtotal, total=total, car_pID=pID_car[0][0], error_pruchase="Porfavor ingrese un destino de domicilio antes de realizar la compra.", username=user)

                        elif len(Direccion) > 0:
                            
                            print("CARRITO ID")
                            print(Carrito)
                            dbCar.carritoUpdate(Carrito) #Actualizo estatus del carrito que compre
                            dbCar.carritoUpdateFecha(Carrito) #Actualizo la fecha a la fecha de compra
                            dbCar.carritoCrearPrimeraVez(correo, 0) #Creo un nuevo carrito

                            #Billing
                            pID_car = dbCar.carritoEmail(correo) #Agarro la ID del carrito que acabe de comprar
                            today = date.today()
                            fecha = today.strftime("%d/%m/%Y")
                            dbBilling.addBilling(Carrito, Direccion, fecha)
                            #Billing
                            
                            return render_template("car_user.html", purchase_confirmation="Compra procesada exitosamente!", subtotal=0, total=0, car_pID=pID_car[0][0], username=user)


                if request.method == 'GET':

                    Direccion = None
                    Carrito = None
                    print("ENTRA AL GET")
                    return render_template("car_user.html", variable_jinja=productos, subtotal=subtotal, total=total, car_pID=pID_car[0][0], username=user)

                return "<h1>Revisa consola</h1>"
        
    return redirect('/login')
         
@app.route('/billing', methods=('GET', 'POST'))
def billing():

    if 'user' in session and session['rol'] == "Usuario":

        correo = session.get("user")
        carritos = dbBilling.carritoConsultarEmail(correo) #Todos los carritos asociados al usuario
        historico = []
        for ID in carritos: #Saco informacion de carrito por carrito
            
            fecha = ID[1]
            pIDs_car = dbCar.carritoIDs(ID[0]) #Saco los productos del carrito actual (iterante)

            if pIDs_car[0][0] == None: #Evaluo si el carrito actual esta vacio
                continue

            else:
                
                lista_intermedia = pIDs_car[0][0].split("-")
                #Divide los elementos en el campo de productos del carrito actual
                count = -1
                for i in lista_intermedia: #Se lleva cada producto individual para asi juntarlo con la fecha
                    count += 1
                    Nombre = db.consultarProductos(i)
                    print(i)                
                    lista = []
                    lista.append(fecha)
                    lista.append(i)
                    lista.append(Nombre[0][1])
                    resultado_car = dbCar.carritoConsultar(ID[0])
                    print(resultado_car)
                    resultado_info = db.consultarProductos(int(i))
                    pAmounts = resultado_car[0][3].split("-")
                    precio = resultado_info[0][2]
                    cantidad = pAmounts[count]
                    total = precio*float(cantidad)
                    lista.append(cantidad)
                    lista.append(precio)
                    lista.append(total) 
                    # lista.append(pAmounts[count])
                    historico.append(lista)
                
        return render_template("billing_user.html", variable_jinja=historico)
    
    if 'user' in session and session['rol'] == "Superadministrador":

        carritos = dbCar.carritoTodoID()
        correo = session.get("user")
        correo_consulta = dbUsuarios.consultarUsuarios(correo)
        nombre = correo_consulta[0][1]
        historico = []

        print(carritos)
        for ID in carritos: #Saco informacion de carrito por carrito        
            
            consulta = dbCar.carritoConsultar(ID[0])
            comprante = consulta[0][2]
            comprante = dbUsuarios.consultarUsuarios(comprante)
            if comprante == False:
                cliente = consulta[0][2]
            else:
                cliente = comprante[0][1]
            #POR HACER: AGARRAR EL CORREO ASOCIADO A CADA CARRITO
            fecha_primero = dbCar.carritoConsultar(ID[0])
            fecha = fecha_primero[0][4]
            pIDs_car = dbCar.carritoIDs(ID[0]) #Saco los productos del carrito actual (iterante)

            if pIDs_car[0][0] == None: #Evaluo si el carrito actual esta vacio
                continue

            else:
                
                lista_intermedia = pIDs_car[0][0].split("-")
                #Divide los elementos en el campo de productos del carrito actual
                count = -1
                for i in lista_intermedia: #Se lleva cada producto individual para asi juntarlo con la fecha
                    count += 1
                    Nombre = db.consultarProductos(i)                
                    lista = []
                    lista.append(fecha)
                    lista.append(i)
                    lista.append(cliente)
                    lista.append(Nombre[0][1])
                    resultado_car = dbCar.carritoConsultar(ID[0])
                    resultado_info = db.consultarProductos(int(i))
                    pAmounts = resultado_car[0][3].split("-")
                    precio = resultado_info[0][2]
                    cantidad = pAmounts[count]
                    total = precio*float(cantidad)
                    lista.append(cantidad)
                    lista.append(precio)
                    lista.append(total) 
                    # lista.append(pAmounts[count])
                    historico.append(lista)
                
        print(historico)
        return render_template("billing_sadmin.html", variable_jinja=historico, username=nombre)

    if 'user' in session and session['rol'] == "Administrador":

        carritos = dbCar.carritoTodoID()
        correo = session.get("user")
        correo_consulta = dbUsuarios.consultarUsuarios(correo)
        nombre = correo_consulta[0][1]
        historico = []

        print(carritos)
        for ID in carritos: #Saco informacion de carrito por carrito        
            
            consulta = dbCar.carritoConsultar(ID[0])
            comprante = consulta[0][2]
            comprante = dbUsuarios.consultarUsuarios(comprante)
            if comprante == False:
                cliente = consulta[0][2]
            else:
                cliente = comprante[0][1]
            #POR HACER: AGARRAR EL CORREO ASOCIADO A CADA CARRITO
            fecha_primero = dbCar.carritoConsultar(ID[0])
            fecha = fecha_primero[0][4]
            pIDs_car = dbCar.carritoIDs(ID[0]) #Saco los productos del carrito actual (iterante)

            if pIDs_car[0][0] == None: #Evaluo si el carrito actual esta vacio
                continue

            else:
                
                lista_intermedia = pIDs_car[0][0].split("-")
                #Divide los elementos en el campo de productos del carrito actual
                count = -1
                for i in lista_intermedia: #Se lleva cada producto individual para asi juntarlo con la fecha
                    count += 1
                    Nombre = db.consultarProductos(i)                
                    lista = []
                    lista.append(fecha)
                    lista.append(i)
                    lista.append(cliente)
                    lista.append(Nombre[0][1])
                    resultado_car = dbCar.carritoConsultar(ID[0])
                    resultado_info = db.consultarProductos(int(i))
                    pAmounts = resultado_car[0][3].split("-")
                    precio = resultado_info[0][2]
                    cantidad = pAmounts[count]
                    total = precio*float(cantidad)
                    lista.append(cantidad)
                    lista.append(precio)
                    lista.append(total) 
                    # lista.append(pAmounts[count])
                    historico.append(lista)
                
        print(historico)
        return render_template("billing_admin.html", variable_jinja=historico, username=nombre)


if __name__=="__main__":
    app.run(debug=True, port=6001)
 
#Ultima vez editado: 10/27/2021 9:50