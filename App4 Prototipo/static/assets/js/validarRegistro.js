const signup_uName = document.getElementById("signup_uName");
const signup_uLastname = document.getElementById("signup_uLastname");
const signup_uEmail = document.getElementById("signup_uEmail");
const signup_uPhone = document.getElementById("signup_uPhone");
const signup_uPassword = document.getElementById("signup_uPassword");
const signup_uPassword2 = document.getElementById("signup_uPassword2");
const signup_form = document.getElementById("signup_form");
const error_signup_uName = document.getElementById("error_signup_uName");
const error_signup_uLastname = document.getElementById("error_signup_uLastname");
const error_signup_uEmail = document.getElementById("error_signup_uEmail");
const error_signup_uPhone = document.getElementById("error_signup_uPhone");
const error_signup_uPassword = document.getElementById("error_signup_uPassword");
const error_signup_uPassword2 = document.getElementById("error_signup_uPassword2");
const email = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;

function validarTexto(parametro){
   var patron = /^[a-zA-Z\s]*$/;
   if(parametro.search(patron)){
     return false;
   } else{
     return true; 
   }
  
}

function validar_Registro(){
    
    console.log("Entro a validarUsuarios()")
    //REVISAR
    let flag = false;
    let errorN = "";
    let errorL = "";
    let errorE = "";
    let errorPh = "";
    let errorPw = "";
    let errorPw2 = "";

    if(signup_uName.value.length == 0 || signup_uName.value.length == null){
        flag = true;
        errorN = "Ingrese un nombre de usuario <br>"
        console.log ("entró al signup_uName");
    } else if(validarTexto(signup_uName.value)==false){
        errorN = "Ingrese solo letras <br>";    
        console.log("aqui vamos nuevo metodo validar texto");
        flag = true;
    } else if(signup_uName.value.length <= 2){
        console.log("Nombre es menor a 3")
        flag = true;
        errorN = "Ingrese un Nombre mas largo <br>";
    } else if(signup_uName.value.length >=25){
        flag = true; 
        errorN = "Ingrese un Nombre mas corto <br>";
    } else if(!isNaN(signup_uName)){
        flag = true;
        errorL = "Ingrese un nombre correcto <br>";
    }


    if(signup_uLastname.value.length == 0 || signup_uLastname.value.length == null){
        flag = true;
        errorL = "Ingrese un apellido de usuario <br>"
        console.log ("entró al add_uLastame");
    } else if(validarTexto(signup_uLastname.value)==false){
        errorL = "Ingrese solo letras <br>";    
        console.log("aqui vamos nuevo metodo validar texto");
        flag = true;
    } else if(signup_uLastname.value.length <= 2){
        flag = true;
        errorL = "Ingrese un Nombre mas largo <br>";
    } else if(signup_uLastname.value.length >=25){
        flag = true; 
        errorL = "Ingrese un apellido mas corto <br>";
    } else if(!isNaN(signup_uLastname)){
        flag = true;
        errorL = "Ingrese un apellido correcto <br>";
    }

    if(signup_uEmail.value.length == 0 || signup_uEmail.value.length == null){
        console.log("entró al error del email")
        flag = true;
        errorE = "Ingrese un Email <br>"
    } else if (!(email.test(signup_uEmail.value))) {
        flag = true;
        errorE = "Ingrese un email valido";
        console.log ("entró al error del email")
    }

    
    if(signup_uPhone.value.length == 0 || signup_uPhone.value.length == null){
        console.log("entro al error de phone")
        flag = true;
        errorPh = "Ingrese un numero  de telefono"
    } else if(!(signup_uPhone.value.length==10)){
        flag = true;
        errorPh = "Ingrese un numero de telefono valido"
    } else if(isNaN(signup_uPhone.value) == true){
        flag = true;  
        errorPh = "Ingrese un numero de telefono valido"
    }

    if(signup_uPassword.value.length == 0 || signup_uPassword.value.length == null){
        flag = true;
        errorPw ="Ingrese una contraseña";
    } else if(signup_uPassword.value.length < 4 || signup_uPassword.value.length >15){
        flag = true; 
        errorPw ="Ingrese una contraseña entre 4 y 15 caracteres";
    }
    
    if(signup_uPassword2.value.length ==0 || signup_uPassword2.value.length == null){
        console.log("Contraseña2 esta vacia")
        flag = true;
        errorPw2 = "Ingrese una contraseña"
    }else if(signup_uPassword2.value != signup_uPassword.value){
        flag = true;
        errorPw2 = "Las contraseñas no coinciden"
    }

    console.log(flag)
    

    if(flag==true){
        console.log("pasó por aquí en el true")
        error_signup_uName.innerHTML = errorN
        error_signup_uLastname.innerHTML = errorL
        error_signup_uPhone.innerHTML = errorPh
        error_signup_uEmail.innerHTML = errorE
        error_signup_uPassword.innerHTML = errorPw
        error_signup_uPassword2.innerHTML = errorPw2
    } else {
        console.log("paso por aqui en el false")
        document.getElementById("signup_form").submit();
        // document.getElementById("signup_form").refresh();
        errorN = "";
        errorL = "";
        errorE = "";
        errorPh = "";
        errorPw = "";
        errorPw2 = "";
        error_signup_uName.innerHTML = errorN
        error_signup_uLastname.innerHTML = errorL
        error_signup_uPhone.innnerHTML = errorPh
        error_signup_uEmail.innerHTML = errorE
        error_signup_uPassword.innerHTML = errorPw
        error_signup_uPassword2.innerHTML = errorPw2
        
    }
}